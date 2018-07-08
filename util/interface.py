from .filehandler import InputReader
from .inputparser import InputParser

class UtilityInterface:
    def __init__(self, round):
        self.inputReader = InputReader(round)
        self.inputParser = InputParser()

    def prepareQrP1(self):
        strings = self.inputReader.readFile('tourist_example_input.txt')
        self.inputParser.parseQrP1(strings)

    def prepareQrP2(self):
        strings = self.inputReader.readFile('interception_example_input.txt')
        self.inputParser.parseQrP2(strings)

    def prepareQrP3(self):
        strings = self.inputReader.readFile('ethan_searches_for_a_string_example_input.txt')
        self.inputParser.parseQrP3(strings)
