from . import db
from marshmallow import fields, Schema


class RestaurantsModel(db.Model):
    """
    Restaurants Model
    """

    # table name
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    feature = db.Column(db.String(128))
    tell = db.Column(db.String(128))
    business_hours1 = db.Column(db.String(128))
    business_hours2 = db.Column(db.String(128))
    regular_holiday = db.Column(db.String(128))
    place = db.Column(db.String(128))
    url = db.Column(db.String(128))
    comments = db.Column(db.String(128))


    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.feature = data.get('feature')
        self.tell = data.get('tell')
        self.business_hours1 = data.get('business_hours1')
        self.business_hours2 = data.get('business_hours2')
        self.regular_holiday = data.get('regular_holiday')
        self.place = data.get('place')
        self.url = data.get('url')
        self.comments = data.get('comments')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_restaurants():
        return RestaurantsModel.query.all()

    @staticmethod
    def get_one_restaurant(id):
        # print('id', id)
        # print('restaruantsmodel', RestaurantsModel)
        return RestaurantsModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)

class RestaurantsSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    feature = fields.Str(required=True)
    tell = fields.Str(required=True)
    business_hours1 = fields.Str(required=True)
    business_hours2 = fields.Str(required=True)
    regular_holiday = fields.Str(required=True)
    place = fields.Str(required=True)
    url = fields.Str(required=True)
    comments = fields.Str(required=True)
