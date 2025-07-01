# Example Reference

This page documents the main example script included with the SDK.

## Main Example Script

::: example.main
    options:
        show_root_heading: true
        show_root_members_full_path: false

## Running the Example

The example script demonstrates all major SDK functionality:

```bash
python example/main.py
```

## Example Functions

The example script includes the following demonstration functions:

### Contact Examples
- `example_contacts()` - Shows how to list and get contacts

### Message Examples  
- `example_messages()` - Shows how to list and send messages

### Status Examples
- `example_status()` - Shows how to check API status

## What the Example Demonstrates

1. **Configuration**: How to set up and validate SDK configuration
2. **Contact Management**: Listing contacts with filters and getting specific contacts
3. **Message Operations**: Listing messages with date ranges and sending messages
4. **Error Handling**: Proper exception handling patterns
5. **Logging**: Using the SDK's built-in logging functionality

## Customizing the Example

You can modify the example script to:

- Test with your own phone numbers
- Try different search queries
- Experiment with different date ranges
- Test error scenarios

The example script is located at `example/main.py` in the SDK repository.