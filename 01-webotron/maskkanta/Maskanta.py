#!/user/bin/python
from MaskantaProgram import *
class Maskanta:
    """Maskanta class."""

    def __init__(self,limit,presetValue):
        """Create a Maskanta objet."""
        self.limit = limit
        self.presetValue= presetValue
        self._programs=[]
        self._programsNotLocked=[]
        self.addMadad(0)




        self.checkLimitvalis()

        self.isMaskantaDataValid = False
        self.initreurnvaluse()

    def initreurnvaluse(self):
        self._maxyears=0
        self._maxpayment=0
        self._firstpayment=0
        self._TotalAmont=0
        self.TotalPecent=0
        self._paymentreturns=[]

        self._Sumleft=[]
        self.avgTime=0
    def GetPaymentReturn(self):
        return self._paymentreturns
    def GetTotalAmont(self):
        return self._TotalAmont
    def GetMaxPayment(self):
        return self._maxpayment
    def GetFirstPayment(self):
        return self._firstpayment
    def Nprograms(self):
        return len(self._programs)
    def getTotalLeft(self):
        return self._Sumleft
    def getAvgTime(self):
        return self.avgTime
    def isMaskantaDataValid(self):
        return self.isMaskantaDataValid
    def checkLimitvalis(self):
        if not ( self.limit in ["high","low"]):
            print("{} not a valide RIBIT Limit".format(self.limit))
            raise ValueError

    def _checktotalsum():
        pass

    def addMadad(self,Madad,printMadad=False):
        self.MADAD=CMADAD(Madad,printMadad)

    def AddProgram(self,RIBIT_Type,Pecent,time_in_years,ribit=None,printData=False,programsLocked=False):


        ribitClass=CRIBIT(RIBIT_Type,time_in_years,self.limit,ribit)
        self._programs.append(
            MaskantaProgram(RIBIT_Type,self.presetValue,Pecent,ribitClass,time_in_years,self.MADAD,printData)
        )
        if(programsLocked == False):
            self._programsNotLocked.append(len(self._programs)-1)
    def GetProgramsNotLocked(self):
        return self._programsNotLocked
    def checkallvaluesvalid(self):
        #print("total part of maskanta {}".format(self.TotalPecent) )
        if (abs(self.TotalPecent - 1))>0.001:
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
                try:
                    program.recalcProgram()
                except:
                    print("****** error in prgram cal *******")
                    program.PrintSummary()
                    raise

            self.avgTime+=program.GetTotalTime()*program.GetPecent()

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

        tempstr+="  |  Total  | Sum left "
        if(printTable):
            print(tempstr)

        for month in range(1,self._maxyears*12+2):
            monthsum=0
            totalSumLeft = 0
            tempstr=""
            tempstr+="{:3} ".format(month)
            for program in self._programs:
                totalSumLeft += program.GetTotalSum(month)
                val=program.GetMonthReturn(month)

                monthsum+=val
                tempstr+="{:8.0f} ".format(val)

            self._paymentreturns.append(monthsum)
            self._Sumleft.append(totalSumLeft)

            tempstr+="  |  {:8.0f} ".format(monthsum)
            tempstr+="  |  {:8.0f} ".format(totalSumLeft)
            if(printTable):
                print(tempstr)
        self._firstpayment=self._paymentreturns[0]
        self._maxpayment=max(self._paymentreturns)
        self.isMaskantaDataValid = True

    def print(self):
        for program in self._programs:
            print("\t{:<6}  {:,}nis ({}) ({:0.3}%)".format(program.GetName(),int(program.GetTotalPay()),program.GetTotalTime(),program.GetPecent()*100))

    def printSummary(self,printlevel= 0):
        if(printlevel>=2):
            print("\tPV {:,} Total return {:,} first payment = {} max return = {} Avgyears {:3.3} (w_o prime)".format(self.presetValue,int(self._TotalAmont),int(self._firstpayment),int(self._maxpayment),self.avgTime))
        for program in self._programs:
            if(printlevel == 3):
                print("\t  {:<6}  {:,}nis ({}) ({:0.3}%)".format(program.GetName(),int(program.GetTotalPay()),program.GetTotalTime(),program.GetPecent()*100))
            elif(printlevel>3):
                print("\t  {:<6}  {:,}nis ({}) ({:0.3}%) {}".format(program.GetName(),int(program.GetTotalPay()),program.GetTotalTime(),program.GetPecent()*100,program.GetRIBIT_byyear()))
        #print("max return {}\nMax years {}".format(int(self._maxpayment),self._maxyears))
        if(printlevel>4):
            self.calc(printSummary=False,printTable=True)

    def changeTime(self,programN,delta_time):
        program = self._programs[programN]
        orignaltime = program.GetTotalTime()
        #time should be [10-30]
        #print("orignaltime {}".format(orignaltime))
        newtime = int((orignaltime+delta_time-10)%20+10)
        #print("new time {} {}".format(newtime,delta_time))
        program.SetTotalTime(newtime)

    def changePercent(self,firstprogramN,secondprogramN,randomRumber,debuglevel=0):
        program1 = self._programs[firstprogramN]
        program2 = self._programs[secondprogramN]
        Pecent1  = program1.GetPecent()
        Pecent2  = program2.GetPecent()
        NewPercent1 = round(max(Pecent1*100+randomRumber,0))/100
        #if(NewPercent1>=(Pecent1+Pecent2)):# in for example 0.1 0 and rand naumber is 5 --> 0.15 -0.05
        #    NewPercent1 = round(max(Pecent1*100-randomRumber,0))/100
        NewPercent2 = round((Pecent1+Pecent2-NewPercent1)*100)/100
        totalPercent = round((Pecent1+Pecent2)*100)/100

        if(min(NewPercent1,NewPercent2)>=0.1):
            """ regular case """
            #print("case 158")
            program1.SetPecent(NewPercent1)
            program2.SetPecent(NewPercent2)
        elif(Pecent1*Pecent2 == 0):
            """ if 1 of the orignal values is 0 and the regular case didint help - swap"""
            #print("case 163")
            program1.SetPecent(Pecent2)
            program2.SetPecent(Pecent1)
        elif(min(NewPercent1,NewPercent2)<0.1):
            """ regular case """
            #print("case 168")
            if(NewPercent1<0.1):
                program1.SetPecent(0.0)
                program2.SetPecent(totalPercent)
            else:
                program1.SetPecent(totalPercent)
                program2.SetPecent(0.0)
        else:
            print("programs {} {} - old {} {}".format(firstprogramN,secondprogramN,Pecent1,Pecent2))
            print("                 new {} {}".format(program1.GetPecent(),program2.GetPecent()))
            rasie

        if(debuglevel>=3):
            print("programs {} {} - old {} {}".format(firstprogramN,secondprogramN,Pecent1,Pecent2))
            print("                 new {} {}".format(program1.GetPecent(),program2.GetPecent()))
        #print("programs {} {} - old {} {}".format(firstprogramN,secondprogramN,Pecent1,Pecent2))
        #print("                 new {} {}".format(NewPercent1,NewPercent2))

    def GetRibits(self):
        ProgramNames=[]
        ProgramValues=[]
        for program in self._programs:
            ProgramNames.append(program.GetName())
            ProgramValues.append(program.rate.GetRIBIT(year=True))
        return ProgramNames , ProgramValues

if __name__ == "__main__":

    MyMaskanta=Maskanta("low",800000)
    MyMaskanta.addMadad(1)
    MyMaskanta.AddProgram("MZ",1/3,10,programsLocked=True)
    MyMaskanta.AddProgram("PRIME",1/3,30)
    MyMaskanta.AddProgram("KLZ",1/3,20,6)
    b=MyMaskanta.GetProgramsNotLocked()
    print(MyMaskanta.GetProgramsNotLocked())

    print(MyMaskanta._programsNotLocked)
    MyMaskanta.calc(False)
    print(MyMaskanta.GetProgramsNotLocked())
    #MyMaskanta.printSummary(5)
    #MyMaskanta.PrintTable()
