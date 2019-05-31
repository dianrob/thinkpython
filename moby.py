fin = open('words.txt')


def fin_strip(m):
    x = []
    for line in m:
        word = line.strip()
        x.append(word)
    return x


def over20(m):
    y = fin_strip(m)
    for i in y:
        if len(i) > 19:
            print(i)


def has_no_e(word):
    y = fin_strip(word)
    z = len(y)
    count = 0
    for i in y:
        if 'e' not in i:
            print(i)
            count += 1
    print(count * 100 / z)

# exercise 9.3


def avoid(word, string):
    if string not in word:
        return True


# exercise 9.4

def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True

# exercise 9.5


def uses_all(word, string):
    for letter in string:
        if letter not in word:
            return False
    return True


def list_check(f):
    x = []
    for i in f:
        if uses_all(i, 'aeiouy'):
            x.append(i)
    print(len(x))


list_check(fin)
