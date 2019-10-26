#!/user/bin/python
from Maskanta import *
import copy
import random

class MaskantaChild:
    def __init__(self,age,serial,Maskanta=None):
        if(Maskanta!=None):
            self.copyMaskanta(Maskanta)
        self.age = age
        self.serial = serial
        self.isDataValid = True

    def SetSerial(self,serial):
        self.serial = serial


    def copyMaskanta(self,Maskanta):
        self.Maskanta=copy.deepcopy(Maskanta)

    def ChangeTime(self,debuglevel=0):
        """
        randomly select 1 program 1-totalamount (0 is used for prime - no change)
        them randomly time to change on program
        time select range (-5::5]) - time is mod by 30 so total time will be in range 10-30
        """
        programsNumbers=list(range(1,self.Maskanta.Nprograms())) #started from 1 , 0 is prime no changeTime
        randomselectedprogram=random.randint(1,len(programsNumbers))
        time = random.randint(-5,5)
        #print("{} {}".format(randomselectedprogram,time))
        self.Maskanta.changeTime(randomselectedprogram,time)
        self.isDataValid = False

    def addyear(self):
        self.age +=1
    def ChangePercents(self,debuglevel=0):
        """
        randomly select 2 program 1-total (0 is used for prime - no change)
        them randomly select percent to move from program a to b
        percent select range (-5::5])
        """
        programsNumbers=list(range(1,self.Maskanta.Nprograms())) #started from 1 , 0 is prime no changeTime
        randomselectedprogram=random.randint(0,len(programsNumbers)-1)
        #print(programsNumbers,randomselectedprogram)
        firstprogramN=programsNumbers.pop(randomselectedprogram)
        if(len(programsNumbers)==1):
            secondprogramN=programsNumbers.pop()
        else:
            secondprogramN=programsNumbers.pop(random.randint(0,len(programsNumbers)-1))
        random_selection=random.randint(-5,5)

        self.Maskanta.changePercent(firstprogramN,secondprogramN,random_selection,debuglevel)
        self.isDataValid = False


    def Run(self):
        if(self.isDataValid == False):
            self.Maskanta.calc() # calc will amke sure all data is valid
            self.isDataValid = True
            self.addyear()

    def GetMaskandaData(self):
        TotalAmont = round(self.Maskanta.GetTotalAmont())
        MaxPayment = round(self.Maskanta.GetMaxPayment())
        FirstPayment = round(self.Maskanta.GetFirstPayment())
        return TotalAmont , MaxPayment , FirstPayment


    def printinfo(self,printlevel=1):
        if(self.isDataValid == False):
            self.Run()
        if(printlevel>0):
            print("serial {} age {}".format(self.serial,self.age))
        #self.Maskanta.print()
        self.Maskanta.printSummary(printlevel)


if __name__ == "__main__":

    MyMaskanta=Maskanta("low",800000)
    MyMaskanta.addMadad(1)
    MyMaskanta.AddProgram("PRIME",0.33,30)
    MyMaskanta.AddProgram("MZ",0.13,10)
    MyMaskanta.AddProgram("KLZ",0.20,20)
    MyMaskanta.AddProgram("KZ",0.14,20)
    MyMaskanta.AddProgram("MZ",0.20,20)
    MyMaskanta.calc(printSummary=False,printTable=False)
    creature=MaskantaChild(1,"aaa",MyMaskanta)
    creature.printinfo()
    creature.ChangeTime()
    creature.printinfo(printlevel=3)
    creature.ChangePercents()
    creature.printinfo(printlevel=3)

    #MyMaskanta.printSummary()
    #MyMaskanta.PrintTable()
