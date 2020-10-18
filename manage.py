import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app, db
# from .app import create_app, db

# import environment from settings.py
import settings
# assign it to env_name
# env_name = settings.flaskenv
env_name = os.environ.get("FLASK_ENV") or 'deveropment' 

# env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
