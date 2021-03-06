from flask_restful import Resource, abort
from .models import MobileFoodFacilityPermit
from flask import jsonify


class FoodTrucks(Resource):
    @staticmethod
    def get(locationid):
        retobj = MobileFoodFacilityPermit.query.filter(MobileFoodFacilityPermit.locationid == locationid).first()
        if retobj:
            return jsonify(retobj.as_dict())
        else:
            return abort(404, message="Location {0} doesn't exist.".format(locationid))
