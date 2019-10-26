#!/user/bin/python
from GAL import *
import copy
import random



class MaskantaGAL:
    def __init__(self,SaveNextGen,TotalChilds,TotalGenerations,PrintLevel):
        self.SaveNextGen = SaveNextGen
        self.TotalChilds = TotalChilds
        self.PrintLevel = PrintLevel
        self.TotalGenerations = TotalGenerations
        self._ancestor = []
        self._childern=[]
        self._childernDic={}
        self._childern_previousRun=[]
        self._childernDic_previousRun={}
        self.SerialNumber=0

    def setMaxPayment(self,maxpayment):
        self._maxPaymentaloud = maxpayment

    def savepreviousRun(self):
        #self._childern_previousRun=copy.deepcopy(self._childern)
        self._childernDic_previousRun=copy.deepcopy(self._childernDic)

    def printGenerationImprovment(self):

        Total = self._childernDic["TotalAmont"][0]
        Total_before = self._childernDic_previousRun["TotalAmont"][0]

        Max = self._childernDic["MaxPayment"][0]
        Max_before = self._childernDic_previousRun["MaxPayment"][0]

        first = self._childernDic["FirstPayment"][0]
        firstbefore = self._childernDic_previousRun["FirstPayment"][0]

        print("  Total Delta {}  ({} --> {})".format((Total_before-Total),Total_before,Total))
        print("  MAX   Delta {}  ({} --> {})".format((Max_before-Max),Max_before,Max))
        print("  First Delta {}  ({} --> {})".format((firstbefore-first),firstbefore,first))

    def addAncestor(self,ancestor):
        temp=copy.deepcopy(ancestor)
        self._ancestor.append(temp)

    def initChildern(self):
        global SerialNumber

        N=0
        while(len(self._childern)<self.TotalChilds):
            temp = copy.deepcopy(self._ancestor[N%len(self._ancestor)])
            self._childern.append(temp)
            self._childern[-1].SetSerial(self.SerialNumber)
            self.SerialNumber += 1
            N += 1

    def createChildern(self):

        N=0
        while(len(self._childern)<self.TotalChilds):
            temp = copy.deepcopy(self._childern[N])
            self._childern.append(temp)
            self._childern[-1].SetSerial(self.SerialNumber)
            self.SerialNumber +=1

            N+=1
        self.UpdateChildrenData()



    def UpdateChildrenData(self):
        count=0
        self._childernDic["TotalAmont"]=[0]*self.TotalChilds
        self._childernDic["MaxPayment"]=[0]*self.TotalChilds
        self._childernDic["FirstPayment"]=[0]*self.TotalChilds
        for child in self._childern:
            child.Run()
            TotalAmont , MaxPayment , FirstPayment = child.GetMaskandaData()

            self._childernDic["TotalAmont"][count] = TotalAmont
            self._childernDic["MaxPayment"][count] = MaxPayment
            self._childernDic["FirstPayment"][count] = FirstPayment
            count+=1

    def Run(self):
        self.initChildern()
        for cycle in range(self.TotalGenerations ):
            self.RunRandomChange()
            #self.printData()
            print("Cycle - {}".format(cycle))
            self.sortChildrenByTotalAmont()
            self.KillBadresults()
            if(cycle>0):
                self.printGenerationImprovment()

            #print(self._childernDic["TotalAmont"])
            #print(self._childernDic["MaxPayment"])
    def printData(self):
        if(self.PrintLevel>0):
            for nchild , child in enumerate(self._childern,start=0):
                print(nchild),
                child.printinfo(self.PrintLevel)

    def KillBadresults(self):
        newchildlist = []
        n=0
        for i in range(len(self._childernDic["MaxPayment"])):
            if(self._childernDic["MaxPayment"][n]<self._maxPaymentaloud):
                newchildlist.append(self._childern[n])
            else:
                self.Dprint("child {} removed".format(n),1)
            n+=1
        self._childern = newchildlist
        "some child were deleted need to doplecate others"
        self.createChildern()


    def RunRandomChange(self):
        self.savepreviousRun()
        for childN , child in enumerate(self._childern,start=0):
        #for child in self._childern:
        #    childN+=1
            self.Dprint("---- {} ------".format(childN),2)
            if(childN<self.SaveNextGen):
                "leave stronge children"
                child.printinfo(self.PrintLevel)
                continue
            randomselection = random.randint(1,3)
            if(randomselection==1):
                self.Dprint("Time changed",2)
                child.ChangeTime(self.PrintLevel)

            elif(randomselection==2):
                self.Dprint("Percents changed",2)
                child.ChangePercents(self.PrintLevel)

            elif(randomselection==3):
                self.Dprint("Time + Percents changed",2)
                child.ChangePercents(self.PrintLevel)
                child.ChangeTime(self.PrintLevel)

            else :
                print(randomselection)
                raise
            child.printinfo(self.PrintLevel)
        self.UpdateChildrenData()

    def sortChildrenByTotalAmont(self):
        Y = copy.copy(self._childernDic["TotalAmont"])

        X = self._childern

        newlist = copy.copy(Y)
        newlist.sort()
        X = self._childern
        newchildernlist = []
        place=0
        totalChildren=len(self._childern)
        for val in newlist:
            for i in range(len(Y)):
                if(Y[i]==val):
                    "value found"
                    newchildernlist.append(self._childern.pop(i))
                    Y.pop(i)
                    #print("found {} in place {}".format(val,i))
                    break


        self._childern = newchildernlist
        #print(self._childern)
        self.UpdateChildrenData()

    def PrintSummary(self):
        self._ancestor[0].printinfo(printlevel=3)
        self._childern[0].printinfo(printlevel=3)
        print("Total serial #{}".format(self.SerialNumber))
        for childN , child in enumerate(self._childern,start=0):
            child.printinfo(2)

    def Dprint(self,str1,orglevel):
        if(orglevel<=self.PrintLevel):
            print(str1)




if __name__ == "__main__":
        MyMaskanta=Maskanta("low",800000)
        MyMaskanta.addMadad(1)
        MyMaskanta.AddProgram("PRIME",0.33,30)
        MyMaskanta.AddProgram("MZ",0.15,10)
        MyMaskanta.AddProgram("KLZ",0.17,20)
        MyMaskanta.AddProgram("KZ",0.15,20)
        MyMaskanta.AddProgram("MZ",0.10,20)
        MyMaskanta.AddProgram("MLZ",0.10,20)
        MyMaskanta.calc()
        creature=MaskantaChild(1,"ancestor",MyMaskanta)
        #GAL=MaskantaGAL(10,100,20,PrintLevel=0)
        GAL=MaskantaGAL(10,100,100,PrintLevel=0)
        GAL.addAncestor(creature)
        GAL.setMaxPayment(5000)
        GAL.Run()
        GAL.PrintSummary()
