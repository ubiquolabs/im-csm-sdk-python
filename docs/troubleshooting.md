# Troubleshooting

This guide helps you resolve common issues when using the IM CSM SDK Python.

## Common Issues

### Configuration Issues

#### Missing Environment Variables

**Error:**
```
ValueError: Missing required environment variables: API_KEY, API_SECRET
```

**Solution:**
1. Check if your environment variables are set:
   ```bash
   echo $API_KEY
   echo $API_SECRET
   echo $URL
   ```

2. If using a `.env` file, ensure it's in the correct location and format:
   ```env
   API_KEY=your_api_key
   API_SECRET=your_api_secret
   URL=https://api.example.com
   ```

3. Restart your application after setting environment variables.

#### Invalid Configuration Values

**Error:**
```
ValueError: Invalid URL format
```

**Solution:**
- Ensure the URL includes the protocol (http:// or https://)
- Verify the URL is accessible and correct

### Authentication Issues

#### Invalid Credentials

**Error:**
```
HTTP 401: Unauthorized
```

**Solution:**
1. Verify your API key and secret are correct
2. Check if your credentials have expired
3. Ensure you're using the correct API endpoint URL

#### Permission Denied

**Error:**
```
HTTP 403: Forbidden
```

**Solution:**
- Contact your API provider to verify your account permissions
- Check if your API key has the necessary scopes

### Network Issues

#### Connection Timeout

**Error:**
```
httpx.ConnectTimeout: Connection timeout
```

**Solution:**
1. Check your internet connection
2. Verify the API URL is accessible
3. Check if there are firewall restrictions
4. Try increasing the timeout in your HTTP client

#### DNS Resolution Error

**Error:**
```
httpx.ConnectError: Name resolution failed
```

**Solution:**
- Verify the API URL is correct
- Check DNS settings
- Try using an IP address instead of domain name

### API Response Issues

#### Invalid JSON Response

**Error:**
```
json.JSONDecodeError: Expecting value
```

**Solution:**
1. Check if the API endpoint is returning valid JSON
2. Verify you're using the correct API version
3. Enable debug logging to see the raw response

#### Validation Errors

**Error:**
```
pydantic.ValidationError: Field required
```

**Solution:**
1. Check the API documentation for required fields
2. Ensure your request data matches the expected schema
3. Verify data types are correct

### SDK Usage Issues

#### Import Errors

**Error:**
```
ModuleNotFoundError: No module named 'im_csm_sdk_python'
```

**Solution:**
1. Install the SDK:
   ```bash
   pip install -e .
   ```

2. Activate your virtual environment:
   ```bash
   source venv/bin/activate
   ```

#### Type Errors

**Error:**
```
TypeError: Expected str, got int
```

**Solution:**
- Check the function documentation for expected parameter types
- Use type hints and IDE support for better type checking
- Ensure data conversion before passing to SDK functions

## Debugging Tips

### Enable Debug Logging

```python
from im_csm_sdk_python import logger
import sys

# Remove default handler and add debug handler
logger.remove()
logger.add(sys.stdout, level="DEBUG")
```

### Check API Response

```python
from im_csm_sdk_python.helpers.api_request import send_request
from im_csm_sdk_python.schemas.request import ApiRequest, ApiRequestType

# Make a raw API request to debug
try:
    response = send_request(
        ApiRequest(
            type=ApiRequestType.GET,
            endpoint='status',
        )
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
```

### Validate Configuration

```python
from im_csm_sdk_python import get_config

try:
    config = get_config()
    print("Configuration is valid:")
    print(f"URL: {config['url']}")
    print(f"API Key: {config['apiKey'][:10]}...")  # Show only first 10 chars
except ValueError as e:
    print(f"Configuration error: {e}")
```

## Performance Issues

### Slow API Responses

**Symptoms:**
- Long wait times for API calls
- Timeout errors

**Solutions:**
1. Check your network connection speed
2. Verify API endpoint performance
3. Implement request caching for repeated calls
4. Use pagination for large datasets

### Memory Usage

**Symptoms:**
- High memory consumption
- Out of memory errors

**Solutions:**
1. Use pagination when listing large datasets
2. Process data in chunks rather than loading everything at once
3. Clear unused variables and objects

## Getting Help

If you continue to experience issues:

1. **Check the logs** - Enable debug logging to get more information
2. **Review the documentation** - Ensure you're following the correct usage patterns
3. **Test with minimal code** - Create a simple test to isolate the issue
4. **Check API status** - Use `im_sdk.get_status()` to verify API availability

### Reporting Issues

When reporting issues, please include:

- SDK version
- Python version
- Operating system
- Complete error message and stack trace
- Minimal code example that reproduces the issue
- Environment configuration (without sensitive data)

## FAQ

### Q: Can I use the SDK without environment variables?

A: No, the SDK requires API credentials to function. You must set the required environment variables or use a `.env` file.

### Q: Is the SDK thread-safe?

A: The SDK uses httpx for HTTP requests, which is thread-safe. However, shared state should be handled carefully in multi-threaded applications.

### Q: Can I use custom HTTP clients?

A: Currently, the SDK uses httpx internally. Custom HTTP client support may be added in future versions.

### Q: How do I handle rate limiting?

A: The SDK doesn't implement automatic rate limiting. You should implement retry logic with exponential backoff in your application if needed. 