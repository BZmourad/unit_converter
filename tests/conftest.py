import pytest
from flask import Flask

app = Flask(__name__)
app.secret_key = "SECRET_KEY"


@pytest.fixture(scope="function")
def app_context():
    """Provides a Flask app context for tests that use flash messages."""
    with app.app_context():
        with app.test_request_context("/"):
            yield
