print("Calculating CLV...")
rfm = calculate_clv(rfm)

print(rfm['CLV_Segment'].value_counts())
