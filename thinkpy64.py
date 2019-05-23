def ispower(a, b):
    if a == b:
        return True
    elif a % b == 0:
        return ispower(a/b, b)
    else:
        return False


print(ispower(2, 10))


def gcd(a, b):
    r = a & b

    if gcd(a, 0) = a:
        return a
    
    elif gcd(b, r):
        
    else:
        return False

