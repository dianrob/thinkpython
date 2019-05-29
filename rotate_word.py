def rotate_word(str, num):
    x = []
    for foo in str:
        y = ord(foo) + num
        x.append(chr(y))
    print(''.join(x))


rotate_word('banana', 3)
