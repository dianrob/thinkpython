

def do_twice(f, x):
    f(x)
    f(x)


def do_four(f, x):
    do_twice(f, x)
    do_twice(f, x)


def print_twice(bruce):
    print(bruce)
    print(bruce)


do_four(print_twice, 'spam')

