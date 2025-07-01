# Examples

This section provides practical examples of using the IM CSM SDK Python in different scenarios.

## Basic Examples

### Quick Start Example

The simplest way to get started with the SDK:

```python
import im_csm_sdk_python as im_sdk
from im_csm_sdk_python.schemas.contacts import ListContactsParams

# List contacts with basic parameters
contacts = im_sdk.list_contacts(
    ListContactsParams(limit=5)
)

for contact in contacts:
    print(f"Contact: {contact.full_name} ({contact.msisdn})")
```

### Complete Example Script

Run the complete example from the repository:

```bash
python example/main.py
```

This script demonstrates:
- Listing contacts with filters
- Getting specific contact information
- Listing messages with date ranges
- Sending messages to contacts
- Checking API status

## Contact Management Examples

### List All Active Contacts

```python
from im_csm_sdk_python.schemas.contacts import ListContactsParams, ContactStatus

# Get only active contacts
contacts = im_sdk.list_contacts(
    ListContactsParams(
        status=[ContactStatus.ACTIVE],
        limit=50
    )
)

print(f"Found {len(contacts)} active contacts")
```

### Search Contacts by Name

```python
# Search for contacts containing "John"
contacts = im_sdk.list_contacts(
    ListContactsParams(
        query="John",
        limit=10
    )
)

for contact in contacts:
    print(f"Found: {contact.full_name} - {contact.msisdn}")
```

### Get Contact Details

```python
try:
    contact = im_sdk.get_contact("1234567890")
    print(f"Contact Details:")
    print(f"  Name: {contact.full_name}")
    print(f"  Phone: {contact.msisdn}")
    print(f"  Email: {contact.email}")
    print(f"  Status: {contact.status}")
    print(f"  Tags: {', '.join(contact.tags)}")
except Exception as e:
    print(f"Contact not found: {e}")
```

## Message Operations Examples

### List Recent Messages

```python
from datetime import datetime, timedelta
from im_csm_sdk_python.schemas.messages import ListMessagesParams, MessageDirection

# Get messages from the last 7 days
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

messages = im_sdk.list_messages(
    ListMessagesParams(
        start_date=start_date,
        end_date=end_date,
        limit=100
    )
)

print(f"Found {len(messages)} messages in the last 7 days")
```

### Filter Messages by Direction

```python
# Get only outbound messages
outbound_messages = im_sdk.list_messages(
    ListMessagesParams(
        direction=MessageDirection.MT,  # Mobile Terminated (outbound)
        limit=50
    )
)

# Get only inbound messages
inbound_messages = im_sdk.list_messages(
    ListMessagesParams(
        direction=MessageDirection.MO,  # Mobile Originated (inbound)
        limit=50
    )
)
```

### Send Message to Contact

```python
from uuid import uuid4
from im_csm_sdk_python.schemas.messages import SendToContactData

# Send a message
try:
    sent_message = im_sdk.send_to_contact(
        SendToContactData(
            msisdn="1234567890",
            message="Hello! This is a test message from the Python SDK.",
            id=str(uuid4())  # Unique message ID
        )
    )
    
    print(f"Message sent successfully!")
    print(f"Message ID: {sent_message.message_id}")
    print(f"Status: {sent_message.status}")
    
except Exception as e:
    print(f"Failed to send message: {e}")
```

## Advanced Examples

### Bulk Operations

```python
from uuid import uuid4

# Send messages to multiple contacts
contacts_to_message = ["1234567890", "0987654321", "1122334455"]
message_text = "Bulk message from Python SDK"

for msisdn in contacts_to_message:
    try:
        result = im_sdk.send_to_contact(
            SendToContactData(
                msisdn=msisdn,
                message=message_text,
                id=str(uuid4())
            )
        )
        print(f"Sent to {msisdn}: {result.message_id}")
    except Exception as e:
        print(f"Failed to send to {msisdn}: {e}")
```

### Pagination Example

```python
def get_all_contacts():
    """Get all contacts using pagination."""
    all_contacts = []
    start = 0
    limit = 50
    
    while True:
        contacts = im_sdk.list_contacts(
            ListContactsParams(
                start=start,
                limit=limit
            )
        )
        
        if not contacts:
            break
            
        all_contacts.extend(contacts)
        start += limit
        
        print(f"Retrieved {len(all_contacts)} contacts so far...")
    
    return all_contacts

# Usage
all_contacts = get_all_contacts()
print(f"Total contacts: {len(all_contacts)}")
```

### Error Handling Example

