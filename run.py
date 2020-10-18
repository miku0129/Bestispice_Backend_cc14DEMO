# heroku logs --tail -a cc14polyglottal-app

# /run.py
import os
import settings

from src.app import create_app


if __name__ == '__main__':
    env_name = os.environ.get('FLASK_ENV') or 'development'

    app = create_app(env_name)
    app.run(debug=True)
