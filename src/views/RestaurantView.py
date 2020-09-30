from flask import request, json, Response, Blueprint
from ..models.RestaurantsModel import RestaurantsModel

restaurant_api = Blueprint('restaurants', __name__)


@restaurant_api.route('/', methods=['GET'])
def test():
    return custom_response({'message': 'Test!'}, 201)


@restaurant_api.route('/', methods=['POST'])
def create_info():

    req_data = request.get_json()
    # print('data', req_data)

    restaurant = RestaurantsModel(req_data)
    restaurant.save()

    return custom_response({'message': 'Add new restaurant!'}, 201)


def custom_response(res, status_code):

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
