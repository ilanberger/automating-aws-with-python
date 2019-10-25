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
        N=0
        while(len(self._childern)<self.TotalChilds):
            temp = copy.deepcopy(self._ancestor[N%len(self._ancestor)])
            self._childern.append(temp)
            N += 1

    def createChildern(self):
        N=0
        while(len(self._childern)<self.TotalChilds):
            temp = copy.deepcopy(self._childern[N])
            self._childern.append(temp)
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
            print("Cycle - {}".format(cycle))
            self.sortChildrenByTotalAmont()
            self.KillBadresults()
            if(cycle>0):
                self.printGenerationImprovment()
            #print(self._childernDic["TotalAmont"])
            #print(self._childernDic["MaxPayment"])
    def KillBadresults(self):
        newchildlist = []
        n=0
        for i in range(len(self._childernDic["MaxPayment"])):
            if(self._childernDic["MaxPayment"][n]<self._maxPaymentaloud):
                newchildlist.append(self._childern[n])
            else:
                print("child {} removed".format(n))
            n+=1
        self._childern = newchildlist
        "some child were deleted need to doplecate others"
        self.createChildern()


    def RunRandomChange(self):
        self.savepreviousRun()
        childN=-1
        for child in self._childern:
            childN+=1
            if(childN<self.SaveNextGen):
                "leave stronge children"
                continue
            randomselection = random.randint(0,2)
            if(randomselection==1):
                child.ChangeTime()
            elif(randomselection==2):
                child.ChangePercents()
            elif(randomselection==2):
                child.ChangePercents()
                child.ChangeTime()
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






if __name__ == "__main__":
        MyMaskanta=Maskanta("low",800000)
        MyMaskanta.addMadad(1)
        MyMaskanta.AddProgram("PRIME",0.33,30)
        MyMaskanta.AddProgram("MZ",0.13,10)
        MyMaskanta.AddProgram("KLZ",0.20,20)
        MyMaskanta.AddProgram("KZ",0.14,20)
        MyMaskanta.AddProgram("MZ",0.20,20)
        MyMaskanta.calc()
        creature=MaskantaChild(1,"ancestor",MyMaskanta)
        GAL=MaskantaGAL(10,100,100,PrintLevel=5)
        GAL.addAncestor(creature)
        GAL.setMaxPayment(5000)
        GAL.Run()
        GAL.PrintSummary()
