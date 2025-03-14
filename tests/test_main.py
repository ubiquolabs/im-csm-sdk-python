
"""Tests for the simple Python application."""
import pytest
from unittest.mock import patch
import io
import sys
from im_csm_sdk_python import main


def test_main_function(capsys):
    """Test that the main function prints the expected output."""
    main.main()
    captured = capsys.readouterr()
    
    assert "Hello, World!" in captured.out
    assert "Welcome to im-csm-sdk-python!" in captured.out
 