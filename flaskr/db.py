"""Sets up SQLAlchemy ORM with App"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import click
from flask.cli import with_appcontext

Base = declarative_base()


def init_engine(database, **kwargs):
    global engine
    engine = create_engine(database)


def init_session():
    global Session
    Session = scoped_session(sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=engine))
    print("created", Session)


def get_session():
    session = Session()
    return session


def end_session(error=None):
    Session.remove()
    if error:
        # Log the error
        print(str(error))


def init_db():
    Base.metadata.create_all(bind=engine)


def clear_db():
    Base.metadata.drop_all(bind=engine)


@click.command('reset-db')
@with_appcontext
def reset_db_command():
    """Clear the existing data and create new tables."""
    clear_db()
    init_db()
    click.echo('Reset the database.')


def init_app(app):
    app.teardown_appcontext(end_session)
    app.cli.add_command(reset_db_command)

def init_app(app):
    app.teardown_appcontext(end_session)
    app.cli.add_command(reset_db_command)
