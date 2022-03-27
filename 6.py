def pack(l):
    """
    Returns a list with consecutive duplicate elements packed into sublists
    """
    li=[]
    i=0
    while i < len(l)-1:
        if l[i] == l[i+1]:
            li[i].append(l[i])
        i=i+1
    print(li)
