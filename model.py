import pickle
import numpy as np
import pandas as pd
import random

def model():
    df=pd.read_csv("data_proc.csv")
    ans=df.iloc[:,-2:]
    arr=np.array(ans)
    charging_stations = arr
    with open('knn_model.pkl', 'rb') as file:
        knn_model = pickle.load(file)
    keys=list(df.index)
    random_key=random.choice(keys)
    lat=df.loc[random_key]['Latitude']
    lon=df.loc[random_key]['Longitude']
    user_coordinates = np.array([[ lat, lon ]]) 
    distances, indices = knn_model.kneighbors(user_coordinates)
    nearest_charging_stations = charging_stations[indices]
    # return nearest_charging_stations
    data = nearest_charging_stations[0]
    new_df = pd.DataFrame(data, columns=["Latitude", "Longitude"])
    matched_rows = []
    for index, row in new_df.iterrows():
        latitude = row['Latitude']
        longitude = row['Longitude']
        row_loc = df.loc[(df['Latitude'] == latitude) & (df['Longitude'] == longitude)]
        matched_rows.append(row_loc)
    result_df = pd.concat(matched_rows, ignore_index=True)
    df_dict_list = result_df.to_dict(orient='list')
    station_dict = {name: (lat, lon) for name, lat, lon in zip(df_dict_list['Station Names'], df_dict_list['Latitude'], df_dict_list['Longitude'])}
    cur_loc=df.loc[random_key]
    return [station_dict,cur_loc]

def generate_random_coordinate(center, radius):
    angle = np.random.uniform(0, 2 * np.pi)
    r = radius * np.sqrt(np.random.uniform(0, 1))
    dx = r * np.cos(angle)
    dy = r * np.sin(angle)
    random_lat = center[0] + (dy / 110.574)  # Approx. km per degree latitude
    random_lon = center[1] + (dx / (111.320 * np.cos(np.radians(center[0]))))  # Approx. km per degree longitude
    return np.array([random_lat, random_lon])
    


