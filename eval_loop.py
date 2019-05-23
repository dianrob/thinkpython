def eval_loop():
    while True:
        line = input('> ')
        if line == 'done':
            break
        print(eval('type(line)'))
    print(eval('type(line)'))



eval_loop()
