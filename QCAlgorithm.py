class QCAlgorithm(object):
    def __init__(self):
        self.cash = 100000;
        print 'Hello World! Default cash: %d' % self.cash 

    def Initialize(self):
        pass

    def OnData(self, data):
        pass

    def SetCash(self, cash):
        self.cash = cash