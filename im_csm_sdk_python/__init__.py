"""im-csm-sdk-python package."""

# IM CSM SDK Python
# A Python SDK for Interactúa Móvil Contact SMS services

# Core functionality
from .core.contacts import list_contacts, get_contact
from .core.messages import (
    list_messages,
    send_to_contact,
)
from .core.status import get_status

# Configuration
from .configs.config import get_config
from .configs.logger import logger

__version__ = '1.0.0'
__author__ = 'IM Team'
__email__ = 'support@interactuamovil.com'

__all__ = [
    # Core functions
    'list_contacts',
    'get_contact',
    'list_messages',
    'send_to_contact',
    'get_status',
    # Configuration
    'get_config',
    # Meta info
    '__version__',
    '__author__',
    '__email__',
]