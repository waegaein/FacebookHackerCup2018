class InputReader:
    def __init__(self, inputDir):
        self.inputDir = inputDir

    def readFile(self, fileName):
        path = self.inputDir + '/' + fileName
        f = open(path, 'r')
        print(f.read())
