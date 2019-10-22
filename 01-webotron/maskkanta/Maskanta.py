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

        self._paymentreturns=[]


        self.checkLimitvalis()

        self.isMaskantaDataValid = False
        self.initreurnvaluse()

    def initreurnvaluse(self):
        self._maxyears=0
        self._maxpayment=0
        self._TotalAmont=0
        self.TotalPecent=0


    def isMaskantaDataValid(self):
        return self.isMaskantaDataValid
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

    def AddProgram(self,RIBIT_Type,Pecent,time_in_years,ribit=None,printData=False):


        ribitClass=CRIBIT(RIBIT_Type,time_in_years,self.limit,ribit)
        self._programs.append(
            MaskantaProgram(RIBIT_Type,self.presetValue,Pecent,ribitClass,time_in_years,self.MADAD,printData)
        )
    def checkallvaluesvalid(self):
        #print("total part of maskanta {}".format(self.TotalPecent) )
        if (self.TotalPecent !=1):
            print("didn't get 100% of Prgrams (got {}%])".format(self.TotalPecent ))
            return False
        for program in self._programs:
            if not(program.GetRIBIT_Type() in ["PRIME","KZ","KLZ","MLZ","MZ"]):
                print("{} not a valide RIBIT type".format(program.GetRIBIT_Type() ))
                return False


        return True

    def calc(self,printSummary=False,printTable=False):
        self.initreurnvaluse()
        #checl all prgram data are valide ( valuse may change and need to recalc them)
        for program in self._programs:
            if(program.isDataValid()==False):
                program.recalcProgram()
            self._maxyears = max(self._maxyears,program.GetTotalTime())
            self.TotalPecent += program.GetPecent()

        # check all programs get to 100%
        if(self.checkallvaluesvalid()==False):
            return -1

        if(printSummary):
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
        self.isMaskantaDataValid = True

    def print(self):
        for program in self._programs:
            print("{:<6} ({})".format(program.GetName(),program.GetTotalTime()))

    def printSummary(self):
        print("PV {:,}\nTotal return {:,} max return {}\nMax years {}".format(self.presetValue,int(self._TotalAmont),int(self._maxpayment),self._maxyears))
        for program in self._programs:
            print("\t{:<6}  {:,}nis ({}) ({:0.3}%)".format(program.GetName(),int(program.GetTotalPay()),program.GetTotalTime(),program.GetPecent()*100))
        #print("max return {}\nMax years {}".format(int(self._maxpayment),self._maxyears))

    def changeTime(self,programN,delta_time):
        program = self._programs[programN]
        orignaltime = program.GetTotalTime()
        program.SetTotalTime(orignaltime+delta_time)



if __name__ == "__main__":

    MyMaskanta=Maskanta("low",800000)
    MyMaskanta.addMadad(1)
    MyMaskanta.AddProgram("MZ",1/3,10)
    MyMaskanta.AddProgram("PRIME",1/3,30)
    MyMaskanta.AddProgram("KLZ",1/3,20,6)
    MyMaskanta.calc(False)
    MyMaskanta.printSummary()
    #MyMaskanta.PrintTable()
