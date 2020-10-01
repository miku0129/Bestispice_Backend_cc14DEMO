# /run.py
import os

from src.app import create_app

if __name__ == '__main__':
    env_name = os.getenv('FLASK_ENV')
    app = create_app(env_name)
    # run app
    # app.run()
    app.run(debug=False, host='0.0.0.0',
            port=int(os.environ.get('PORT', 5000)))
