def is_palindrome(l):
    """
    Returns True if l is a palindrome, False otherwise
    """
    a=""
    for i in range(0,len(l)//2):
        if l[i]==l[len(l)-i-1]:
            a="True"
        else:
            a="False"
    if a=="True":
        print("True")
    else:
        print("False")
