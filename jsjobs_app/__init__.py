from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os


# Initiating app from Flask and configuring it with Config of file config.py
app = Flask('js_jobs', template_folder='templates/', static_folder='static/')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

"""# Setting up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))"""

from jsjobs_app import views, models
