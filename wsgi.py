from src.app import create_app
import os 

env_name = os.environ.get("FLASK_ENV") or 'development'
app = create_app(env_name)

