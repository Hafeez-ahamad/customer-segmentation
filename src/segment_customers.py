import joblib
import pandas as pd

def segment_customers(model_path, data):
    model = joblib.load(model_path)
    clusters = model.predict(data)
    return clusters
