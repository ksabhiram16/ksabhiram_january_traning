import pandas as pd

def calculate_clv(rfm):

    # Simple CLV approximation
    rfm['CLV'] = rfm['Monetary'] * rfm['Frequency']

    # Create CLV Segments
    rfm['CLV_Segment'] = pd.qcut(rfm['CLV'],
                                 q=4,
                                 labels=['Low', 'Medium', 'High', 'Very High'])

    return rfm
