
from cmath import sqrt
from matplotlib.pyplot import axis
import pandas as pd

def linearProbabilityRatingModel(bizData):
    """
    Function takes in dataFrame with review and rating fields and computes a consolidated rating value based on the confidence of the rating achieved by the number of reviews availability.
    This uses a LINEAR probability model.
    """

    bizData['rating_adj_factor'] = bizData['review_count'].apply(lambda x: (0.8+0.0002*x) if x <= 1000 else 1)
    bizData['rating'] = bizData['rating']*bizData['rating_adj_factor']
    outputDf = bizData.drop(['rating_adj_factor'], axis=1)

    return outputDf


def exponentialProbabilityRatingModel(bizData):
    """
    Function takes in dataFrame with review and rating fields and computes a consolidated rating value based on the confidence of the rating achieved by the number of reviews availability
    This uses an EXPONENTIAL probability model.
    """

    bizData['rating_adj_factor'] = bizData['review_count'].apply(lambda x: abs(x/(sqrt((1/0.09)*(x**2)+1000000)) + 0.7))
    bizData['rating'] = bizData['rating']*bizData['rating_adj_factor']
    outputDf = bizData.drop(['rating_adj_factor'], axis=1)

    return outputDf


# code for testing functions if required
# testData = {
#     'id': ['test1','t2','t3','t4','t5'],
#     'distance': [456,123,23,876,454],
#     'lat': [13123,12434,234235,43536,34536],
#     'long': [123124,46788,2454,3454356,345345],
#     'rating': [4.6, 4.9,3.5,2.1,5.0],
#     'price': ['$', '$$', '$','$$$','$$$$'],
#     'review_count': [0,999,23,34353,1245]}

# ls = pd.DataFrame(testData)

# print(linearProbabilityRatingModel(ls))
# print(exponentialProbabilityRatingModel(ls))
