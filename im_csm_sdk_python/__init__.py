"""im-csm-sdk-python package."""

# IM CSM SDK Python
# A Python SDK for Interactúa Móvil Contact SMS services

# Core functionality
# Configuration
from .configs.config import get_config
from .configs.logger import logger
from .core.contacts import get_contact, list_contacts
from .core.messages import (
    list_messages,
    send_to_contact,
)
from .core.status import get_status

__all__ = [
    # Core functions
    'list_contacts',
    'get_contact',
    'list_messages',
    'send_to_contact',
    'get_status',
    # Configuration
    'get_config',
    'logger',
]
