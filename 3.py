def reverse_list(l):
    """
    Returns the reverse of a list l
    """
    for i in range(len(l)//2):
        temp=l[i]
        l[i]=l[len(l)-i-1]
        l[len(l)-i-1]=temp
    print(l)
