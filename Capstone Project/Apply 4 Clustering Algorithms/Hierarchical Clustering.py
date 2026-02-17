rom sklearn.cluster import AgglomerativeClustering

hc = AgglomerativeClustering(n_clusters=4)
hc_labels = hc.fit_predict(scaled_data)
