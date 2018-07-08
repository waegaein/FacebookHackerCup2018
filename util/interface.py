from .filehandler import *
from .inputparser import InputParser

class UtilityInterface:
    def __init__(self, round):
        self.fileHandler = FileHandler(round)
        self.inputParser = InputParser()
    # QualificationRound
    # Problem1
    def prepareQrP1(self):
        strings = self.fileHandler.readFile('input/tourist_example_input.txt')
        self.inputParser.parseQrP1(strings)
    def finishQrP1(self, result):
        self.fileHandler.writeFile('tourist_solution_output.txt', result)
        self.checkQrP1();
    def checkQrP1(self):
        self.checker('answer/tourist_example_output.txt', 'output/tourist_solution_output.txt')

    # Problem2
    def prepareQrP2(self):
        strings = self.fileHandler.readFile('interception_example_input.txt')
        self.inputParser.parseQrP2(strings)
        
    # Problem3
    def prepareQrP3(self):
        strings = self.fileHandler.readFile('ethan_searches_for_a_string_example_input.txt')
        self.inputParser.parseQrP3(strings)

    # Meta utility
    def checker(self, answerPath, resultPath):
        answer = self.fileHandler.readFile(answerPath)
        result = self.fileHandler.readFile(resultPath)
        print('=ANSWER=')
        print(('\n').join(answer))
        print('=RESULT=')
        print(('\n').join(result))
        if answer == result:
            print('=CORRECT=')
        else:
            print('=WRONG=')
