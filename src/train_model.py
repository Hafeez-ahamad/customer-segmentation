from sklearn.cluster import KMeans
import joblib

def train_model(data, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)

    # Save model
    joblib.dump(kmeans, '../models/kmeans_model.pkl')
    return kmeans
