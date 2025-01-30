import matplotlib.pyplot as plt
import seaborn as sns

def visualize_clusters(data, clusters):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=data.iloc[:, 0], y=data.iloc[:, 1], hue=clusters, palette='viridis')
    plt.title('Customer Segmentation using K-Means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.savefig('../results/clustering_results.png')
    plt.show()
