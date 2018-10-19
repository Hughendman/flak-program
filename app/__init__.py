# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    db.app = app

    # 注册蓝本
    # 增加auth蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # 增加404蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/authss')

    #  sqlacodegen mysql://root:abcd234@localhost:3306/superset_board?charset=utf8mb4 > models.py


    return app