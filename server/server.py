from flask import Flask, request, jsonify, request
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/hello')
def hello():
    return 'hi'

@app.route('/get_location')
def location():
    response = jsonify({'locations': util.get_location()})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
# creating a route for predicting price
@app.route('/makeprediction',methods=['POST'])
def Predict():
    try: 
        sqft = float(request.form['sqft'] )
        bath = float(request.form['bath'] )
        balcony = float(request.form['balcony'] )
        bhk = float(request.form['bhk'])
        location = request.form['location']
        

        if request.method == 'OPTIONS':
            response = jsonify({'estimated_price':util.estimatePrice(location,sqft,bath,balcony,bhk)})
            
            return response
        
        response = jsonify({'estimated_price':util.estimatePrice(location,sqft,bath,balcony,bhk)})
    
        return response
    except:
        return "invalid Entries"



if __name__ == "__main__":
    print("Starting python flask server...")
    util.load_artifacts()
    app.run()