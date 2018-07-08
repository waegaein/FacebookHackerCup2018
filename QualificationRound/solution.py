import sys
import filehandler as fh

class Solution:
    def __init__(self):
        self.inputReader = fh.InputReader('input')

    def p1(self):
        print('p1')
        strings = self.inputReader.readFile('tourist_example_input.txt')
        print(strings)

    def p2(self):
        print('p2')

    def p3(self):
        print('p3')

if __name__ == '__main__':
    sol = Solution()
    prob = sys.argv[1]
    if prob == '1':
        sol.p1()
    elif prob == '2':
        sol.p2()
    elif prob == '3':
        sol.p3()
    else:
        print('Invalid Argument')
