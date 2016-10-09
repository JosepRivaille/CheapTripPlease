from flask import Flask, request, jsonify
from flask_cors import CORS
import ArrangementHandling as ah
import SkyScannerIO as ssIO

app = Flask(__name__)
CORS(app)


# From server to web
@app.route('/getData')
def get_calculated_data():
    data_list = []
    data_maps = {
        'name': "Barcelona",
        'lat': 41.3851,
        'lng': 2.1734
    }
    data_list.append(data_maps)
    data_maps = {
        'name': "Valencia",
        'lat': 39.4699,
        'lng': 0.3763
    }
    data_list.append(data_maps)
    return jsonify(data_list)


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
    if number_cities is not None:
        list_cities = [origin_city]
        for x in range(number_cities):
            list_cities.append(request.form.get('city_' + 'asd'))
        list_cities.append(destination_city)
        list_cities.append(start_day)
        list_cities.append(end_day)
    # ArrangementHandling m(list_cities)
    return


# Autocomplete route
@app.route("/autocomplete/<query>")
def autocomplete_query(query=""):
    return ssIO.auto_suggest_location(query)

if __name__ == '__main__':
    app.run()
