from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)

    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint, url_prefix='/')

    from app.formula import formula as formula_blueprint
    app.register_blueprint(formula_blueprint, url_prefix='/formula')

    from app.collection import collection as collection_blueprint
    app.register_blueprint(collection_blueprint, url_prefix='/collection')

    from app.table import table as table_blueprint
    app.register_blueprint(table_blueprint, url_prefix='/tables')

    return app