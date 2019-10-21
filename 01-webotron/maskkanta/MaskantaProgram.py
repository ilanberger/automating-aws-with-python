#!/user/bin/python

from Ribit import *
def PMT(presetValue,rate,time_in_years):
    time_in_months=time_in_years*12.0
    rate_month=rate*1.0/12/100
    PMT_=PMT_month(presetValue,rate_month,time_in_months)
    return PMT_

def PMT_month(presetValue,rate_month,time_in_months):
    PMT_=presetValue*rate_month/(1-1.0/((1.0+rate_month)**time_in_months))
    return PMT_

def calcMaskantaProgram(presetValue,rate,time_in_years,madad,printinfo=False):
    time_in_months=time_in_years*12.0
    #rate_month=rate*1.0/12/100
    #madam_month=madad*1.0/12/100
    monthReturn_list=[]
    Keren_total=presetValue
    Rebit=0
    Keren_return=0
    Total_return=0

    Sum_Rebit=0
    Sum_Total=0

    madam_month_list = madad.GetMadad_list()
    #rate_month_list  = [0.1666]*int(time_in_months)
    rate_month_list  = rate.GetRIBIT()

    for month in range(1,int(time_in_months+1)):
        Keren_total=Keren_total*(1+madam_month_list[month-1]/100)

        monthReturn=PMT_month(Keren_total,rate_month_list[month-1]/100,(time_in_months-month+1))
        Rebit=Keren_total*rate_month_list[month-1]/100
        Keren_return=monthReturn-Rebit

        if(printinfo):
            print("{:3} {:8.0f} {:8.0f} {:8.0f} {:8.0f}".format(month,monthReturn,Keren_return,Rebit,Keren_total))

        Sum_Rebit+=Rebit
        Sum_Total+=monthReturn
        monthReturn_list.append(monthReturn)

        Keren_total=Keren_total-Keren_return

    return Sum_Rebit,Sum_Total,monthReturn_list

class MaskantaProgram:
    """MaskantaProgram class."""

    def __init__(self,Name,presetValue,RIBIT,time_in_years,madad):
        """Create a MaskantaProgram objet."""
        self.Name = Name
        self.presetValue = presetValue

        self.time_in_years = time_in_years
        self.madad = madad
        self.rate = RIBIT

        Sum_Rebit,Sum_Total,monthReturn_list = calcMaskantaProgram(self.presetValue,self.rate,self.time_in_years,self.madad,False)
        self.Sum_Rebit = Sum_Rebit
        self.Sum_Total = Sum_Total
        self.monthReturn_list = monthReturn_list
    def PrintSummary(self):
        print("\nMaskanta  {} {:,}\nTime = {}".format(self.Name, self.presetValue ,self.time_in_years))
        print("Total pay {:,}  ({:,} rebit {:,} MADAD )".format(round(self.Sum_Total),round(self.Sum_Rebit),round(self.Sum_Total-self.Sum_Rebit-self.presetValue)))
        self.madad.GetMadad_print()
        print("\nRIBITS")
        self.rate.PrintRBITData()

    def PrintTable(self):
        calcMaskantaProgram(self.presetValue,self.rate,self.time_in_years,self.madad,True)

    def GetTotalPay(self):
        return self.Sum_Total

    def GetMonthlyPay(self):
        return self.monthReturn_list

presetValue=800000

madad = 1# in % ,1 percent


RIBIT_Type="MZ"
time_in_years=30
limit="low"
ribit_kovoa=CRIBIT(RIBIT_Type,time_in_years,limit)
#ribit_kovoa.PrintRBITData()

MADAD=CMADAD(madad)

if __name__ == "__main__":
    MyMaskantaProgram=MaskantaProgram("my first MaskantaProgram",presetValue,ribit_kovoa,time_in_years,MADAD)
    #MyMaskantaProgram.PrintTable()
    MyMaskantaProgram.PrintSummary()
