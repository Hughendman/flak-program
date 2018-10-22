# coding=utf-8
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

from config import config
from flask_cors import CORS

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__,
                static_folder = "./dist/static",
                template_folder = "./dist")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app,supports_credentials=True)

    db.init_app(app)
    db.app = app

    @app.route('/')
    def index():
        return render_template("index.html")

    # 注册蓝本
    # 增加auth蓝本
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # 增加404蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/authss')

    #  sqlacodegen mysql://root:abcd234@localhost:3306/superset_board?charset=utf8mb4 > models.py


    return app