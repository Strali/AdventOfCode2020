from typing import List

def listprod(factors: List[int]):
    """Calculate the product of a list of integers"""

    product = 1
    for factor in factors:
        product = product*factor

    return product
