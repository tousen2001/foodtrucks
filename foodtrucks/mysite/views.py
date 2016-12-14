from flask import render_template
from .models import MobileFoodFacilityPermit
from . import food_app
from . import db
from sqlalchemy import text
import simplejson


@food_app.route("/")
def index():
    for item in MobileFoodFacilityPermit.query.all():
        print item

    return render_template('index.html')


@food_app.route("/api/nearby")
def nearby():
    result = db.engine.connect().execute(text("""
        select * from mobile_food_facility_permit where locationid = :locationid
    """), locationid = 762182)

    retlist = [dict(zip(row.keys(), row)) for row in result]

    return simplejson.dumps(retlist)
