from flask import Flask, request, jsonify, send_from_directory
import util
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='client')
CORS(app)  # CORS allow kar diya pura

# Serve index.html on root
@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'app.html')

# Serve static files (css, js, images)
@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(app.static_folder, path)

# API route to get locations
@app.route('/get_location', methods=['GET'])
def get_location():
    response = jsonify({'locations': util.get_location()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# API route to make prediction
@app.route('/makeprediction', methods=['POST'])
def make_prediction():
    try:
        sqft = float(request.form['sqft'])
        bath = float(request.form['bath'])
        balcony = float(request.form['balcony'])
        bhk = float(request.form['bhk'])
        location = request.form['location']
        price = util.estimatePrice(location, sqft, bath, balcony, bhk)
        response = jsonify({'estimated_price': price})
        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Loading model before running the server
if __name__ == "__main__":
    print("Loading saved artifacts...")
    util.load_artifacts()
    print("Artifacts loaded. Starting Flask server...")
    app.run(debug=True)
