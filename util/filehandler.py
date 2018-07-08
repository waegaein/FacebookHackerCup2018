class FileHandler:
    def __init__(self, round):
        self.resDir = 'res'
        self.round = round

    def readFile(self, fileName):
        path = self.round + '/' + self.resDir + '/' + fileName
        f = open(path, 'r')
        lines = list(map(lambda x: x.replace('\n', ''), f.readlines()))
        f.close()
        return lines

    def writeFile(self, fileName, contents):
        path = self.round + '/res/output/' + fileName
        f = open(path, 'w')
        f.write(contents)
        f.close()
