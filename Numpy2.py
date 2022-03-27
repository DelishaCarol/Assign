import numpy as np
def shuf(arr):
  '''
  Input: 
    arr: Numpy array of arbitrary number of dimensions (>1)
  Output:
    numpy array of same shape as arr but with rows shuffled
  '''
  a=eval(input("Enter the array:"))
  arr=np.array(a)
  np.random.shuffle(arr)
  print(arr)

