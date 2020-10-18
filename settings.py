import os
from os.path import join, dirname

# なんでpython-dotenvでinstallしたのにdotenvで動くのだろうか？
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

databaseurl = os.environ.get("DATABASE_URL")
flaskenv = os.environ.get("FLASK_ENV")