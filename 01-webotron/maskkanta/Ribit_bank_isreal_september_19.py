#!/user/bin/python
#Ribit types
#PRIME
#KLZ KVOA LO TZVODA
#KZ  KVOA    TZVODA
#MLZ MESTANA LO TZVODA
#MZ  MESTANA    TZVODA

value={}
value["PRIME"]={}
value["KZ"]={}
value["KLZ"]={}

value["MLZ"]={}
value["MZ"]={}

prime=1.75
prime_delat=-0.55
value["PRIME"]["high"]         = [prime+prime_delat]*8
value["PRIME"]["low"]          = value["PRIME"]["high"]


value["KLZ"]["high"]= [2.39,3.18,3.16,2.76,3.10,3.44,3.73,3.93]
value["KLZ"]["low"] = value["KLZ"]["high"]

value["MLZ"]["high"] = [3.43]*8
value["MLZ"]["low"]  = [3.43]*8

value["MZ"]["high"] = [2.54]*8
value["MZ"]["low"]  = [2.54]*8

value["KZ"]["high"] = [2.81, 2.71   , 3.16  , 1.96  , 2.28, 2.66, 3.12, 3.33  ]
value["KZ"]["low"]  = value["KZ"]["high"]

fiveyearexpectedchange=[0,0.5,1,1.5,2,2.5,3]
fiveyearexpectedchange=[0]*len(fiveyearexpectedchange)

def GetRIBIT(RIBIT_Type,time,limit):
    list_place=-1
    if(time<1):
        list_place=0
    elif(time<=2):
        list_place=1
    elif(time<=5):
        list_place=2
    elif(time<=10):
        list_place=3
    elif(time<=15):
        list_place=4
    elif(time<=20):
        list_place=5
    elif(time<=25):
        list_place=6
    else:
        list_place=-1
    if not(RIBIT_Type in value.keys()):
        return -1
    if not(limit in value[RIBIT_Type].keys()):
        return -1
    return value[RIBIT_Type][limit][list_place]

class CRIBIT:
    def __init__(self,RIBIT_Type,time_in_years,limit,overrideValue=None):
        """Create a RIBIT objet."""
        self.RIBIT_Type = RIBIT_Type

        self.limit = limit
        self.overrideValue = overrideValue
        #self.MakeRIBITList()
        self.time_in_years = time_in_years # this should be removed
        #self.MakeRIBITList()
        self.RIBIT_list=[]
        self.RIBIT_list_year=[]
    def GetRIBITbyyear(self):
        return self.RIBIT_list_year
    def SetTimeInyears(self,time_in_years):
        self.time_in_years = time_in_years
        self.MakeRIBITList()


    def GetRIBITinYear(self,YearOfMASKANTA=0):
        if(self.RIBIT_Type in ["KZ","KLZ"]):
            return GetRIBIT(self.RIBIT_Type,self.time_in_years ,self.limit)
        elif(self.RIBIT_Type in ["PRIME"]):#need to do better prime estmation
            return GetRIBIT(self.RIBIT_Type,self.time_in_years ,self.limit)
        else:
            RIBIT_ogen= GetRIBIT(self.RIBIT_Type,self.time_in_years ,self.limit)
            fiveyearN=int(YearOfMASKANTA/5)
            return RIBIT_ogen+fiveyearexpectedchange[fiveyearN]

    def MakeRIBITList(self):
        RIBIT_list=[]
        RIBIT_list_year=[]
        if(self.RIBIT_Type in ["KZ","KLZ"]):
            RIBIT_year = self.GetRIBITinYear() if (self.overrideValue==None) else self.overrideValue

            RIBIT_list = [RIBIT_year/12]*12*self.time_in_years
            RIBIT_list_year = [RIBIT_year]*self.time_in_years
        else:
            for year in range(self.time_in_years):
                RIBIT_year=self.GetRIBITinYear(year)
                RIBIT_list_year.append(RIBIT_year)
                for month in range(1,13):
                    RIBIT_list.append(RIBIT_year/12)
        self.RIBIT_list=RIBIT_list
        self.RIBIT_list_year=RIBIT_list_year
    def GetRIBIT(self,year=False):
        if(year):
            return self.RIBIT_list_year
        return self.RIBIT_list
    def PrintRBITData(self):
        print("RIBIT_Type = {}".format(self.RIBIT_Type))
        print("Time_in_years = {}".format(self.time_in_years))
        print("Limit = {}".format(self.limit))
        print("Value is years {} {}".format(len(self.GetRIBIT(True)),self.GetRIBIT(True)))
        if(self.RIBIT_Type in ["MLZ","KLZ"]):
            print("not using madad")

        #print("Value is month {} {}".format(len(self.GetRIBIT(False)),self.GetRIBIT(False)))
    def GetRIBIT_Type(self):
        return self.RIBIT_Type
    def GetRIBIT_limit(self):
        return self.limit
    def UseMadad(self):
        if(self.RIBIT_Type in ["MLZ","KLZ","PRIME"]):
            return False
        return True
