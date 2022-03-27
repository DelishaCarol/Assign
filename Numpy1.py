
import numpy as np
def gen_strides(a, stride_len, window_len):
    '''
    Input:
      a: Numpy array of 1 dimension
      stride_len: int, stride length
      window_len : int, window length
    
    Output:
      Numpy array of 2 dimensions containing windowed strides as explained above
    '''
    l=[]
    li=[]
    for i in range(0,arr.size,stride_len):
        l=arr[i:i+4]
        if l.size==4:
            
            li.append(l)
        
    print(li)
        

a=eval(input("Enter the array(of 1 D):"))
arr=np.array(a)
stride_len=int(input("Enter the stride length:"))
window_len=int(input("Enter the window length:"))
gen_strides(arr,stride_len,window_len)
