from QCAlgorithm import QCAlgorithm
import numpy as np

class BasicTemplateAlgorithm(QCAlgorithm):

    def Initialize(self):
        print 'Initialize method called'
        self.SetCash(200000)
        print 'Cash: %d' % self.cash

        print 'Pi = %f' % np.pi

    def OnData(self, data):
        pass

if __name__ == "__main__":
    algorithm = BasicTemplateAlgorithm()
    algorithm.Initialize()