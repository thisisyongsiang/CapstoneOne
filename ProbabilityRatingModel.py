
from cmath import sqrt

def linear(review_count, rating):
    """
    Function takes in review and rating as inputs, and computes a consolidated rating value based on the confidence of the rating achieved by the number of reviews availability
    This uses a LINEAR probability model.
    """

    if review_count <= 1000:
        return (0.7+0.0003*review_count)*rating
    else:
        return rating

def exponential(review_count, rating):
    """
    Function takes in review and rating as inputs, and computes a consolidated rating value based on the confidence of the rating achieved by the number of reviews availability
    This uses an EXPONENTIAL probability model.
    """

    return abs(review_count/(sqrt((1/0.09)*(review_count**2)+1000000)) + 0.7)*rating
