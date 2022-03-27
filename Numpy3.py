import numpy as np
def match(a,b):
    '''
    Inputs:
      a, b: numpy arrays of same shape of 1 dimension
    Outputs:
      list containing indices where both arrays have same elements
    '''
    '''a=eval(input("Enter the first array:"))
    b=eval(input("Enter the second array:"))
    a_n=np.array(a)
    b_n=np.array(b)'''
    l=[]
    for i in range(0,a_n.size):
        if a_n[i]==b_n[i]:
            l.append(i)
    print(l)

a=eval(input("Enter the first array:"))
b=eval(input("Enter the second array:"))
a_n=np.array(a)
b_n=np.array(b)
match(a_n,b_n)
