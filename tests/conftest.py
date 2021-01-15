"""Creates instance of app that will *normally* be used for testing"""

import pytest
from flaskr import create_app

@pytest.fixture
def app():

    app = create_app({
        'TESTING': True,
        'DATABASE': "sqlite:///:memory:",
    })

    yield app