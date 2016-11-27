from flask import Flask, request, redirect, url_for, render_template
import requests
app = Flask(__name__)

# TODO: https://pythonhosted.org/Flask-Bootstrap/basic-usage.html
# hook it up with bootstrap, add some style
# learn about maps api, highlight bars in the map result
# get place of user, calculate distance and show the nearest bar

@app.route('/')
def main():
    return render_template('search.html')

@app.route('/', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        return redirect(url_for('map', place=request.form['place']))
    else:
        return redirect(url_for('search.html'))# change to main???

@app.route('/map')
def map(): # :param string
    place = request.args.get('place', None)
    data = api_call(place)
    return render_template('map.html', latitude=data[0], longitude=data[1])

def api_call(place): # :param string
    base_url = "http://maps.google.com/maps/api/geocode/json?address="
    query = place.replace(' ', '+')
    r = requests.get(str(base_url + query))
    j = r.json()
    latitude = j['results'][0]['geometry']['location']['lat']
    longitude = j['results'][0]['geometry']['location']['lng']
    coord = (latitude, longitude)
    return coord

if __name__ == '__main__':
    app.run(debug=True)
