import sys
from util.utility import Utility

class Solution:
    def __init__(self):
        self.util = Utility('input')

    def p1(self):
        print('p1')

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
