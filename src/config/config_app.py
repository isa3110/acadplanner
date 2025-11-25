from model import *
from flask import Flask
from flask_login import LoginManager

def config(app: Flask) -> None:
    app.secret_key = 'LASJDHJDWUABBDAWDB@##'

    login_manager: LoginManager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id) -> User | None:
        return session.get(User, int(user_id))


def start_database(app) -> None:
    with app.app_context():
        Base.metadata.create_all(ENGINE)
    app.run(debug=True)