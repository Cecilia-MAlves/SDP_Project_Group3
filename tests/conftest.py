import os
import tempfile
import pytest
from app import create_app


@pytest.fixture
def client(app):
    app = create_app()
    app.testing = True
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
