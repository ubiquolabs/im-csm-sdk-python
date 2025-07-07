# Configuration

Complete guide for configuring the IM CSM SDK Python.

## Environment Variables

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `API_KEY` | API authentication key | `your_api_key_here` |
| `API_SECRET` | API authentication secret | `your_secret_here` |
| `URL` | Base URL for the IM CSM API | `https://api.example.com` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `LOG_PATH` | Path for log files | `logs/im-csm-sdk-python.log` |
| `LOG_LEVEL` | Logging level | `DEBUG` |

## Setup Methods

### Option 1: .env File (Recommended)

Create a `.env` file in your project root:

```env
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
URL=https://api.example.com
LOG_LEVEL=INFO
```

### Option 2: Environment Variables

```bash
export API_KEY="your_api_key_here"
export API_SECRET="your_api_secret_here"
export URL="https://api.example.com"
```

The SDK automatically loads `.env` files using `python-dotenv`.

## Configuration Functions

### get_config()

The SDK provides a `get_config()` function that validates and returns configuration:

```python
from im_csm_sdk_python import get_config

try:
    config = get_config()
    print(f"API URL: {config['url']}")
except ValueError as e:
    print(f"Configuration error: {e}")
```

This function will raise a `ValueError` if any required environment variables are missing.

## Logger Configuration

The SDK uses [Loguru](https://loguru.readthedocs.io/) with these default settings:

- **Level**: `DEBUG` (set via `LOG_LEVEL`)
- **File**: `logs/im-csm-sdk-python.log` (set via `LOG_PATH`)
- **Rotation**: Daily at midnight
- **Retention**: 1 month
- **Compression**: gzip

### Log Levels

| Level | Description |
|-------|-------------|
| `DEBUG` | Detailed diagnostic information |
| `INFO` | General information messages |
| `WARNING` | Warning messages |
| `ERROR` | Error messages |
| `CRITICAL` | Critical system failures |

### Using the Logger

```python
from im_csm_sdk_python import logger

logger.info("Operation completed successfully")
logger.error("An error occurred", error=str(e))
```

### Custom Logger Setup

```python
from im_csm_sdk_python import logger
import sys

# Console logging only
logger.remove()
logger.add(sys.stdout, level="INFO")

# Custom file logging
logger.add("custom.log", rotation="10 MB", retention="1 week")
```

## Validation

### Basic Validation

```python
from im_csm_sdk_python import get_config, get_status, logger

def validate_setup():
    try:
        # Check configuration
        config = get_config()
        logger.info("✅ Configuration valid")
        
        # Check API connectivity
        status = get_status()
        logger.info("✅ API connection successful")
        return True
    except Exception as e:
        logger.error(f"❌ Setup failed: {e}")
        return False
```

## Common Errors

### Missing Environment Variables
```
ValueError: Missing required environment variables: API_KEY, API_SECRET
```
**Solution:** Set all required environment variables or create a `.env` file.

### Invalid API Credentials
```
HTTP 401: Unauthorized
```
**Solution:** Verify your API key and secret are correct.

### Permission Errors
```
PermissionError: Permission denied: 'logs/im-csm-sdk-python.log'
```
**Solution:** Create logs directory or use different path:
```bash
mkdir -p logs
# or
export LOG_PATH="/tmp/sdk.log"
```

### Network Connection Issues
```
ConnectionError: Failed to establish connection
```
**Solution:** Check your network connection and API URL.

## Best Practices

1. **Use .env files** for local development
2. **Use environment variables** in production
3. **Set LOG_LEVEL=INFO** in production
4. **Never commit credentials** to version control
5. **Validate configuration** at application startup
