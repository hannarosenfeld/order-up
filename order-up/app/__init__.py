from flask import Flask
from .config import Configuration
from .models import db   # New import
from .routes import orders
from .routes import session
from flask_login import LoginManager, current_user 
from .models import db, Employee

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(orders.bp)
app.register_blueprint(session.bp)

db.init_app(app)  # Configure the application with SQLAlchemy

login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
