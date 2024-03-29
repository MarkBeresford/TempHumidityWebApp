from flask import Flask, render_template, request
from aws_controller import get_esp8266_items_dynamo
from model.sensor_reading import map_to_sensor_readings
from flask_cors import CORS
from datetime import datetime

application = Flask(__name__)
application.config.from_prefixed_env()
CORS(application)


@application.route('/')
def index():
    return render_template('landing_page.html')


@application.route('/view-temp-and-humidity-data', methods=['POST', 'GET'])
def view_temp_and_humidity_data():
    if request.method == 'POST':
        dates = request.get_json()
        window_to_look_over = [
            int(datetime.strptime(dates[0], "%d/%m/%Y").strftime("%Y%m%d000000")),
            int(datetime.strptime(dates[1], "%d/%m/%Y").strftime("%Y%m%d235959"))
        ]
        esp8266_data = get_esp8266_items_dynamo(
            table_name=application.config["DYNAMO_TABLE_NAME"],
            region=application.config["DYNAMO_REGION"],
            window=window_to_look_over
        )
        sensor_data = map_to_sensor_readings(esp8266_data)
        return sensor_data
    else:
        return render_template('temp_sensor.html')


if __name__ == '__main__':
    application.run()
