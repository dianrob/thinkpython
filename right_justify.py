def right_justify(s):
    length = 70 - len(s)
    x = ' '*length
    print(f"{x} {s}")
    print(len(x))

right_justify('hackbarth')

