import os
from typing import Any, Dict

from dotenv import load_dotenv

load_dotenv()


def get_config() -> Dict[str, Any]:
    """Get configuration from environment variables.

    Returns:
        Dict[str, Any]: Configuration dictionary

    Raises:
        ValueError: If required environment variables are missing
    """
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    url = os.getenv('URL')

    if not api_key or not api_secret or not url:
        missing = []
        if not api_key:
            missing.append('API_KEY')
        if not api_secret:
            missing.append('API_SECRET')
        if not url:
            missing.append('URL')
        raise ValueError(
            f'Missing required environment variables: {", ".join(missing)}'
        )

    return {
        'apiKey': api_key,
        'apiSecret': api_secret,
        'url': url,
    }


# For backwards compatibility, but prefer get_config()
config = {
    'apiKey': os.getenv('API_KEY'),
    'apiSecret': os.getenv('API_SECRET'),
    'url': os.getenv('URL'),
}
