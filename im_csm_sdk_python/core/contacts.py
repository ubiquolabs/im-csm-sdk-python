from typing import List

from loguru import logger
from pydantic import TypeAdapter

from ..helpers.api_request import send_request
from ..schemas.contacts import Contact, ListContactsParams
from ..schemas.request import ApiRequest, ApiRequestType

ta_contacts = TypeAdapter(List[Contact])
ta_contact = TypeAdapter(Contact)


def list_contacts(params: ListContactsParams) -> List[Contact]:
    """List all contacts.

    Args:
        params (ListContactsParams): The parameters to list the contacts.

    Returns:
        List[Contact]: List of contacts

    Raises:
        Exception: If API response is invalid
    """
    try:
        logger.info('Step 1. List contacts')

        response = send_request(
            ApiRequest(
                type=ApiRequestType.GET,
                endpoint='contacts',
                params=params.model_dump(exclude_none=True),
            )
        )

        data = response.json()

        return ta_contacts.validate_python(data)
    except Exception as e:
        logger.error(f'Error listing contacts: {e}')
        raise e


def get_contact(msisdn: str) -> Contact:
    """Get a contact by MSISDN.

    Args:
        msisdn (str): The MSISDN number of the contact to retrieve.

    Returns:
        Contact: The contact information

    Raises:
        Exception: If API response is invalid
    """
    try:
        logger.info(f'Step 1. Get contact {msisdn}')

        response = send_request(
            ApiRequest(
                type=ApiRequestType.GET,
                endpoint=f'contacts/{msisdn}',
                params={'msisdn': msisdn},
            )
        )

        data = response.json()

        return ta_contact.validate_python(data)
    except Exception as e:
        logger.error(f'Error getting contact: {e}')
        raise e
