import os
import tempfile
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

@pytest.fixture
def runner():
    return app.test_cli_runner()
