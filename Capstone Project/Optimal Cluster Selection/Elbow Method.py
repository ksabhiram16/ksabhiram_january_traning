inertia = []

for k in range(2,10):
    km = KMeans(n_clusters=k)
    km.fit(scaled_data)
    inertia.append(km.inertia_)

plt.plot(range(2,10), inertia)
plt.xlabel("K")
plt.ylabel("Inertia")
plt.show()
