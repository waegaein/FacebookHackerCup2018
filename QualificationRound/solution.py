import sys
import filehandler as fh

def p1():
    print('p1')
    inputReader = fh.InputReader('input')
    strings = inputReader.readFile('tourist_example_input.txt')
    print(strings)

def p2():
    print('p2')

def p3():
    print('p3')

if __name__ == '__main__':
    prob = sys.argv[1]
    if prob == '1':
        p1()
    elif prob == '2':
        p2()
    elif prob == '3':
        p3()
    else:
        print('Invalid Argument')
