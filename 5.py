def compress(l):
    """
    Returns a list with consecutive duplicate elements replaced by a single element
    """
    i=0
    while i < len(l)-1:
        if l[i] == l[i+1]:
            del l[i]
        else:
            i = i+1
    print(l)        

