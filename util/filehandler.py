class InputReader:
    def __init__(self, round):
        self.inputDir = 'input'
        self.round = round

    def readFile(self, fileName):
        path = self.round + '/' + self.inputDir + '/' + fileName
        f = open(path, 'r')
        lines = list(map(lambda x: x.replace('\n', ''), f.readlines()))
        return lines
