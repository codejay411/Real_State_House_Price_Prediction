import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None




def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('artifacts/realestatemodel.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
    print(__locations)

def get_location_names():
    list1=[]
    for i in __locations:
        list1.append(i); 
    return list1

def get_data_columns():
    list1=[]
    for i in __data_columns:
        list1.append(i); 
    return list1
def get_estimated_price(location,sqft,bath,balcony,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    x[3] = balcony
    if loc_index >= 0:
        x[loc_index] = 1

    #return model.predict([x])[0]
    return round(__model.predict([x])[0])

    
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',2850, 4,1,4))
''' print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location'''