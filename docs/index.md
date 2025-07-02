# IM CSM SDK Python

Python SDK for Interactúa Móvil Contact SMS services

## Overview

The IM CSM SDK Python provides a simple and efficient way to interact with the Interactúa Móvil Contact SMS API from Python applications. It allows you to manage contacts, send and list messages, and check API status with easy-to-use functions and Pydantic models.

## Features

- **Contact Management**: List and retrieve contact information
- **Message Operations**: Send messages and retrieve message history
- **Status Monitoring**: Check API service status
- **Type Safety**: Full Pydantic v2 support with type hints
- **Error Handling**: Comprehensive error handling and logging

## Quick Start

### Installation

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the SDK
pip install -e .
```

### Configuration

Set up your environment variables:

```bash
export API_KEY="your_api_key"
export API_SECRET="your_api_secret"
export URL="https://api.example.com"
```

Or create a `.env` file:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
URL=https://api.example.com
```

### Basic Usage

```python
import im_csm_sdk_python as im_sdk
from im_csm_sdk_python.schemas.contacts import ListContactsParams
from im_csm_sdk_python.schemas.messages import SendToContactData

# List contacts
contacts = im_sdk.list_contacts(
    ListContactsParams(limit=10, query="John")
)

# Get a specific contact
contact = im_sdk.get_contact("1234567890")

# Send a message
sent_message = im_sdk.send_to_contact(
    SendToContactData(
        msisdn="1234567890",
        message="Hello from Python SDK!",
        id="unique-message-id"
    )
)

# Check API status
status = im_sdk.get_status()
```

## Example Usage

Run the complete example:

```bash
python example/main.py
```

This example demonstrates all the main features of the SDK including contact management, message operations, and status checking.

## Requirements

- Python 3.8+
- httpx >= 0.28.1
- pydantic >= 2.10.6
- loguru >= 0.7.3
- python-dotenv >= 1.0.1

## Next Steps

- [Configuration Guide](configuration.md) - Learn how to configure the SDK
- [Examples](examples/index.md) - More usage examples
- [API Reference](reference/index.md) - Complete API documentation
- [Troubleshooting](troubleshooting.md) - Common issues and solutions 