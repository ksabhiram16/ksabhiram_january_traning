from sklearn.metrics import silhouette_score

score = silhouette_score(scaled_data, kmeans_labels)
print("Silhouette Score:", score)

#Also calculate Davies-Bouldin:


from sklearn.metrics import davies_bouldin_score
db_score = davies_bouldin_score(scaled_data, kmeans_labels)
