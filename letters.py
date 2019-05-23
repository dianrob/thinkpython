def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)


def do_n(f, n):
    if n <= 0:
        return
    f()
    do_n(f, n-1)



