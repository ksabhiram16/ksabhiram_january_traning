from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=4)
gmm_labels = gmm.fit_predict(scaled_data)
