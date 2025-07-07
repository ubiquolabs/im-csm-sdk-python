# im-csm-sdk-python

Python SDK for IM CSM API

## Overview

This SDK provides a simple and efficient way to interact with the IM CSM API from Python applications. It allows you to manage contacts, send and list messages, and check API status with easy-to-use functions and Pydantic models.

## Requirements

- Python 3.8+
- [Pydantic v2](https://docs.pydantic.dev/)
- [FastAPI](https://fastapi.tiangolo.com/) (for advanced usage)
- Other dependencies are listed in `pyproject.toml`

## Installation

### Option 1: Using requirements.txt (Recommended for production)

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies using requirements.txt
pip install -r requirements.txt
```

### Option 2: Using uv (Fastest)

```bash
# Install uv if you haven't already
pip install uv

# Create and activate a virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

## Configuration

If your SDK requires configuration (e.g., API keys, endpoints), set them as environment variables or in a config file. See `im_csm_sdk_python/configs/config.py` for details.

## Usage Example

You can test the SDK using the provided example script:

```bash
python example/main.py
```

This script demonstrates how to list messages, send a message, and interact with contacts. Check the code in `example/main.py` for more details and usage patterns.

## Main Operations

- **Status**
  - Get API status: `im_csm_sdk_python.get_status()`
- **Contacts**
  - List contacts: `im_csm_sdk_python.list_contacts(params)`
  - Get a contact: `im_csm_sdk_python.get_contact(msisdn)`
- **Messages**
  - List messages: `im_csm_sdk_python.list_messages(params)`
  - Send message to contact: `im_csm_sdk_python.send_to_contact(data)`

## Contributing

Feel free to open issues or submit pull requests to improve the SDK. Please ensure your code follows the project's style guidelines and includes appropriate tests.
