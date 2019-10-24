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

    def addAncestor(self,ancestor):
        temp=copy.deepcopy(ancestor)
        self._ancestor.append(temp)

    def initChildern(self):
        N=0
        while(len(self._childern)<self.TotalChilds):
            temp = copy.deepcopy(self._ancestor[N%len(self._ancestor)])
            self._childern.append(temp)

        N += 1
        print(self._childern)

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
            self.UpdateChildrenData()
            print("Cycle - {}".format(cycle))
            self.sortChildrenByMaxAmount()
            print(self._childernDic["MaxPayment"])

    def RunRandomChange(self):
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

    def sortChildrenByMaxAmount(self):
        Y = self._childernDic["MaxPayment"]
        X = self._childern

        newlist = copy.copy(Y)
        newlist.sort()
        print(newlist)
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



        #self._childern  = [x for _,x in sorted(zip(Y,X))]
        #self.UpdateChildrenData()


#X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
#Y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
#Z = [x for _,x in sorted(zip(Y,X))]
#print(Z)  # ["a", "d", "h", "b", "c", "e", "i", "f", "g"]




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
        GAL=MaskantaGAL(2,10,3,PrintLevel=5)
        GAL.addAncestor(creature)
        GAL.Run()
