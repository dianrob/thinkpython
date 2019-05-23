def reversal_loop(n):
    index = -1
    while abs(index) <= abs(len(n)):
        letter = n[index]
        print(letter)
        index = index - 1


prefixes = 'JKLMNOPQ'
suffix = 'ack'


def ducklings():
    for letter in prefixes:
        if letter == 'O' or letter == 'Q':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)


# ducklings()


def find(word, letter, n):
    while n < len(word):
        if word[n] == letter:
            return n
        n = n + 1
    return -1


# print(find('bananas', 's', 2))

def count(word, letter, n):
    count = 0
    while n < len(word):
        if word[n] == letter:
            count = count + 1
        n = n + 1
    print(count)


count('banana', 'a', 1)
