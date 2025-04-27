import pickle
import json
import numpy as np
import os

__location = None
__data_columns = None
__model = None

def get_location(): 
    '''To get the location list'''
    return __location

def load_artifacts():
    print("Loading saved artifacts...")

    base_path = os.path.abspath(os.path.dirname(__file__))  # pakka absolute path

    model_folder = os.path.join(base_path, "Model")

    columns_path = os.path.join(model_folder, "columns.json")
    model_path = os.path.join(model_folder, "linearModel")

    print(f"Trying to load columns from: {columns_path}")
    print(f"Trying to load model from: {model_path}")

    if not os.path.exists(columns_path):
        print("columns.json file not found! 🚨")
    if not os.path.exists(model_path):
        print("linearModel file not found! 🚨")

    with open(columns_path, "r") as f:
        global __location
        global __data_columns
        __data_columns = json.load(f)['columns']
        __location = __data_columns[4:]

    with open(model_path, "rb") as f:
        global __model
        __model = pickle.load(f)

    print("Saved artifacts loaded successfully!")

def estimatePrice(location,sqft,bath,balcony,bhk):
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
