from .filehandler import InputReader
from .inputparser import InputParser

class UtilityInterface:
    def __init__(self, inputDir):
        self.inputReader = InputReader('input')
        self.inputParser = InputParser()

    def qrP1(self):
        strings = self.inputReader.readFile('tourist_example_input.txt')
        self.inputParser.parseQrP1(strings)
