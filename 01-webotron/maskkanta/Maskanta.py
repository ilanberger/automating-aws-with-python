#!/user/bin/python
from MaskantaProgram import *
class Maskanta:
    """Maskanta class."""

    def __init__(self,limit,presetValue):
        """Create a Maskanta objet."""
        self.limit = limit
        self.presetValue= presetValue
        self._programs=[]
        self.addMadad(0)
        self._maxyears=0
        self._paymentreturns=[]
        self._maxpayment=0
        self._TotalAmont=0
        self.checkLimitvalis()
        self.TotalPecent=0

    def checkLimitvalis(self):
        if not ( self.limit in ["high","low"]):
            print("{} not a valide RIBIT Limit".format(self.limit))
            raise ValueError

    def _checktotalsum():
        pass
    def GetmaxPayment(self):
        return self._maxpayment
    def addMadad(self,Madad):
        self.MADAD=CMADAD(Madad)

    def AddProgram(self,RIBIT_Type,Pecent,time_in_years,ribit=None):
        self._maxyears = max(self._maxyears,time_in_years)
        self.TotalPecent += Pecent

        ribitClass=CRIBIT(RIBIT_Type,time_in_years,self.limit,ribit)
        self._programs.append(
            MaskantaProgram(RIBIT_Type,self.presetValue*Pecent,ribitClass,time_in_years,self.MADAD)
        )
    def checkallvaluesvalid(self):
        print(self.TotalPecent )
        if (self.TotalPecent !=1):
            print("didn't get 100% of Prgrams (got {}%])".format(self.TotalPecent ))
            return False
        for program in self._programs:
            if not(program.GetRIBIT_Type() in ["PRIME","KZ","KLZ","MLZ","MZ"]):
                print("{} not a valide RIBIT type".format(program.GetRIBIT_Type() ))
                return False


        return True

    def calc(self,printTable=True):
        #todo make sure all pescent add to PV
        if(self.checkallvaluesvalid()==False):
            return -1
        for program in self._programs:
            program.PrintSummary()

        tempstr="{0:<8}".format("")
        for program in self._programs:
            self._TotalAmont+=program.GetTotalPay()

            tempstr+="{0:<10}".format(program.GetName())

        tempstr+="  |  Total"
        if(printTable):
            print(tempstr)
        for month in range(1,self._maxyears*12+2):
            monthsum=0
            tempstr=""
            tempstr+="{:3} ".format(month)
            for program in self._programs:
                val=program.GetMonthReturn(month)
                monthsum+=val
                tempstr+="{:8.0f} ".format(val)
            self._paymentreturns.append(monthsum)
            tempstr+="  |  {:8.0f} ".format(monthsum)
            if(printTable):
                print(tempstr)
        self._maxpayment=max(self._paymentreturns)

    def printSummary(self):
        print("PV {:,}\nTotal return {:,}".format(self.presetValue,int(self._TotalAmont)))
        for program in self._programs:
            print("\t{:<6}  {:,}nis ({})".format(program.GetName(),int(program.GetTotalPay()),program.GetTotalTime()))
        print("max return {}\nMax years {}".format(int(self._maxpayment),self._maxyears))



if __name__ == "__main__":

    MyMaskanta=Maskanta("low",800000)
    MyMaskanta.addMadad(1)
    MyMaskanta.AddProgram("MZ",1/3,10)
    MyMaskanta.AddProgram("PRIME",1/3,30)
    MyMaskanta.AddProgram("KLZ",1/3,20,6)
    MyMaskanta.calc(False)
    MyMaskanta.printSummary()
    #MyMaskanta.PrintTable()
