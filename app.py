
# src/app.py

from flask import Flask
from flask_cors import CORS

from .src.config import app_config
from .src.models import db
# from .config import app_config
# from .models import db


# try stop using router
from .src.views.RestaurantView import restaurant_api as restaurant_blueprint
# from .views.RestaurantView import restaurant_api as restaurant_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    CORS(app)

    app.config.from_object(app_config[env_name])

    db.init_app(app)

    app.register_blueprint(restaurant_blueprint,
                           url_prefix='/api/v1/restaurants')

    @app.route('/', methods=['GET'])
    def index():
        """
        example endpoint
        """
        return 'Congratulations! Your first endpoint is workin'

    return app
