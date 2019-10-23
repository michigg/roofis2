import os
from urllib.parse import urlencode, quote_plus

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

ROOFIS_API = os.environ.get("ROOFIS_API")


@app.route('/', methods=['GET', 'POST'])
def index():
    locations = requests.get(f'{ROOFIS_API}locations/').json()
    if request.method == 'POST':
        form = request.form
        start_date = form.get("start_date", None)
        start_time = form.get("start_time", None)
        location = form.get("location", None)
        min_size = form.get("min_size", None)
        if start_time and start_date:
            url = get_roofis_api_url(location, min_size, start_date, start_time)
            print(url)
            response = requests.get(url)
            if response.status_code == 200:
                print(response.json())
                empty_results = True if not response.json() else False
                return render_template("index.jinja2", free_rooms=response.json(), locations=locations, form=form,
                                       empty_results=empty_results)
            return render_template("index.jinja2",
                                   error="Zurzeit ist der RooFiS Endpunkt nicht erreichbar. Versuchen Sie es später nochmal, oder kontaktieren Sie den Administrator. ",
                                   locations=locations, form=form)
        else:
            return render_template("index.jinja2",
                                   error="Sie müssen mindestens ein Startdatum und eine Startzeit angeben",
                                   locations=locations, form=form)
    else:
        return render_template("index.jinja2", locations=locations, form={})


def get_roofis_api_url(location, min_size, start_date, start_time):
    params = {}
    params['start_date'] = start_date
    params['start_time'] = start_time
    if location:
        params['location'] = location
    if min_size:
        params['min_size'] = min_size
    url = f'{ROOFIS_API}?{urlencode(params, quote_via=quote_plus)}'
    return url


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8888')
