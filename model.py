import pickle
import numpy as np
import pandas as pd

def model():
    df=pd.read_csv("data_proc.csv")
    ans=df.iloc[:,-2:]
    arr=np.array(ans)
    charging_stations = arr
    with open('knn_model.pkl', 'rb') as file:
        knn_model = pickle.load(file)
    user_coordinates = np.array([[28.40359049 , 76.1155232 ]]) 
    distances, indices = knn_model.kneighbors(user_coordinates)
    nearest_charging_stations = charging_stations[indices]
    return nearest_charging_stations