# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db
from app.views import *
from app.models import *
from app.forms import *

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
