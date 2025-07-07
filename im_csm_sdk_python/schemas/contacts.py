from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ContactStatus(str, Enum):
    """Enum for contact status."""

    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    BLOCKED = 'BLOCKED'


class Contact(BaseModel):
    """Schema for a contact."""

    model_config = ConfigDict(use_enum_values=True)

    msisdn: Optional[str] = Field(
        description='The phone number of the contact', default=None
    )
    tags: list[str] = Field(description='The tags associated with the contact')
    first_name: Optional[str] = Field(
        description='The first name of the contact', default=None
    )
    last_name: Optional[str] = Field(
        description='The last name of the contact', default=None
    )
    full_name: Optional[str] = Field(
        description='The full name of the contact', default=None
    )
    email: Optional[str] = Field(
        description='The email address of the contact', default=None
    )
    status: str = Field(description='The status of the contact')
    phone_number: Optional[str] = Field(
        description='The phone number without country code', default=None
    )
    country_code: Optional[str] = Field(
        description='The country code of the phone number', default=None
    )
    added_from: Optional[str] = Field(
        description='The source from which the contact was added', default=None
    )
    profile_uid: str = Field(
        description='The unique identifier of the contact profile'
    )
    monitoring: bool = Field(
        description='Whether the contact is being monitored'
    )


class ListContactsParams(BaseModel):
    """Schema for the parameters of a list contacts request."""

    model_config = ConfigDict(use_enum_values=True)

    status: Optional[list[ContactStatus]] = Field(
        default=None, description='The contact status to find'
    )
    query: Optional[str] = Field(
        default=None, description='The query string for search'
    )
    start: Optional[int] = Field(
        default=None, description='The offset (start index)', ge=0
    )
    limit: Optional[int] = Field(
        default=None, description='The limit of results', ge=1
    )
