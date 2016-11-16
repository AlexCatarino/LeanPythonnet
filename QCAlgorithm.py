from decimal import Decimal

import clr
clr.AddReference("System")
clr.AddReference("NodaTime")
clr.AddReference("QuantConnect.Algorithm")
clr.AddReference("QuantConnect.Common")

from System import *
from NodaTime import *
from QuantConnect import * 
from QuantConnect.Securities import *

class QCAlgorithm(object):
    def __init__(self):
        self.Cash = 100000;
        print 'Initial cash: %d' % self.Cash
        self.StartDate = DateTime(1998, 1, 1)
        self.EndDate = DateTime.Now.AddDays(-1)

        self._timeKeeper = TimeKeeper(self.StartDate, [TimeZones.NewYork]);

        self.Securities = SecurityManager(self._timeKeeper);
        self.Transactions = SecurityTransactionManager(self.Securities);
        self.Portfolio = SecurityPortfolioManager(self.Securities, self.Transactions);

    def Initialize(self):
        pass

    def OnData(self, data):
        pass

    def SetStartDate(self, year, month, day):
        self.StartDate = DateTime(year, month, day);

    def SetEndDate(self, year, month, day):
        self.EndDate = DateTime(year, month, day);

    def SetCash(self, cash):
        self.Cash = cash
        self.Portfolio.SetCash(Decimal(cash))
        print 'Cash was set to %d' % cash

    def AddSecurity(self, securityType, symbol, resolution = Resolution.Minute, fillDataForward = True, extendedMarketHours = False):
        symbolObject = Symbol.Create(symbol, securityType, Market.USA)
        print '%s was added' % symbolObject        