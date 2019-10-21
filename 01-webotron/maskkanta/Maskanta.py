#!/user/bin/python
from MaskantaProgram import *
class Maskanta:
    """Maskanta class."""

    def __init__(self,limit,presetValue):
        """Create a Maskanta objet."""
        self.limit = limit
        self.presetValue= presetValue
        self._programs=[]
        self.addMadad(0)

    def _checktotalsum():
        pass

    def addMadad(self,Madad):
        self.MADAD=CMADAD(Madad)

    def AddProgram(self,RIBIT_Type,Pecent,time_in_years,ribit=None):
        ribitClass=CRIBIT(RIBIT_Type,time_in_years,self.limit,ribit)
        self._programs.append(
            MaskantaProgram("my first MaskantaProgram",self.presetValue*Pecent,ribitClass,time_in_years,self.MADAD)
        )
    def calc(self):
        #todo make sure all pescent add to PV

        for program in self._programs:
            print("-"*60)
            program.PrintSummary()







if __name__ == "__main__":

    MyMaskanta=Maskanta("low",800000)
    MyMaskanta.addMadad(1)
    MyMaskanta.AddProgram("MZ",1/3,10)
    MyMaskanta.AddProgram("PRIME",1/3,30)
    MyMaskanta.AddProgram("KLZ",1/3,20,6)
    MyMaskanta.calc()

    #MyMaskanta.PrintTable()
