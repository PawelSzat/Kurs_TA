import sys
from calc import Calculator

def main(*args):
    calc = Calculator()
    left, op, right = args
    print({
        '+': calc.add,
        '-': calc.sub,
        'x': calc.mul,
        '/': calc.div,
    }[op](int(left), int(right)))

if __name__ == '__main__':
    args = sys.argv[1:]
    main(*args)
