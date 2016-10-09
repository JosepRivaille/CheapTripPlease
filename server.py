from flask import Flask, request
import json
from flask_cors import CORS

from ArrangementHandling import ArrangementHandling

app = Flask(__name__)
CORS(app)


# From server to web
@app.route('/getData')
def get_calculated_data():
    return False


# From web to server
@app.route("/sendData", methods=['POST'])
def post_sent_data():
    # Origin
    origin_city = request.form.get('originCity')
    start_day = request.form.get('startDate')
    # Destination
    destination_city = request.form.get('destinationCity')
    end_day = request.form.get('endDate')
    # Cities to visit
    number_cities = request.form.get('numberCities', type=int)
    list_cities = [origin_city]
    for x in range(number_cities):
        list_cities.append(request.form.get('city_' + x))
    list_cities.append(destination_city)
    list_cities.append(start_day)
    list_cities.append(end_day)
    # ArrangementHandling m(list_cities)


if __name__ == '__main__':
    app.run()
