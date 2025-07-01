from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class MessageDirection(str, Enum):
    """Enum for the direction of a message."""

    ALL = 'ALL'
    MT = 'MT'
    MO = 'MO'


class Message(BaseModel):
    """Schema for a message."""

    message_id: str = Field(description='The unique identifier of the message')
    short_code: str = Field(
        description='The short code used to send the message'
    )
    type: int = Field(description='The type of the message')
    direction: MessageDirection = Field(
        description='The direction of the message (ALL/MT/MO)'
    )
    status: str = Field(description='The status of the message')
    message: str = Field(description='The content/text of the message')
    sent_count: int = Field(description='Number of successfully sent messages')
    error_count: int = Field(description='Number of messages with errors')
    total_recipients: int = Field(description='Total number of recipients')
    msisdn: str = Field(
        description='The phone number associated with the message'
    )
    country: str = Field(description='The country code')
    is_billable: bool = Field(description='Whether the message is billable')
    is_scheduled: bool = Field(description='Whether the message is scheduled')
    created_on: datetime = Field(description='When the message was created')
    created_by: str = Field(description='User who created the message')


class ListMessagesParams(BaseModel):
    """Schema for the parameters of a messages list request."""

    model_config = ConfigDict(use_enum_values=True)

    start_date: Optional[datetime] = Field(
        description='The start date of the messages', default=None
    )
    end_date: Optional[datetime] = Field(
        description='The end date of the messages', default=None
    )
    start: Optional[int] = Field(
        description='The offset of the results (-1 to ignore)', default=-1
    )
    limit: Optional[int] = Field(
        description='The limit of the result list (-1 to ignore)', default=-1
    )
    msisdn: Optional[str] = Field(
        description='The phone number of the contact', default=None
    )
    direction: Optional[MessageDirection] = Field(
        description='The direction of the messages', default=None
    )


class SendToContactData(BaseModel):
    """Schema for the data payload of a send message to contact request."""

    msisdn: str = Field(description='The phone number to send the message to')
    message: str = Field(description='The message content to send')
    id: Optional[str] = Field(
        description='Optional message identifier', default=None
    )


class SendToContactResponse(BaseModel):
    """Schema for the response of a send message to contact request."""

    message_id: str = Field(description='The ID of the sent message')
    short_code: str = Field(
        description='The short code used to send the message'
    )
    type: int = Field(description='The type of message')
    direction: MessageDirection = Field(
        description='The direction of the message (MT/MO)'
    )
    status: str = Field(description='The status of the sent message')
    sent_from: str = Field(
        description='Source from where the message was sent'
    )
    id: str = Field(description='Unique identifier for the message')
    message: str = Field(description='The message content sent')
    sent_count: int = Field(description='Number of messages sent')
    error_count: int = Field(description='Number of errors occurred')
    total_recipients: int = Field(description='Total number of recipients')
    msisdn: str = Field(description='The phone number the message was sent to')
    country: str = Field(description='Country code')
    is_billable: bool = Field(description='Whether the message is billable')
    is_scheduled: bool = Field(description='Whether the message is scheduled')
    created_on: datetime = Field(description='When the message was created')
    created_by: str = Field(description='Who created the message')
    total_monitors: int = Field(description='Total number of monitors')


class SendToTagsData(BaseModel):
    """Schema for the data payload of a send message to tags request."""

    tags: list[str] = Field(description='The tags to send the message to')
    message: str = Field(description='The message content to send')
    id: Optional[str] = Field(
        description='Optional message identifier', default=None
    )


class SendToTagsResponse(BaseModel):
    """Schema for the response of a send message to tags request."""

    id: str = Field(description='Unique identifier for the message')
    short_code: str = Field(
        description='The short code used to send the message'
    )
    type: int = Field(description='The type of message')
    direction: MessageDirection = Field(
        description='The direction of the message (MT/MO)'
    )
    status: str = Field(description='The status of the sent message')
    sent_from: str = Field(
        description='Source from where the message was sent'
    )
    message: str = Field(description='The message content sent')
    sent_count: int = Field(description='Number of messages sent')
    error_count: int = Field(description='Number of errors occurred')
    total_recipients: int = Field(description='Total number of recipients')
    is_billable: bool = Field(description='Whether the message is billable')
    is_scheduled: bool = Field(description='Whether the message is scheduled')
    created_on: datetime = Field(description='When the message was created')
    total_monitors: int = Field(description='Total number of monitors')
