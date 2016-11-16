from QCAlgorithm import QCAlgorithm
import numpy as np
from QuantConnect import *

class BasicTemplateAlgorithm(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2013, 10, 7)
        self.SetEndDate(2013, 10, 11)
        self.SetCash(np.pi * 100000)

        self.AddSecurity(SecurityType.Equity, "SPY")
        
        print self.StartDate
        print self.EndDate
        print self.Portfolio.Cash

    def OnData(self, data):
        pass

if __name__ == "__main__":
    algorithm = BasicTemplateAlgorithm()
    algorithm.Initialize()