from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    #블루프린트
    from .views import main_views, user_views, movedata_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(user_views.bp)
    app.register_blueprint(movedata_views.bp)

    return app