from . filehandler import InputReader
from . inputparser import InputParser

class Utility:
    def __init__(self, inputDir):
        self.inputReader = InputReader('input')
        self.inputParser = InputParser()

    def p1(self):
        strings = self.inputReader.readFile('tourist_example_input.txt')
        self.inputParser.parseP1()
