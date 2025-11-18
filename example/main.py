"""Example usage of the IM CSM SDK Python."""

import sys
import os
import random
import argparse
from datetime import datetime, timedelta
from typing import List, Optional
from uuid import uuid4

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

ALLOWED_STATUS = ("ACTIVE", "INACTIVE")


def _generate_alias() -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(random.choice(alphabet) for _ in range(8))


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
            alias=_generate_alias(),
        )
    )
    logger.info(
        f'Created shortlink: {created.short_url} (alias={created.alias or "auto"}) - Status: {created.status}'
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
            f'{shortlink.status} - alias={shortlink.alias or "auto"}'
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

            if (shortlink.status or "").upper() == 'ACTIVE':
                logger.info(f'Deactivating shortlink: {shortlink_id}')
                updated = im_sdk.update_shortlink_status(shortlink_id, 'INACTIVE')
                logger.info(f'Updated status: {updated.status}')
            else:
                logger.info('Shortlink already INACTIVE. Reactivation is not supported.')


def main():
    """Main example function."""
    if len(sys.argv) > 1 and sys.argv[1] == 'shortlinks':
        run_shortlinks_cli(sys.argv[2:])
        return

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


def run_shortlinks_cli(cli_args: List[str]) -> None:
    """Command-line interface for shortlink operations."""
    parser = argparse.ArgumentParser(
        prog='python example/main.py shortlinks',
        description='Shortlinks command runner',
    )
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('run', help='Run the full shortlinks example flow (default)')

    create = subparsers.add_parser('create', help='Create a shortlink')
    create.add_argument('long_url', help='Long URL to shorten')
    create.add_argument('name', nargs='?', default=None, help='Optional shortlink name')
    create.add_argument(
        'status',
        nargs='?',
        default='ACTIVE',
        help='Optional status (default ACTIVE)',
    )
    create.add_argument('alias', nargs='?', default=None, help='Optional alias (no spaces)')

    list_cmd = subparsers.add_parser('list', help='List shortlinks')
    list_cmd.add_argument('limit', nargs='?', type=int, default=10, help='Limit (default 10)')
    list_cmd.add_argument(
        'offset',
        nargs='?',
        type=int,
        default=-6,
        help='Offset / timezone (default -6)',
    )

    date_cmd = subparsers.add_parser('date', help='List shortlinks by date range')
    date_cmd.add_argument('start_date', help='Start date (YYYY-MM-DD)')
    date_cmd.add_argument('end_date', help='End date (YYYY-MM-DD)')
    date_cmd.add_argument('limit', nargs='?', type=int, default=10)
    date_cmd.add_argument('offset', nargs='?', type=int, default=-6)

    get_cmd = subparsers.add_parser('id', help='Get shortlink by ID')
    get_cmd.add_argument('shortlink_id', help='Shortlink url_id')

    update_cmd = subparsers.add_parser('update', help='Update shortlink status (INACTIVE only)')
    update_cmd.add_argument('shortlink_id', help='Shortlink url_id')
    update_cmd.add_argument('status', help='New status (only INACTIVE supported)')

    subparsers.add_parser('status', help='Show allowed statuses')

    args = parser.parse_args(cli_args)
    command = args.command or 'run'

    if command == 'run':
        example_shortlinks()
        return
    if command == 'create':
        shortlinks_create(args.long_url, args.name, args.status, args.alias)
        return
    if command == 'list':
        shortlinks_list(limit=args.limit, offset=args.offset)
        return
    if command == 'date':
        shortlinks_list(
            start_date=args.start_date,
            end_date=args.end_date,
            limit=args.limit,
            offset=args.offset,
        )
        return
    if command == 'id':
        shortlinks_get(args.shortlink_id)
        return
    if command == 'update':
        shortlinks_update(args.shortlink_id, args.status)
        return
    if command == 'status':
        logger.info('Allowed statuses: ACTIVE (create) / INACTIVE (deactivation only).')
        return
    parser.print_help()


def shortlinks_create(
    long_url: str,
    name: Optional[str],
    status: Optional[str],
    alias: Optional[str],
) -> None:
    normalized_status = (status or 'ACTIVE').strip().upper()
    if normalized_status not in ALLOWED_STATUS:
        raise ValueError(f'Invalid status {status!r}. Use one of {ALLOWED_STATUS}.')
    logger.info(f'Creating shortlink: {long_url}')
    created = im_sdk.create_shortlink(
        CreateShortlinkData(
            long_url=long_url,
            name=name,
            status=normalized_status,
            alias=alias,
        )
    )
    logger.info(
        f'Created: {created.short_url} '
        f'(alias={created.alias or "auto"}, status={created.status or normalized_status})'
    )


def shortlinks_list(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> None:
    params = ListShortlinksParams(
        start_date=start_date,
        end_date=end_date,
        limit=limit,
        offset=offset,
    )
    shortlinks = im_sdk.list_shortlinks(params)
    logger.info(f'Found {len(shortlinks)} shortlinks')
    for shortlink in shortlinks[:10]:
        logger.info(
            f'Shortlink {shortlink.url_id or shortlink._id} - {shortlink.short_url} '
            f'(status={shortlink.status}, alias={shortlink.alias or "auto"})'
        )


def shortlinks_get(shortlink_id: str) -> None:
    logger.info(f'Fetching shortlink: {shortlink_id}')
    shortlink = im_sdk.get_shortlink_by_id(shortlink_id)
    logger.info(
        f'Shortlink {shortlink.url_id or shortlink._id} - {shortlink.short_url} '
        f'(status={shortlink.status}, visits={shortlink.visits})'
    )


def shortlinks_update(shortlink_id: str, status: str) -> None:
    normalized = status.strip().upper()
    if normalized != 'INACTIVE':
        raise ValueError('Shortlinks can only transition to INACTIVE.')
    logger.info(f'Updating shortlink {shortlink_id} to {normalized}')
    updated = im_sdk.update_shortlink_status(shortlink_id, normalized)
    logger.info(f'Updated status: {updated.status}')


if __name__ == '__main__':
    main()
