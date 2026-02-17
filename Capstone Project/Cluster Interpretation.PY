rfm['Cluster'] = kmeans_labels
rfm.groupby('Cluster').mean()

#Example interpretation:

| Cluster | Meaning                                        |
| 0       | High frequency, high spend → Premium customers |
| 1       | Low spend, low frequency → At-risk customers   |
| 2       | High recency → Recently inactive               |
| 3       | Moderate everything → Regular customers        |
