import numpy as np
def inv(arr):
    """
    Given an array arr (square matrix), find its inverse
    """
    a=eval(input("Enter the array of equal dimensions:"))
    arr=np.array(a)
    print(np.linalg.inv(arr))

