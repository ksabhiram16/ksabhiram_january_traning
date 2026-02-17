rfm['Cluster'] = labels
rfm.groupby('Cluster').mean()

#interept like :

| Cluster | Description                                        |
| ------- | -------------------------------------------------- |
| 0       | High Monetary + High Frequency → Premium Customers |
| 1       | Low Monetary + High Recency → At Risk              |
| 2       | Medium everything → Regular Customers              |
| 3       | Low Frequency → Occasional Buyers                  |


Highest Revenue Segment:
    Cluster with highest Monetary value

Premium Marketing:
     Premium customers → Exclusive offers, VIP programs

Likely to Churn:
     High Recency + Low Frequency cluster

Retention Strategy:
   Loyalty rewards
    Re-engagement emails
     Special discounts


     CLV Formula Used: CLV=Monetary*Frequency

CLV=Monetary×Frequency
Segments:
CLV Segment	             Meaning
Very High	          Most valuable long-term customers
High	              Strong repeat buyers
Medium	              Growth potential customers
Low	Low                engagement customers
