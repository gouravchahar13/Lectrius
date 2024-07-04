import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import pickle

df=pd.read_csv("data_proc.csv")
ans=df.iloc[:,-2:]
arr=np.array(ans)
# User coordinates (latitude, longitude)
user_coordinates = np.array([[28.60383, 77.13497891]])

# Function to generate one random coordinate within a given radius
def generate_random_coordinate(center, radius):
    angle = np.random.uniform(0, 2 * np.pi)
    r = radius * np.sqrt(np.random.uniform(0, 1))
    dx = r * np.cos(angle)
    dy = r * np.sin(angle)
    random_lat = center[0] + (dy / 110.574)  # Approx. km per degree latitude
    random_lon = center[1] + (dx / (111.320 * np.cos(np.radians(center[0]))))  # Approx. km per degree longitude
    return np.array([random_lat, random_lon])
radius_km = 10
random_coordinate = generate_random_coordinate(user_coordinates[0], radius_km).reshape(1, -1)
k = 5
knn = NearestNeighbors(n_neighbors=k, algorithm='ball_tree')
knn.fit(arr)

with open('knn_model.pkl', 'wb') as file:
    pickle.dump(knn, file)

