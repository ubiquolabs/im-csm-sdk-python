"""Example usage of the IM CSM SDK Python."""

from datetime import datetime, timedelta
from uuid import uuid4

import im_csm_sdk_python as im_sdk
from im_csm_sdk_python.configs.logger import logger
from im_csm_sdk_python.schemas.contacts import (
    ListContactsParams,
)
from im_csm_sdk_python.schemas.messages import (
    ListMessagesParams,
    MessageDirection,
    SendToContactData,
    SendToTagsData,
)


def example_contacts():
    """Example of using contacts functions."""
    logger.info('=== Testing Contacts ===')

    logger.info('Listing contacts...')
    contacts = im_sdk.list_contacts(
        ListContactsParams(
            start=0,
            limit=10,
            query='Julio',
        )
    )
    logger.info(f'Found {len(contacts)} contacts')
    for contact in contacts[:3]:  # Show first 3
        logger.info(f'Contact: {contact.full_name} ({contact.msisdn})')

    logger.info('Getting contact...')
    contact = im_sdk.get_contact('50231241024')
    logger.info(f'Contact: {contact.full_name} ({contact.msisdn})')


def example_messages():
    """Example of using messages functions."""
    logger.info('=== Testing Messages ===')

    logger.info('Listing messages...')
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    messages = im_sdk.list_messages(
        ListMessagesParams(
            start_date=start_date,
            end_date=end_date,
            start=0,
            limit=50,
            msisdn='50231241024',
            direction=MessageDirection.MT,
            delivery_status_enable=True,
        )
    )
    logger.info(f'Found {len(messages)} messages')
    for message in messages[:3]:  # Show first 3
        logger.info(
            f'Message: {message.message_id} - {message.direction} - {message.msisdn} - {message.message}'  # noqa: E501
        )
    logger.info('Sending message to contact...')
    sent_message = im_sdk.send_to_contact(
        SendToContactData(
            msisdn='50211241024',
            message='Hello from Python SDK!',
            id=str(uuid4()),
        )
    )
    logger.info(
        f'Sent message: {sent_message.message_id} - {sent_message.status}'
    )


def example_status():
    """Example of using status function."""
    logger.info('=== Testing Status ===')

    status = im_sdk.get_status()
    logger.info(f'API Status: {status}')


def example_send_to_tags():
    """Example of using send to tags function."""
    logger.info('=== Testing Send to Tags ===')

    sent_message = im_sdk.send_to_tags(
        SendToTagsData(
            tags=['python'],
            message='Hello from Python SDK with tags!',
            id=str(uuid4()),
        )
    )
    logger.info(f'Sent message: {sent_message.id=} - {sent_message.status=}')


def main():
    """Main example function."""
    logger.info('Starting IM CSM SDK Python Example')

    try:
        # example_contacts()
        # example_messages()
        # example_send_to_tags()
        example_status()

        logger.info('All examples completed successfully!')

    except Exception as e:
        logger.error(f'Example failed: {e}')
        raise


if __name__ == '__main__':
    main()
