
if __name__ == '__main__':
    a = int(input('a:'))
    b = int(input('b:'))

    if b % 2 == 0:
        print(a-b)
    elif int(str(b)[-1]) == 5:
        print(2*a)
