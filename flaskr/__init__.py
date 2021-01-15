"""Flask App Factory"""

import os

from flask import Flask, render_template, request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # configuration and database location
    app.config.from_mapping(
        SECRET_KEY='dev',
        # need to change this to sqlite:///C:\\
        DATABASE=f"sqlite:////{os.path.join(app.instance_path, 'flaskr.db')}",
    )

    print('Initing app, ')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        raise Exception("Should not happen")
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initializing items needed for SQLAlchemy ORM
    from flaskr import db
    db.init_engine(app.config['DATABASE'])
    db.init_session()
    db.init_db()
    db.init_app(app)

    #from flaskr.api import create_user
    # a simple page that says hello
    @app.route('/', methods=('GET', 'POST'))
    def hello():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            create_user(username, password)
            return "Hello World"
        else:
            return render_template("register.html")

    return app
