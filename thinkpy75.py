import math


def mathsqrt(a):
    return math.sqrt(a)


def mathsqrt_repeat():
    n = 1
    c = []
    for n in range(1, 11):
        list2 = math.sqrt(n)
        c.append(list2)
    return c


def mysqrt(a):
    x = 1
    a = int(a)
    while True:
        y = (x + a/x) / 2
        epsilon = 0.0000001
        if abs(y-x) < epsilon:
            return x
            break
        x = y


def tuplelist():
    n = 1
    c = []
    for n in range(1, 11):
        low = mysqrt(n)
        c.append(low)
    return c


def first_two_rows():
    print('a   mysqrt(a)     math.sqrt(a)   diff')
    print('-   ---------     -------------  ----')


def print_row():
    for n in range(1, 10):
        print(float(n),  "{:<9f}".format(list_my_sqrt[n-1]),
              "{:<9f}".format(math.sqrt(n)),
              list_my_sqrt[n-1] - math.sqrt(n))
    return


# def diff(a, b, n):
#    for n in range(1, 10):
#        return(a[n] - b[n])


list_my_sqrt = tuplelist()
print(list_my_sqrt)
list_math_sqrt = mathsqrt_repeat()
# list_diff = diff(list_my_sqrt[0], list_math_sqrt[0], 1)

first_two_rows()
print_row()

