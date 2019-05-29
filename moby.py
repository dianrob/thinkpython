moby = open('words.txt')


def readline(words):
    m = []
    for line in words:
        y = words.readline()
        m.append(y.strip())
    return m


def bigger20(m):
    print(' '.join([i for i in m if len(i) > 19]))


def has_no_e(word):
    if 'e' not in word:
        print('True')


has_no_e('banana')



#bigger20(readline(moby))
