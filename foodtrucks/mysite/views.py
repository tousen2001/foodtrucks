from flask import render_template, request
from .models import MobileFoodFacilityPermit
from . import food_app
from . import db
from sqlalchemy import text
import simplejson


@food_app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', id_menu=1)
    else:
        lstlength = request.form.values()
        icount = sum(lstlength.count(x) for x in lstlength)
        message=''

        if icount == 3:
            message = "<div class='alert-info'>This triangle is a scalene.</div>"
        elif icount == 5:
            message = "<div class='alert-info'>This triangle is a isosceles.</div>"
        elif icount == 9:
            message = "<div class='alert-info'>This triangle is a equilateral.</div>"

        return render_template('index.html', id_menu=1, message=message)


@food_app.route("/map")
def map():
    return render_template('foodtrucks.html', id_menu=2)


@food_app.route("/api/test")
def test():
    result = db.engine.connect().execute(text("""
        select * from mobile_food_facility_permit where locationid = :locationid
    """), locationid = 762182)

    retlist = [dict(zip(row.keys(), row)) for row in result]

    return simplejson.dumps(retlist)


@food_app.route("/api/nearby", methods=['POST'])
def nearby():
    dict_data = dict(request.form)

    result = db.engine.connect().execute(text("""
        SELECT
            locationid,
            location,
            latitude,
            longitude,
            ST_DISTANCE(POINT(:lat, :lng),
                    POINT(latitude, longitude)) * 111195 AS ptdistance
        FROM
            mobile_food_facility_permit
        ORDER BY ptdistance
        LIMIT 10;
    """), lat=dict_data['lat'][0], lng=dict_data['lng'][0])

    retlist = [dict(zip(row.keys(), row)) for row in result]

    return simplejson.dumps(retlist)
