moby = open('words.txt')


def readline(words):
    m = []
    for line in words:
        y = words.readline()
        m.append(y.strip())
    return m


def bigger20(m):
    print(' '.join([i for i in m if len(i) > 19]))


m = readline(moby)

bigger20(m)
