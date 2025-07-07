from typing import List

from loguru import logger
from pydantic import TypeAdapter

from ..helpers.api_request import send_request
from ..schemas.messages import (
    ListMessagesParams,
    Message,
    SendToContactData,
    SendToContactResponse,
    SendToTagsData,
    SendToTagsResponse,
)
from ..schemas.request import ApiRequest, ApiRequestType

ta_messages = TypeAdapter(List[Message])
ta_message = TypeAdapter(Message)
ta_send_to_contact_response = TypeAdapter(SendToContactResponse)
ta_send_to_tags_response = TypeAdapter(SendToTagsResponse)


def list_messages(params: ListMessagesParams) -> List[Message]:
    """Gets log message list.

    Args:
        params (ListMessagesParams): The parameters to list the messages.

    Returns:
        List[Message]: List of messages

    Raises:
        Exception: If API response is invalid
    """
    try:
        logger.info('Step 1. List messages')

        response = send_request(
            ApiRequest(
                type=ApiRequestType.GET,
                endpoint='messages',
                params=params.model_dump(exclude_none=True),
            )
        )

        data = response.json()

        return ta_messages.validate_python(data)
    except Exception as e:
        logger.error(f'Error listing messages: {e}')
        raise e


def send_to_contact(data: SendToContactData) -> SendToContactResponse:
    """Sends a message to a specific contact.

    Args:
        data (SendToContactData): The data payload to send the message.

    Returns:
        Message: The message just sent

    Raises:
        Exception: If API response is invalid
    """
    try:
        logger.info(f'Step 1. Send message to contact {data.msisdn}')

        response = send_request(
            ApiRequest(
                type=ApiRequestType.POST,
                endpoint='messages/send_to_contact',
                data=data.model_dump(exclude_none=True),
            )
        )

        response_data = response.json()
        return ta_send_to_contact_response.validate_python(response_data)
    except Exception as e:
        logger.error(f'Error sending message to contact: {e}')
        raise e


def send_to_tags(data: SendToTagsData) -> SendToTagsResponse:
    """Sends a message to a specific tag.

    Args:
        data (SendToTagsData): The data payload to send the message.
    """
    try:
        logger.info(f'Step 1. Send message to tags {data.tags}')

        response = send_request(
            ApiRequest(
                type=ApiRequestType.POST,
                endpoint='messages/send',
                data=data.model_dump(exclude_none=True),
            )
        )

        response_data = response.json()
        return ta_send_to_tags_response.validate_python(response_data)
    except Exception as e:
        logger.error(f'Error sending message to tags: {e}')
        raise e
