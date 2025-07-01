from typing import Any, Dict

from loguru import logger

from ..helpers.api_request import send_request
from ..schemas.request import ApiRequest, ApiRequestType


def get_status() -> Dict[str, Any]:
    """Get the status of the API.

    Returns:
        Dict[str, Any]: The status information from the API

    Raises:
        ValueError: If API response is invalid
    """
    try:
        logger.info('Step 1. Get API status')

        response = send_request(
            ApiRequest(
                type=ApiRequestType.GET,
                endpoint='status',
            )
        )

        return response.json()
    except Exception as e:
        logger.error(f'Error getting status: {e}')
        raise e
