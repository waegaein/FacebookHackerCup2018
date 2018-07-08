import sys
sys.path.append('..')
# print(sys.path)
from util.interface import UtilityInterface
from .inputparser import InputParser

class Solution:
    def __init__(self):
        self.round = 'QualificationRound'
        self.util = UtilityInterface(self.round)
        self.parser = InputParser()
        self.p1Name = 'tourist'
        self.p2Name = 'interception'
        self.p3Name = 'ethan_searches_for_a_string'

    def p1(self):
        # print('p1')
        probName = self.p1Name
        self.parser.parseP1(self.util.readInput(probName))
        self.util.writeOutput(probName, 'testt')
        self.util.checkOutput(probName)

    def p2(self):
        # print('p2')
        probName = self.p2Name
        self.parser.parseP2(self.util.readInput(probName))
        self.util.writeOutput(probName, 'testt')
        self.util.checkOutput(probName)

    def p3(self):
        # print('p3')
        probName = self.p3Name
        self.parser.parseP3(self.util.readInput(probName))
        self.util.writeOutput(probName, 'testt')
        self.util.checkOutput(probName)
