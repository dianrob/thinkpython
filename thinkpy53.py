def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print("Holy shit, Fermat was wrong!")
        else:
            print("That doesn't work.")
    else:
        print("Please enter n > 2")


def fermat_input():
    a = int(input("Please enter a number for a!\n"))
    b = int(input("Please enter a number for b!\n"))
    c = int(input("Please enter a number for c!\n"))
    n = int(input("Please enter a number for n!\n"))

    check_fermat(a, b, c, n)


def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print("No!")
    else:
        print("Yes!")


def is_triangle_input():
    a = int(input("Please enter a number for a!\n"))
    b = int(input("Please enter a number for b!\n"))
    c = int(input("Please enter a number for c!\n"))
    is_triangle(a, b, c)


def recurse(n, s):
    """
    Takes two integer as params and sums them with each recursive call while subtracting from the first param. As soon
    as this hits 0 the sum is printed
    """
    print(f"recurse    n -> {n}")
    print(f"recurse    s -> {s}")
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)




