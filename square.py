def foo(f, g):
    f()
    do_four(g)
    f()
    do_four(g)
    f()
    do_four(g)
    f()
    do_four(g)
    f()


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def do_eigth(f):
    do_four(f)
    do_four(f)


def print_beam():
    print('+ ' + 4*'- ', end="")


def print_wall():
    print('|         ', end="")


def print_beams():
    do_four(print_beam)
    print('+')
    do_four(print_wall)
    print('|')


print_beams()
