from flask import render_template, request
from .models import MobileFoodFacilityPermit
from . import food_app
from . import db
from sqlalchemy import text
from flask import jsonify


@food_app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', id_menu=1)
    else:
        icount = 0

        lstlength = []
        for x in request.form.values():
            if x not in lstlength:
                lstlength.append(x)
            else:
                icount += 1

        message=''

        if icount == 0:
            message = "<h1 class='alert-info'>This triangle is a scalene.</h1>"
        elif icount == 1:
            message = "<h1 class='alert-info'>This triangle is a isosceles.</h1>"
        elif icount == 2:
            message = "<h1 class='alert-info'>This triangle is a equilateral.</h1>"

        lstlength = request.form.values()
        icount = sum(lstlength.count(x) for x in lstlength)

        if icount == 3:
            message = "<h1 class='alert-info'>This triangle is a scalene.</h1>"
        elif icount == 5:
            message = "<h1 class='alert-info'>This triangle is a isosceles.</h1>"
        elif icount == 9:
            message = "<h1 class='alert-info'>This triangle is a equilateral.</h1>"

        solution1 = """solution 01<pre><code>for x in request.form.values():
    if x not in lstlength:
        lstlength.append(x)
    else:
        icount += 1</code></pre>"""

        solution2 = """solution 02<pre><code>icount = sum(lstlength.count(x) for x in lstlength)</code></pre>"""

        return render_template('index.html', id_menu=1, message=message, solution1=solution1, solution2=solution2)


@food_app.route("/map")
def map():
    return render_template('foodtrucks.html', id_menu=2)


@food_app.route("/api/test")
def test():
    result = db.engine.connect().execute(text("""
        select * from mobile_food_facility_permit where locationid = :locationid
    """), locationid = 762182)

    retlist = [dict(zip(row.keys(), row)) for row in result]

    return jsonify(retlist)


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

    return jsonify(retlist)
