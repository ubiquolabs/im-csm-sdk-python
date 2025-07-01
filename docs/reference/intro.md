# API Reference Introduction

This section provides comprehensive technical documentation for the IM CSM SDK Python implementation.

## Overview

The API reference is organized into the following sections:

- **[Core Functions](index.md)** - Main SDK functions for contacts, messages, and status
- **[Configuration](configuration.md)** - Configuration functions and environment variables
- **[Example](example.md)** - Documentation of the example script

## SDK Architecture

The IM CSM SDK Python is structured as follows:

### Core Modules
- `core/contacts.py` - Contact management functions
- `core/messages.py` - Message operations
- `core/status.py` - API status checking

### Configuration
- `configs/config.py` - Configuration management
- `configs/logger.py` - Logging configuration

### Data Schemas
- `schemas/contacts.py` - Contact-related data models
- `schemas/messages.py` - Message-related data models
- `schemas/request.py` - API request models

### Helpers
- `helpers/api_request.py` - HTTP request handling
- `helpers/authentication.py` - Authentication utilities

### Utilities
- `utils/sort_params.py` - Parameter sorting utilities
- `utils/timeit.py` - Timing and performance utilities

## Type Safety

The SDK uses Pydantic v2 for:
- Input validation
- Output parsing
- Type safety
- Automatic documentation generation

All functions include proper type hints and return typed objects.

## Error Handling

The SDK implements comprehensive error handling:
- Configuration validation
- HTTP error handling
- Data validation errors
- Network connectivity issues

## Logging

Built-in logging using Loguru provides:
- Structured logging
- Configurable log levels
- File rotation support
- Debug information for troubleshooting

## Usage Patterns

Common usage patterns are documented throughout the reference:
- Synchronous operations
- Error handling best practices
- Configuration management
- Data validation