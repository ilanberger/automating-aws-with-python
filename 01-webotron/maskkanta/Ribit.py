#!/user/bin/python
#Ribit types
#PRIEM
#KVOA_LO_TZAMOD
#METANA_TZMODA

value={}
value["PRIEM"]={}
value["KVOA_LO_TZAMOD"]={}
value["METANA_TZMODA"]={}
value["PRIEM"]["high"]         = [1.75 , 1.75 ,  1.75 ,1.75  , 1.75]
value["PRIEM"]["low"]          = [0.95 , 0.95  , 0.95 ,0.95  , 1.75]
value["KVOA_LO_TZAMOD"]["high"]= [3.25 , 3.75  , 4.25 , 4.75 , 5  ]
value["KVOA_LO_TZAMOD"]["low"] = [2.5  , 3.00  , 3.75 , 4.00 , 4.5]
value["METANA_TZMODA"]["high"] = [3.4  , 3.4   , 3.4  , 3.4  , 3.4  ]
value["METANA_TZMODA"]["low"]  = [2.75 , 2.75  , 2.75 , 2.75 , 2.75]

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
