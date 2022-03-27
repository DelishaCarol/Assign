import numpy as np
def rankArray(arr):
    '''
    Input:
        arr: Numpy array of arbitrary dimensions 
    Output:
        numpy array of same shape as arr but with elements replaced by their ranks
    '''
    l=[]
    '''a=eval(input("Enter the array:"))
    arr=np.array(a)'''
    copy_arr=arr
    #for i in range(arr.size):
        #for j in range(len(arr[i]):
           # c
    copy_arr.sort()
    print(copy_arr)
 
 
    if len(arr.shape)==1:
        
        for i in range(s.size):
            l.append((i,s[i]))

        for j in range(arr.size):
            for k in range(len(l)):
                if arr[j]==l[k][1]:
                    arr[j]=l[k][0]
        print(arr)
    else:
        for i in range(len(s)):
            for j in range(len(s[i])):
                l.append((j,s[i][j]))
         #print(l)
        
        for k in range(arr.size):
            for x in range(len(arr[k])):
                for m in range(len(l)):
                    if arr[k][x]==l[m][1]:
                         arr[k][x]=l[m][0]
        print(arr)
                        
                
                

       
a=eval(input("Enter the array:"))
arr=np.array(a)
rankArray(arr)
    
