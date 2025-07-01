from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ApiRequestType(str, Enum):
    """Enum for HTTP request types."""

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class ApiRequest(BaseModel):
    """Request schema for API calls.

    Attributes:
        type (ApiRequestType): The type of request (e.g., "GET", "POST").
        endpoint (str): The API endpoint to call.
        params (dict, optional): Query parameters for the request.
        data (dict, optional): Data to send in the request body.
    """
    model_config = ConfigDict(use_enum_values=True)

    endpoint: str = Field(description='The API endpoint to call')
    type: ApiRequestType = Field(
        description="The type of request (e.g., 'GET', 'POST')"
    )
    params: Optional[dict] = Field(
        default=None, description='Query parameters for the request'
    )
    data: Optional[dict] = Field(
        default=None, description='Data to send in the request body'
    )

    @field_validator('endpoint')
    @classmethod
    def validate_endpoint(cls, v: str) -> str:
        """Validate endpoint format.

        Args:
            v: The endpoint string to validate

        Returns:
            str: The validated endpoint

        Raises:
            ValueError: If endpoint is empty or has invalid format
        """
        if not v or v.strip() == '':
            raise ValueError('Endpoint cannot be empty')

        # Ensure endpoint starts with '/'
        if not v.startswith('/'):
            v = f'/{v}'

        return v
