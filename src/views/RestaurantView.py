from flask import request, json, Response, Blueprint, jsonify, g
from ..models.RestaurantsModel import RestaurantsModel

# try stop using router
restaurant_api = Blueprint('restaurants', __name__)


# @restaurant_api.route('/', methods=['GET'])
# def test():
#     return custom_response({'message': 'Test!'}, 201)

@restaurant_api.route('/', methods=['POST'])
# post new information about a restaurant
def create_info():

    req_data = request.get_json()
    # print('data', req_data)

    restaurant = RestaurantsModel(req_data)
    restaurant.save()
    print(restaurant.name)

    return custom_response({'message': 'Add new restaurant!'}, 201)


@restaurant_api.route('/<int:restaurant_id>', methods=['DELETE'])
# delete a restaurant which find by id
def delete(restaurant_id):
    restaurant = RestaurantsModel.get_one_restaurant(restaurant_id)
    restaurant.delete()

    return custom_response({'message': 'Deleted'}, 201)


@restaurant_api.route('/<int:restaurant_id>', methods=['GET'])
# get single information about a restaurant by id
def get_an_info(restaurant_id):
    ret = RestaurantsModel.get_one_restaurant(restaurant_id)
    print('ret', ret.name)
    # return custom_response({'message': 'done!'}, 201)
    return jsonify(name=ret.name, feature=ret.feature, place=ret.place, tell=ret.tell, business_hours1=ret.business_hours1, business_hours2=ret.business_hours2, regular_holiday=ret.regular_holiday, url=ret.url)


@restaurant_api.route('/', methods=['GET'])
# get all information of restaurants
def get_all_info():
    ret = RestaurantsModel.get_all_restaurants()
    print('ret', ret[0])
    print('type?', type(ret))
    print(len(ret))

    # return jsonify(name=ret[0].name)
    # for item in ret:
    #     jsonify(name=item.name)
    # ret_dct = {i: ret[i].name for i in range(0, len(ret), 1)}

    # ret_dct = {i: [ret[i].name, ret[i].feature]for i in range(0, len(ret), 1)}
    ret_dct = {ret[i].name: [ret[i].id, ret[i].feature,
                             ret[i].place, ret[i].url]for i in range(0, len(ret), 1)}

    return custom_response(ret_dct, 201)


@restaurant_api.route('/<int:restaurant_id>', methods=['PUT'])
# update information of single restaurants which be found by id
def update(restaurant_id):
    req_data = request.get_json()
    data = req_data
    ret = RestaurantsModel.get_one_restaurant(restaurant_id)
    ret.update(data)
    return jsonify(name=ret.name, feature=ret.feature, place=ret.place, tell=ret.tell, business_hours1=ret.business_hours1, business_hours2=ret.business_hours2, regular_holiday=ret.regular_holiday, url=ret.url)


def custom_response(res, status_code):

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
