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

value["PRIME"]["high"]         = [1.75 , 1.75 ,  1.75 ,1.75  , 1.75]
value["PRIME"]["low"]          = [0.95 , 0.95  , 0.95 ,0.95  , 1.75]

value["KLZ"]["high"]= [3.25 , 3.75  , 4.25 , 4.75 , 5  ]
#value["KLZ"]["low"] = [2.5  , 3.00  , 3.75 , 4.00 , 4.5]
value["KLZ"]["low"] = [2 , 2  , 2,2 ,2]

value["KZ"]["high"] = [3  , 3   , 3.5  , 4  , 4  ]
value["KZ"]["low"]  = [1  , 1   , 1    , 2  , 2  ]


value["MLZ"]["high"] = [3.5  , 3.5   , 3.5  , 3.5  , 3.5  ]
value["MLZ"]["low"]  = [2.5 , 2.5  , 2.5 , 2.5 , 2.5]

value["MZ"]["high"] = [3.4  , 3.4   , 3.4  , 3.4  , 3.4  ]
value["MZ"]["low"]  = [2.75 , 2.75  , 2.75 , 2.75 , 2.75]

def GetRIBIT(RIBIT_Type,time,limit):
    list_place=-1
    if(time<11):
        list_place=0
    elif(time<16):
        list_place=1
    elif(time<21):
        list_place=2
    elif(time<25):
        list_place=3
    else:
        list_place=4
    if not(RIBIT_Type in value.keys()):
        return -1
    if not(limit in value[RIBIT_Type].keys()):
        return -1
    return value[RIBIT_Type][limit][list_place]

class CRIBIT:
    def __init__(self,RIBIT_Type,time_in_years,limit,overrideValue=None):
        """Create a RIBIT objet."""
        self.RIBIT_Type = RIBIT_Type
        self.time_in_years = time_in_years
        self.limit = limit
        self.overrideValue = overrideValue
        self.MakeRIBITList()

    def GetRIBITinYear(self,YearOfMASKANTA=0):
        if(self.RIBIT_Type in ["KZ","KLZ"]):
            return GetRIBIT(self.RIBIT_Type,self.time_in_years ,self.limit)
        else:
            RIBIT= GetRIBIT(self.RIBIT_Type,self.time_in_years ,self.limit)
            RIMIT_change_from_delta=(0.5)*int(YearOfMASKANTA/5)
            return RIBIT+RIMIT_change_from_delta

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

        #print("Value is month {} {}".format(len(self.GetRIBIT(False)),self.GetRIBIT(False)))
    def GetRIBIT_Type(self):
        return self.RIBIT_Type
    def GetRIBIT_limit(self):
        return self.limit
    def UseMadad(self):
        if(self.RIBIT_Type in ["MLZ","KLZ"]):
            print("not using madad")
            return False
        return True




class CMADAD:
    """MADAD class."""

    def __init__(self,madad_number):
        """Create a MADA objet."""
        self._vlaues=[madad_number/12]*(12*30)
        self._vlauesyear=[madad_number]*(30)
    def GetMadad(self,month):
        return self._vlaues[month]

    def GetMadad_list(self):
        return self._vlaues
    def GetMadad_print(self):
        str_="Madad\nconstent of %{} per year\n".format(self._vlauesyear[0])
        print(str_)
