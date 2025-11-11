"""Shortlinks core functions."""

from typing import List, Optional

from loguru import logger
from pydantic import TypeAdapter

from ..helpers.api_request import send_request
from ..schemas.request import ApiRequest, ApiRequestType
from ..schemas.shortlinks import (
    CreateShortlinkData,
    ListShortlinksParams,
    Shortlink,
    UpdateShortlinkStatusData,
)

ta_shortlinks = TypeAdapter(List[Shortlink])
ta_shortlink = TypeAdapter(Shortlink)


def list_shortlinks(params: Optional[ListShortlinksParams] = None) -> List[Shortlink]:
    """List all shortlinks.

    Args:
        params (Optional[ListShortlinksParams]): Parameters for listing shortlinks.

    Returns:
        List[Shortlink]: List of shortlinks

    Raises:
        Exception: If API response is invalid
    """
    try:
        logger.info("Listing shortlinks")

        request_params = None
        if params:
            request_params = params.model_dump(exclude_none=True)

        response = send_request(
            ApiRequest(
                type=ApiRequestType.GET,
                endpoint="short_link/",
                params=request_params,
            )
        )

        # Get raw content and decode properly
        content = response.content
        if isinstance(content, bytes):
            content = content.decode('utf-8', errors='ignore')
        
        import json
        data = json.loads(content)

        if isinstance(data, dict) and "data" in data:
            return ta_shortlinks.validate_python(data["data"])
        return ta_shortlinks.validate_python(data)

    except Exception as e:
        logger.error(f"Error listing shortlinks: {e}")
        raise e


def get_shortlink_by_id(shortlink_id: str) -> Shortlink:
    """Get a shortlink by ID.

    Args:
        shortlink_id (str): The shortlink ID.

    Returns:
        Shortlink: The shortlink information

    Raises:
        Exception: If API response is invalid
    """
    try:
        logger.info(f"Getting shortlink by ID: {shortlink_id}")

        response = send_request(
            ApiRequest(
                type=ApiRequestType.GET,
                endpoint="short_link/",
                params={"id": shortlink_id},
            )
        )

        data = response.json()

        if isinstance(data, dict) and "url_id" in data:
            return ta_shortlink.validate_python(data)
        return ta_shortlink.validate_python(data)

    except Exception as e:
        logger.error(f"Error getting shortlink by ID: {e}")
        raise e


def create_shortlink(data: CreateShortlinkData) -> Shortlink:
    """Create a new shortlink.

    Args:
        data (CreateShortlinkData): The shortlink data.

    Returns:
        Shortlink: The created shortlink

    Raises:
        Exception: If API response is invalid
    """
    try:
        if data.alias:
            logger.info("Creating shortlink: %s (alias=%s)", data.long_url, data.alias)
        else:
            logger.info("Creating shortlink: %s", data.long_url)

        response = send_request(
            ApiRequest(
                type=ApiRequestType.POST,
                endpoint="short_link",
                data=data.model_dump(exclude_none=True),
            )
        )

        data_response = response.json()

        return ta_shortlink.validate_python(data_response)

    except Exception as e:
        logger.error(f"Error creating shortlink: {e}")
        raise e


def update_shortlink_status(
    shortlink_id: str, status: str
) -> Shortlink:
    """Update shortlink status."""
    try:
        logger.info(f"Updating shortlink status: {shortlink_id} to {status}")
        if status.upper() == "ACTIVE":
            raise ValueError("Shortlinks cannot be reactivated; only INACTIVE updates are supported.")

        response = send_request(
            ApiRequest(
                type=ApiRequestType.PUT,
                endpoint=f"short_link/{shortlink_id}/status",
                params={"id": shortlink_id},
                data={"status": status},
            )
        )

        data = response.json()

        return ta_shortlink.validate_python(data)

    except Exception as e:
        logger.error(f"Error updating shortlink status: {e}")
        raise e

