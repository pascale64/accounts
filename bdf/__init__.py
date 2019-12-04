import os
from flask import Flask, request, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from datetime import timedelta


db = SQLAlchemy()
migrate = Migrate()



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=60)

    db.init_app(app)
    migrate.init_app(app, db)
    
    from bdf.aux import bp as aux_bp
    app.register_blueprint(aux_bp)
    
    from bdf.books import bp as books_bp
    app.register_blueprint(books_bp)


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
