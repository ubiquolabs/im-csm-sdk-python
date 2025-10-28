# im-csm-sdk-python

Python SDK for IM CSM API

## Overview

This SDK provides a simple and efficient way to interact with the IM CSM API from Python applications. It allows you to manage contacts, send and list messages, create and manage shortlinks, and check API status with easy-to-use functions and Pydantic models.

## Rate Limits

The API has rate limits to ensure fair usage:

- **Shortlinks**: Maximum of 10 shortlinks created per minute per account (default)
- When you exceed the limit, you'll receive a 403 error with code `42900`
- **For inquiries or requests to increase the limit**: Please contact Technical Support directly through their support channels

Example error response:
```json
{
  "code": 42900,
  "error": "Ha excedido el límite de solicitudes. Intente nuevamente más tarde"
}
```

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

This script demonstrates how to list messages, send a message, interact with contacts, and manage shortlinks. Check the code in `example/main.py` for more details and usage patterns.

## Testing

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Run Examples

```bash
# Run all examples (including shortlinks)
python example/main.py
```

### Interactive Testing

```python
from im_csm_sdk_python import list_shortlinks, create_shortlink
from im_csm_sdk_python.schemas.shortlinks import CreateShortlinkData, ListShortlinksParams

# List shortlinks
shortlinks = list_shortlinks(ListShortlinksParams(limit=10))
print(f"Found {len(shortlinks)} shortlinks")

# Create shortlink
created = create_shortlink(
    CreateShortlinkData(
        long_url="https://www.example.com/test",
        name="Test Shortlink",
        status="ACTIVE"
    )
)
print(f"Created: {created.short_url}")
```

## Main Operations

- **Status**
  - Get API status: `im_csm_sdk_python.get_status()`
- **Contacts**
  - List contacts: `im_csm_sdk_python.list_contacts(params)`
  - Get a contact: `im_csm_sdk_python.get_contact(msisdn)`
- **Messages**
  - List messages: `im_csm_sdk_python.list_messages(params)`
  - Send message to contact: `im_csm_sdk_python.send_to_contact(data)`
  - Send message to tags: `im_csm_sdk_python.send_to_tags(data)`
- **Shortlinks**
  - List shortlinks: `im_csm_sdk_python.list_shortlinks(params)`
  - Get shortlink by ID: `im_csm_sdk_python.get_shortlink_by_id(shortlink_id)`
  - Create shortlink: `im_csm_sdk_python.create_shortlink(data)`
  - Update shortlink status: `im_csm_sdk_python.update_shortlink_status(shortlink_id, status)`

## API Response Examples

### Create Shortlink - Success
```json
{
  "success": true,
  "message": "Shortlink created successfully",
  "account_id": 12345,
  "url_id": "123ABC",
  "short_url": "https://shorturl-pais.com/123ABC",
  "long_url": "https://www.example.com/very-long-url-with-parameters"
}
```

### List Shortlinks - Success
```json
{
  "success": true,
  "message": "Shortlinks retrieved successfully",
  "data": [
    {
      "_id": "123ABC",
      "account_uid": "abcde12345678kklm",
      "name": "Enlace corto de prueba",
      "status": "INACTIVE",
      "base_url": "https://shorturl-pais.com/",
      "short_url": "https://shorturl-pais.com/123ABC",
      "long_url": "https://www.example.com/long-url-here",
      "visits": 0,
      "unique_visits": 0,
      "preview_visits": 0,
      "created_by": "SHORTLINK_API",
      "reference_type": "SHORT_LINK",
      "expiration": false,
      "expiration_date": null,
      "created_on": 1735689600000
    }
  ],
  "account_id": 12345
}
```

### Get Shortlink by ID - Success
```json
{
  "success": true,
  "message": "Shortlink found",
  "account_id": 12345,
  "url_id": "123ABC",
  "short_url": "https://shorturl-pais.com/123ABC",
  "long_url": "https://www.example.com/long-url-with-parameters",
  "name": "Example Shortlink",
  "status": "ACTIVE",
  "visits": 0,
  "unique_visits": 0,
  "preview_visits": 0,
  "created_by": "SHORTLINK_API",
  "created_on": 1735689600000
}
```

### Get Shortlink by ID - Not Found
```json
{
  "success": false,
  "message": "Shortlink not found"
}
```

## Contributing

Feel free to open issues or submit pull requests to improve the SDK. Please ensure your code follows the project's style guidelines and includes appropriate tests.
