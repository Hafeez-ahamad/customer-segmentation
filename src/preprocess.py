import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(filepath):
    data = pd.read_csv(filepath)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data, data
