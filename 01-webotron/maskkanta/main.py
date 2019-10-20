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

def calcMaskanta(presetValue,rate,time_in_years,madad,printinfo=False):
    time_in_months=time_in_years*12.0
    rate_month=rate*1.0/12/100
    #madam_month=madad*1.0/12/100
    monthReturn_list=[]
    Keren_total=presetValue
    Rebit=0
    Keren_return=0
    Total_return=0

    Sum_Rebit=0
    Sum_Total=0

    madam_month_list = madad.GetMadad_list()
    rate_month_list  = [rate_month]*int(time_in_months)

    for month in range(1,int(time_in_months+1)):
        Keren_total=Keren_total*(1+madam_month_list[month-1]/100)

        monthReturn=PMT_month(Keren_total,rate_month_list[month-1],(time_in_months-month+1))
        Rebit=Keren_total*rate_month_list[month-1]
        Keren_return=monthReturn-Rebit

        if(printinfo):
            print("{:3} {:8.0f} {:8.0f} {:8.0f} {:8.0f}".format(month,monthReturn,Keren_return,Rebit,Keren_total))

        Sum_Rebit+=Rebit
        Sum_Total+=monthReturn
        monthReturn_list.append(monthReturn)

        Keren_total=Keren_total-Keren_return

    return Sum_Rebit,Sum_Total,monthReturn_list

class Maskanta:
    """Maskanta class."""

    def __init__(self,Name,presetValue,rate,time_in_years,madad):
        """Create a Maskanta objet."""
        self.Name = Name
        self.presetValue = presetValue
        self.rate = rate
        self.time_in_years = time_in_years
        self.madad = CMADAD(madad)

        Sum_Rebit,Sum_Total,monthReturn_list = calcMaskanta(self.presetValue,self.rate,self.time_in_years,self.madad,False)
        self.Sum_Rebit = Sum_Rebit
        self.Sum_Total = Sum_Total
        self.monthReturn_list = monthReturn_list
    def PrintSummary(self):
        print("\nMaskanta  {} {:,}\nRate = {}\nMadad = {}\nTime = {}".format(self.Name, self.presetValue ,self.rate ,self.madad.GetMadad_print() ,self.time_in_years))
        print("Total pay {:,}  ({:,} rebit)".format(round(self.Sum_Total),round(self.Sum_Rebit)))

    def PrintTable(self):
        calcMaskanta(self.presetValue,self.rate,self.time_in_years,self.madad,True)

    def GetTotalPay(self):
        return self.Sum_Total

    def GetMonthlyPay(self):
        return self.monthReturn_list

presetValue=800000
rate  = 2 # in % ,2 percent
madad = 1# in % ,1 percent
time_in_years=10

#print(PMT(presetValue,rate,time_in_years))

#Sum_Rebit,Sum_Total,monthReturn_list = calcMaskanta(presetValue,rate,time_in_years,madad,True)
#print("\nMaskanta {}\nRate = {}\nMadad = {}\nTime = {}".format(presetValue,rate,madad,time_in_years))
#print("Total pay {:8.0f}  ({:8.0f} rebit)".format(Sum_Total,Sum_Rebit))

MyMaskanta=Maskanta("my first maskanta",presetValue,rate,time_in_years,madad)
MyMaskanta.PrintTable()
MyMaskanta.PrintSummary()
#print(GetRIBIT("PRIEM",10,"low"))
#print(GetRIBIT("KVOA_LO_TZAMOD",30,"high"))
