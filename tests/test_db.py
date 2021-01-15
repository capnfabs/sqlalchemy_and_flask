"""The interesting part - I am not passing the conftest app
fixture to these test functions, but yet when I run it there is a Session() object
(which the create_app function should be making but I never passed the app to the test?
Things are also being added to a database (don't know which one since no app was passed
to the test....the database is also persisting between tests because I will get an integrity
error from the second test because all username values should be unique and the username from the
first test's database insertion is still there."""

import pytest
from flaskr.db import get_session
from flaskr.models import User

def test_working_outside_of_app_context(app):
    #with app.app_context():
    session = get_session()
    new_user = User(username="kelly", password="kelly")
    session.add(new_user)
    session.commit()
    assert len(session.query(User).filter(User.username=="kelly").all()) == 1

def test_again(app):
    test_working_outside_of_app_context(app)

def test_database_insertion_and_persistence_outside_of_app_context(app):
    #with app.app_context():
    session = get_session()
    new_user = User(username="kelly", password="kelly")
    session.add(new_user)
    session.commit()
