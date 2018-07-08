from .filehandler import *

class UtilityInterface:
    def __init__(self, round):
        self.fileHandler = FileHandler(round)

    def readInput(self, probName):
        return self.fileHandler.readFile('input/' + probName + '_example_input.txt')

    def writeOutput(self, probName, result):
        self.fileHandler.writeFile(probName + '_solution_output.txt', result)

    def checkOutput(self, probName):
        self.checker(probName + '_example_output.txt', probName + '_solution_output.txt')

    def checker(self, answerPath, resultPath):
        answer = self.fileHandler.readFile('answer/' + answerPath)
        result = self.fileHandler.readFile('output/' + resultPath)
        print('=ANSWER=')
        print(('\n').join(answer))
        print('=RESULT=')
        print(('\n').join(result))
        if answer == result:
            print('=CORRECT=')
        else:
            print('=WRONG=')
