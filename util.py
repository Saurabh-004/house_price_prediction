import pickle
import json
import numpy as np
import os

__location = None
__data_columns = None
__model = None

def get_location():
    '''Return location list'''
    return __location

# util.py (updated)
def load_artifacts():
    print("Loading saved artifacts...")
    try:
        # Get the directory of util.py
        base_path = os.path.dirname(os.path.abspath(__file__))
        model_folder = os.path.join(base_path, "Model")  # Model folder is next to util.py

        # Load columns.json
        with open(os.path.join(model_folder, "columns.json"), "r") as f:
            global __location, __data_columns
            data = json.load(f)
            __data_columns = data['columns']  # Ensure the key is 'columns'
            __location = __data_columns[4:]  # Adjust slicing if needed

        # Load the model
        with open(os.path.join(model_folder, "linearModel"), "rb") as f:
            global __model
            __model = pickle.load(f)

        print("Artifacts loaded successfully!")
    except Exception as e:
        print(f"Error loading artifacts: {str(e)}")

def estimatePrice(location, sqft, bath, balcony, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

if __name__ == "__main__":
    load_artifacts()
    print(get_location())
    print(estimatePrice("indira nagar", 1500, 2, 1, 2))
