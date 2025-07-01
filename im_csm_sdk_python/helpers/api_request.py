from urllib.parse import urljoin

from httpx import HTTPStatusError, Response, request
from loguru import logger

from ..configs.config import get_config
from ..helpers.authentication import authorization
from ..schemas.request import ApiRequest


def send_request(api_request: ApiRequest) -> Response:
    """Send authenticated request to API.

    Args:
        api_request (ApiRequest): Request data containing type, endpoint, params, data

    Returns:
        httpx.Response: Response from the API

    Raises:
        ValueError: If required API configuration is missing
        HTTPStatusError: If HTTP request fails
    """
    request_config = get_config()

    request_config['params'] = api_request.params
    request_config['data'] = api_request.data

    try:
        auth = authorization(request_config)
    except Exception as e:
        logger.error(f'Failed to generate authorization: {e}')
        raise

    try:
        logger.info(
            f'Step 3. Send {api_request.type} request to {api_request.endpoint}'  # noqa: E501
        )
        logger.trace(f'Data: {api_request.data}')
        logger.trace(f'Params: {api_request.params}')

        response = request(
            method=api_request.type,
            url=urljoin(
                request_config['url'], f'/api/rest{api_request.endpoint}'
            ),
            json=api_request.data,
            params=api_request.params,
            headers={
                'Date': auth['Date'],
                'Authorization': auth['Authorization'],
            },
        )

        # Raise for HTTP errors
        response.raise_for_status()

        logger.trace(f'Request URL: {response.request.url}')
        logger.trace(f'Request response: {response.json()}')
        logger.trace(f'Request response status: {response.status_code}')

        return response

    except HTTPStatusError as e:
        logger.error(f'HTTP error {e.response.status_code}: {e}')
        raise e
    except Exception as e:
        logger.error(f'Request failed: {e}')
        raise
