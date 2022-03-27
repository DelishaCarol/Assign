import numpy as np
def lin_eqn(a,b):
    a = np.array([[1, 2], [3, 4]])  
    b = np.array([8, 18])

    inv_a=np.linalg.inv(a)
    x=np.dot(inv_a,b)
    print(x)

