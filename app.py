from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import util
import os

app = Flask(__name__, static_folder='client', static_url_path='')
CORS(app)  # CORS lagana zaruri hai bro jab remote pe ho

# Route for home
@app.route('/')
def serve_home():
    return app.send_static_file('app.html')


# Serve static files (CSS, JS, Images)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

# API endpoint for location
@app.route('/get_location')
def get_location():
    response = jsonify({'locations': util.get_location()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# API endpoint for price prediction
@app.route('/makeprediction', methods=['POST'])
def make_prediction():
    try:
        sqft = float(request.form['sqft'])
        bath = float(request.form['bath'])
        balcony = float(request.form['balcony'])
        bhk = float(request.form['bhk'])
        location = request.form['location']

        estimated_price = util.estimatePrice(location, sqft, bath, balcony, bhk)
        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        return jsonify({'error': str(e)})

# IMPORTANT: Port change for Render/Heroku
# app.py (updated)
# ... (previous imports)

util.load_artifacts()  # Load artifacts when the app starts

# ... (rest of your routes)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
