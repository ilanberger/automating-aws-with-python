#!/user/bin/python
from Maskanta import *
import copy
class MaskantaChild:
    def __init__(self,age,serial,Maskanta=None):
        if(Maskanta!=None):
            self.copyMaskanta(Maskanta)
        self.age = age
        self.serial = serial
        self.isDataValid = True

    def copyMaskanta(self,Maskanta):
        self.Maskanta=copy.deepcopy(Maskanta)

    def ChangeTime(self,programN=2,time=-5):
        self.Maskanta.changeTime(programN,time)
        self.isDataValid = False

    def ChangeAmount(self):
        pass
    def printinfo(self):
        if(self.isDataValid == False):
            self.Maskanta.calc() # calc will amke sure all data is valid
            self.isDataValid = True
        print("serial {} age {}".format(self.serial,self.age))
        #self.Maskanta.print()
        self.Maskanta.printSummary()
if __name__ == "__main__":

    MyMaskanta=Maskanta("low",800000)
    MyMaskanta.addMadad(1)
    MyMaskanta.AddProgram("MZ",1/3,10)
    MyMaskanta.AddProgram("PRIME",1/3,30)
    MyMaskanta.AddProgram("KLZ",1/3,20,6)
    MyMaskanta.calc(printSummary=False,printTable=False)
    creature=MaskantaChild(1,"aaa",MyMaskanta)
    creature.printinfo()
    creature.ChangeTime()
    creature.printinfo()

    #MyMaskanta.printSummary()
    #MyMaskanta.PrintTable()
