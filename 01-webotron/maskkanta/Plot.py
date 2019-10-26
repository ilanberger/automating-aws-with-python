#!/user/bin/python
from GAL_main import *

import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')

#plt.show()
#plt.savefig('/Users/iberger/Documents/temp/foo.png')
class PrintMaskanta:
    def __init__(self):
        self.MaskantaGAL = []
        self.savepath=""
    def AddMaskantaGAL(self,MaskantaGAL):
        self.MaskantaGAL.append(MaskantaGAL)

    def SetSavePath(self,setpath):
        self.savepath = setpath
    def PlotReturn(self,maxreturn):

        #plt.set_label('TotalReturns')
        plt.title("TotalReturns")
        plt.ylabel('return')
        plt.xlabel('months')
        str_="Total Retuens\n"
        for child in self.MaskantaGAL:
            returns=child.getReturns()
            monthstimeline=range(0,len(returns))
            plt.plot(monthstimeline,returns,label=child.GetSerial())
            TotalAmont , MaxPayment , FirstPayment = child.GetMaskandaData()
            str_+="{} {:,}\n".format(child.GetSerial(),TotalAmont)
            print(str_)
        plt.plot(monthstimeline,[maxreturn]*len(monthstimeline),color='black',linestyle='dashed')
        plt.legend()
        #plt.text(50, 2000, "blabla", {'color': 'C2', 'fontsize': 18}, va="top", ha="right")
        plt.text(50, 2000, str_)
        plt.savefig(self.savepath+'foo.png')



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

        MyMaskanta1=Maskanta("low",800000)
        MyMaskanta1.addMadad(1)
        MyMaskanta1.AddProgram("PRIME",0.33,30)
        MyMaskanta1.AddProgram("KLZ",0.37,20)
        MyMaskanta1.AddProgram("MZ",0.30,20)
        MyMaskanta1.calc()
        creature1 = MaskantaChild(2,"programA",MyMaskanta1)

        MyMaskanta2=Maskanta("low",800000)
        MyMaskanta2.addMadad(1)
        MyMaskanta2.AddProgram("PRIME",0.33,30)
        MyMaskanta2.AddProgram("KLZ",0.67,13)
        MyMaskanta2.calc()
        creature2 = MaskantaChild(2,"Best",MyMaskanta2)

        PM=PrintMaskanta()
        PM.SetSavePath("/Users/iberger/Documents/temp/")
        PM.AddMaskantaGAL(creature)
        PM.AddMaskantaGAL(creature1)
        PM.AddMaskantaGAL(creature2)
        PM.PlotReturn(5000)
