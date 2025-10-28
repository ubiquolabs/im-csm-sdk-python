"""Example usage of the IM CSM SDK Python."""

from datetime import datetime, timedelta
from uuid import uuid4

import sys
import os

# Add parent directory to path to ensure we can import the package
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
from im_csm_sdk_python.schemas.shortlinks import (
    CreateShortlinkData,
    ListShortlinksParams,
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
    contact = im_sdk.get_contact('50212345678')
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
            msisdn='50212345678',
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
            msisdn='50212345678',
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


def example_shortlinks():
    """Example of using shortlinks functions."""
    logger.info('=== Testing Shortlinks ===')

    logger.info('Creating shortlink...')
    created = im_sdk.create_shortlink(
        CreateShortlinkData(
            long_url='https://www.example.com/very-long-url-with-parameters',
            name='Example Shortlink',
            status='ACTIVE',
        )
    )
    logger.info(
        f'Created shortlink: {created.short_url} - Status: {created.status}'
    )

    logger.info('Listing shortlinks...')
    shortlinks = im_sdk.list_shortlinks(
        ListShortlinksParams(
            limit=10,
            offset=-6,
        )
    )
    logger.info(f'Found {len(shortlinks)} shortlinks')
    for shortlink in shortlinks[:3]:
        logger.info(
            f'Shortlink: {shortlink.name} - {shortlink.short_url} - '
            f'{shortlink.status}'
        )

    if shortlinks:
        shortlink_id = shortlinks[0].url_id or shortlinks[0]._id
        if shortlink_id:
            logger.info(f'Getting shortlink by ID: {shortlink_id}')
            shortlink = im_sdk.get_shortlink_by_id(shortlink_id)
            logger.info(
                f'Shortlink details: {shortlink.name} - Visits: '
                f'{shortlink.visits}'
            )

            logger.info(f'Updating shortlink status: {shortlink_id}')
            updated = im_sdk.update_shortlink_status(shortlink_id, 'INACTIVE')
            logger.info(f'Updated status: {updated.status}')


def main():
    """Main example function."""
    logger.info('Starting IM CSM SDK Python Example')

    try:
        # example_contacts()
        # example_messages()
        # example_send_to_tags()
        # example_status()
        example_shortlinks()

        logger.info('All examples completed successfully!')

    except Exception as e:
        logger.error(f'Example failed: {e}')
        raise


if __name__ == '__main__':
    main()
