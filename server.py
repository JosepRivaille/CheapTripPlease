from flask import Flask, request
import json
from flask_cors import CORS
import ArrangementHandling as ah

app = Flask(__name__)
CORS(app)


# From server to web
@app.route('/getData')
def get_calculated_data():
    return False


# From web to server
@app.route("/sendData", methods=['POST'])
def post_sent_data():
    bundle_days_orig_dest_citieslist = []
    # Origin
    origin_city = request.form.get('originCity')
    start_day = request.form.get('startDate')
    # Destination
    destination_city = request.form.get('destinationCity')
    end_day = request.form.get('endDate')
    # Cities to visit
    number_cities = request.form.get('numberCities', type=int)
    # Build bundle
    bundle_days_orig_dest_citieslist.append(start_day)
    bundle_days_orig_dest_citieslist.append(end_day)
    bundle_days_orig_dest_citieslist.append(origin_city)
    bundle_days_orig_dest_citieslist.append(destination_city)
    for x in range(number_cities):
        bundle_days_orig_dest_citieslist.append(request.form.get('city_' + x))
    backend = ah.ArrangementHandler(bundle_days_orig_dest_citieslist)


if __name__ == '__main__':
    app.run()