```python
from im_csm_sdk_python import logger

def safe_send_message(msisdn: str, message: str):
    """Send message with comprehensive error handling."""
    try:
        result = im_sdk.send_to_contact(
            SendToContactData(
                msisdn=msisdn,
                message=message,
                id=str(uuid4())
            )
        )
        logger.info(f"Message sent successfully to {msisdn}")
        return result
        
    except ValueError as e:
        logger.error(f"Invalid parameters: {e}")
        return None
        
    except ConnectionError as e:
        logger.error(f"Network error: {e}")
        return None
        
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None

# Usage
result = safe_send_message("1234567890", "Test message")
if result:
    print(f"Success: {result.message_id}")
else:
    print("Failed to send message")
```

### Configuration Validation Example

```python
from im_csm_sdk_python import get_config, logger

def validate_sdk_setup():
    """Validate SDK configuration before use."""
    try:
        # Test configuration
        config = get_config()
        logger.info("Configuration is valid")
        
        # Test API connectivity
        status = im_sdk.get_status()
        logger.info(f"API Status: {status}")
        
        # Test basic functionality
        contacts = im_sdk.list_contacts(
            ListContactsParams(limit=1)
        )
        logger.info(f"API connectivity test passed")
        
        return True
        
    except Exception as e:
        logger.error(f"SDK setup validation failed: {e}")
        return False

# Run validation before main application logic
if validate_sdk_setup():
    print("SDK is ready to use!")
else:
    print("Please check your configuration")
```

## Integration Examples

### FastAPI Web Application

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import im_csm_sdk_python as im_sdk
from im_csm_sdk_python.schemas.contacts import ListContactsParams
from im_csm_sdk_python.schemas.messages import SendToContactData
from uuid import uuid4

app = FastAPI(title="IM CSM SDK API", version="1.0.0")

# Request/Response models
class SendMessageRequest(BaseModel):
    msisdn: str
    message: str

class SendMessageResponse(BaseModel):
    success: bool
    message_id: Optional[str] = None
    status: Optional[str] = None
    error: Optional[str] = None

class ContactResponse(BaseModel):
    msisdn: Optional[str]
    name: Optional[str]
    status: str

class ContactsListResponse(BaseModel):
    success: bool
    contacts: List[ContactResponse]
    total: int

@app.post("/send-message", response_model=SendMessageResponse)
async def send_message(request: SendMessageRequest):
    """Send a message to a contact."""
    try:
        result = im_sdk.send_to_contact(
            SendToContactData(
                msisdn=request.msisdn,
                message=request.message,
                id=str(uuid4())
            )
        )
        
        return SendMessageResponse(
            success=True,
            message_id=result.message_id,
            status=result.status
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to send message: {str(e)}"
        )

@app.get("/contacts", response_model=ContactsListResponse)
async def list_contacts(limit: int = 50, query: Optional[str] = None):
    """List contacts with optional filtering."""
    try:
        contacts = im_sdk.list_contacts(
            ListContactsParams(limit=limit, query=query)
        )
        
        contact_list = [
            ContactResponse(
                msisdn=c.msisdn,
                name=c.full_name,
                status=c.status
            )
            for c in contacts
        ]
        
        return ContactsListResponse(
            success=True,
            contacts=contact_list,
            total=len(contact_list)
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to list contacts: {str(e)}"
        )

@app.get("/contacts/{msisdn}")
async def get_contact(msisdn: str):
    """Get a specific contact by MSISDN."""
    try:
        contact = im_sdk.get_contact(msisdn)
        
        return {
            "success": True,
            "contact": {
                "msisdn": contact.msisdn,
                "name": contact.full_name,
                "email": contact.email,
                "status": contact.status,
                "tags": contact.tags
            }
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=f"Contact not found: {str(e)}"
        )

@app.get("/status")
async def get_api_status():
    """Check API status."""
    try:
        status = im_sdk.get_status()
        return {"success": True, "status": status}
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"API status check failed: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

**Running the FastAPI application:**

```bash
# Install FastAPI and uvicorn
pip install fastapi uvicorn

# Run the application
python your_app.py

# Or use uvicorn directly
uvicorn your_app:app --reload
```

**API Documentation:**
- Interactive docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Async Usage (Future Enhancement)

```python
# Note: Current SDK is synchronous, but here's how async might work
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def send_messages_async(message_data_list):
    """Send multiple messages concurrently."""
    loop = asyncio.get_event_loop()
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [
            loop.run_in_executor(
                executor,
                im_sdk.send_to_contact,
                data
            )
            for data in message_data_list
        ]
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

# Usage
# results = asyncio.run(send_messages_async(message_data_list))
```

## Next Steps

- Check the [API Reference](../reference/index.md) for complete function documentation
- Review [Configuration](../configuration.md) for setup details
- See [Troubleshooting](../troubleshooting.md) for common issues 