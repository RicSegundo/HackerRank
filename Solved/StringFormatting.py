def binary(n):

    # Returns the binary representation of n

    rev_bin = ''

    while n != 0:
        if n % 2 == 0:
            rev_bin += ('0')
            n = n//2
        else:
            rev_bin += ('1')
            n = n//2

    return rev_bin[::-1]

def hexadecimal(n):

    # Returns the binary representation of n

    hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    rev_rest = ''

    while n != 0:
        rev_rest += hexa[n % 16]
        n = n//16

    return rev_rest[::-1]

def octal(n):

    # Returns Octal representation of n

    oct = ''
    while n != 0:
        oct += str(n % 8)
        n = n//8

    return oct[::-1]

n = 17


def print_formatted(number):
    wid = len('{0:b}'.format(n))
    for i in range(1, n + 1):
        o = octal(i)
        h = hexadecimal(i)
        b = binary(i)
        print(f'{i:>{wid}} {o:>{wid}} {h:>{wid}} {b:>{wid}}')


if __name__ == '__main__':
    print_formatted(n)



"""

def print_formatted(number):
    width = len('{0:b}'.format(n))
    for i in range(1, n + 1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width))

"""