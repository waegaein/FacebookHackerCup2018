import sys
sys.path.append('..')
# print(sys.path)
from util.interface import UtilityInterface

class Solution:
    def __init__(self):
        self.round = 'QualificationRound'
        self.util = UtilityInterface(self.round)

    def p1(self):
        # print('p1')
        self.util.prepareQrP1()
        self.util.finishQrP1('test')

    def p2(self):
        # print('p2')
        self.util.prepareQrP2()

    def p3(self):
        # print('p3')
        self.util.prepareQrP3()
