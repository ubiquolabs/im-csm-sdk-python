import base64
import hashlib
import hmac
import json
from datetime import datetime
from urllib.parse import quote as q_parse

from loguru import logger

from ..utils.sort_params import sort_params


def authorization(config):
    """Generate authentication headers for API requests.

    Args:
        config(dict): Configuration containing apiKey, apiSecret, data

    Returns:
        dict: Authentication headers with Date and Authorization
    """
    logger.info('Step 2. Create authorization headers')

    auth = {}
    formatted_params = ''
    formatted_data = ''
    formatted_date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

    if not config.get('apiKey') or not config.get('apiSecret'):
        return 'Keys are needed!'

    if config.get('data'):
        formatted_data = json.dumps(config['data'], separators=(',', ':'))

    if config.get('params'):
        sorted_params = sort_params(config['params'])
        formatted_params = '&'.join(
            [
                f'{key}={q_parse(str(sorted_params[key])).replace("%20", "+")}'
                for key in sorted_params
            ]
        )

    canonical_string = (
        f'{config["apiKey"]}{formatted_date}{formatted_params}{formatted_data}'
    )

    # Create HMAC-SHA1 signature and encode in base64
    sign = hmac.new(
        config['apiSecret'].encode('utf-8'),
        canonical_string.encode('utf-8'),
        hashlib.sha1,
    ).digest()
    signature = base64.b64encode(sign).decode('utf-8')

    logger.trace(
        f'{formatted_data=}, {formatted_params=}, {canonical_string=}, {signature=}'
    )

    auth['Date'] = formatted_date
    auth['Authorization'] = f'IM {config["apiKey"]}:{signature}'

    logger.trace(f'Auth headers: {auth}')

    return auth
