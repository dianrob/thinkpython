def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1: -1]


def is_palindrome(x):
    if len(x) > 2:
        pal = last(x)
        i_n = middle(x)
        drom = first(x)
        print(pal + i_n + drom)


is_palindrome('otto')


def palindrome_short(x):
    if x[::-1] == x:
        return True
    else:
        return False


palindrome_short('kacke')
