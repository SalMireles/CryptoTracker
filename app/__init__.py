import os
import config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Construct core Flask application with embedded Dash app.
app = Flask(__name__, instance_relative_config=False)
Bootstrap(app)
CONFIG = config.ProdConfig if os.environ.get("APP_SETTING") else config.DevConfig
app.config.from_object(CONFIG)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# handle login
login = LoginManager(app)
login.login_view = "login"


with app.app_context():
    # Import parts of our core Flask app
    # Define in this context to avoid circular imports
    from app import routes, errors, models, db, login  # noqa

    # Import Dash application
    from .plotly_dash.dashboard import init_dashboard

    app = init_dashboard(app)

    db.create_all()
