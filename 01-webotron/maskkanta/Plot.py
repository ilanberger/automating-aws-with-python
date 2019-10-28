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
            #print(str_)
        plt.plot(monthstimeline,[maxreturn]*len(monthstimeline),color='black',linestyle='dashed')
        plt.legend()
        #plt.text(50, 2000, "blabla", {'color': 'C2', 'fontsize': 18}, va="top", ha="right")
        plt.text(50, 2000, str_)
        plt.savefig(self.savepath+'MonthlyPayment.png')
        plt.clf()

    def PlotSUMLeft(self):

        #plt.set_label('TotalReturns')
        plt.title("Total left")
        plt.ylabel('Total amount')
        plt.xlabel('months')
        for child in self.MaskantaGAL:
            TotalLeft=child.getTotalLeft()
            monthstimeline=range(0,len(TotalLeft))
            plt.plot(monthstimeline,TotalLeft,label=child.GetSerial())


        #plt.plot(monthstimeline,[maxreturn]*len(monthstimeline),color='black',linestyle='dashed')
        plt.legend()
        #plt.text(50, 2000, "blabla", {'color': 'C2', 'fontsize': 18}, va="top", ha="right")
        #plt.text(50, 2000, str_)
        plt.savefig(self.savepath+'TotalLeft.png')
        plt.clf()

    def PlotMadad(self,ChildN=0):

        #plt.set_label('TotalReturns')
        plt.title("Madad [Month]")
        plt.ylabel('expected MADAD')
        plt.xlabel('months')

        for child in self.MaskantaGAL:
            Madad=child.GetMadad()
            monthstimeline=range(0,len(Madad))
            plt.plot(monthstimeline,Madad,label=child.GetSerial())

        plt.legend()
        plt.savefig(self.savepath+'Madad_month.png')
        plt.clf()

        plt.title("Madad [Year]")
        plt.ylabel('expected MADAD')
        plt.xlabel('Year')

        for child in self.MaskantaGAL:
            Madad=child.GetMadad_year()
            monthstimeline=range(0,len(Madad))
            plt.plot(monthstimeline,Madad,label=child.GetSerial())

        plt.legend()
        plt.savefig(self.savepath+'Madad_year.png')
        plt.clf()

    def PlotRribits(self,ChildN=0):
        plotcolors=["blue","green","red","cyan","magenta","yellow","black"]


        child  = self.MaskantaGAL[ChildN]
        ProgramNames , ProgramValues = child.Maskanta.GetRibits()
        plt.title("RIBITS of {}".format(child.GetSerial()))
        plt.ylabel('expected RIBITS')
        plt.xlabel('Years')
        p=0
        for ProgramName in ProgramNames:
            color=plotcolors[p]
            plt.plot(ProgramValues[p],label=ProgramName, color = color)
            if(ProgramName in ["KZ","MZ"]):
                #add madad_number
                ribit_and_madad=[sum(x) for x in zip(ProgramValues[p], child.GetMadad_year())]
                plt.plot(ribit_and_madad,linestyle='dashed',label="{}+madad".format(ProgramName),color = color)
            p+=1
        plt.legend()
        plt.savefig(self.savepath+'Ribits_of_{}.png'.format(child.GetSerial()))
        plt.clf()

    def PlotMadad1(self,ChildN=0):
        fig, axs = plt.subplots(nrows=1, ncols=2, sharex=True)


        ax = axs[0]
        #plt.title("Madad [Month]")
        ax.set_title('Madad [Months]')
        ax.set_ylabel('expected MADAD')
        ax.set_xlabel('months')

        for child in self.MaskantaGAL:
            Madad=child.GetMadad()
            monthstimeline=range(0,len(Madad))
            ax.plot(monthstimeline,Madad,label=child.GetSerial())
        ax.set_ylim(0,3)
        #ax.legend()


        ax = axs[1]
        ax.set_title('Madad [Years]')
        ax.set_ylabel('expected MADAD')
        ax.set_xlabel('Years')

        for child in self.MaskantaGAL:
            Madad=child.GetMadad_year()
            yeartimeline=range(0,len(Madad))
            ax.plot(yeartimeline,Madad,label=child.GetSerial())
        ax.set_xlim(0, yeartimeline[-1])
        ax.set_ylim(0,3)
        #plt.legend()
        plt.savefig(self.savepath+'Madad_all.png')
        plt.clf()



if __name__ == "__main__":
        PV=800000

        MyMaskanta=Maskanta("low",PV)
        MyMaskanta.addMadad(1)
        MyMaskanta.AddProgram("PRIME",0.33,30)
        MyMaskanta.AddProgram("MZ",0.15,10)
        MyMaskanta.AddProgram("KLZ",0.17,20)
        MyMaskanta.AddProgram("KZ",0.15,20)
        MyMaskanta.AddProgram("MZ",0.10,20)
        MyMaskanta.AddProgram("MLZ",0.10,20)
        MyMaskanta.calc()
        creature=MaskantaChild(1,"ancestor",MyMaskanta)

        MyMaskanta1=Maskanta("low",PV)
        MyMaskanta1.addMadad(1)
        MyMaskanta1.AddProgram("PRIME",0.33,30)
        MyMaskanta1.AddProgram("KLZ",0.37,20)
        MyMaskanta1.AddProgram("MZ",0.30,20)
        MyMaskanta1.calc()
        creature1 = MaskantaChild(2,"programA",MyMaskanta1)

        MyMaskanta2=Maskanta("low",PV)
        MyMaskanta2.addMadad(1)
        MyMaskanta2.AddProgram("PRIME",0.33,30)
        MyMaskanta2.AddProgram("KLZ",0.67,13)
        MyMaskanta2.calc()
        creature2 = MaskantaChild(2,"Best long prime",MyMaskanta2)

        MyMaskanta3=Maskanta("low",PV)
        MyMaskanta3.addMadad(1)
        MyMaskanta3.AddProgram("PRIME",0.20,18)
        MyMaskanta3.AddProgram("KLZ",0.57,16)
        MyMaskanta3.AddProgram("KZ",0.23,15)
        MyMaskanta3.calc()
        creature3 = MaskantaChild(2,"Best short prime",MyMaskanta3)


        PM=PrintMaskanta()
        PM.SetSavePath("/Users/iberger/Documents/temp/")
        PM.AddMaskantaGAL(creature)
        PM.AddMaskantaGAL(creature1)
        PM.AddMaskantaGAL(creature2)
        PM.AddMaskantaGAL(creature3)


        PM.PlotReturn(5000)
        PM.PlotSUMLeft()
        PM.PlotMadad1()
        PM.PlotRribits(0)
