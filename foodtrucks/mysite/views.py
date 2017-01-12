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
        icount1 = 0
        icount2 = 0

        icount1 = len(set(request.form.values()))

        message = {3: "<h1 class='alert-info'>This triangle is a scalene.</h1>",
                   2: "<h1 class='alert-info'>This triangle is a isosceles.</h1>",
                   1: "<h1 class='alert-info'>This triangle is a equilateral.</h1>",
                   5: "<h1 class='alert-info'>This triangle is a isosceles.</h1>",
                   9: "<h1 class='alert-info'>This triangle is a equilateral.</h1>"}

        lstlength = request.form.values()
        icount2 = sum(lstlength.count(x) for x in lstlength)

        solution1 = """solution 01
<pre><code>
icount = len(set(request.form.values())
</code></pre>"""

        solution2 = """solution 02<pre><code>icount = sum(lstlength.count(x) for x in lstlength)</code></pre>"""

        return render_template('index.html', id_menu=1, message1=message[icount1], message2=message[icount2],
                               solution1=solution1, solution2=solution2)


@food_app.route("/map")
def show_map():
    return render_template('foodtrucks.html', id_menu=2)


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
