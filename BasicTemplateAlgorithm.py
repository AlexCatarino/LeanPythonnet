from QCAlgorithm import QCAlgorithm

class BasicTemplateAlgorithm(QCAlgorithm):

    def Initialize(self):
        print 'Initialize method called'

    def OnData(self, data):
        pass

if __name__ == "__main__":
    algorithm = BasicTemplateAlgorithm()
    algorithm.Initialize()