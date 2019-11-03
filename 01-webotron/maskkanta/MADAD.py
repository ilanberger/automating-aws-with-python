class CMADAD:
    """MADAD class."""

    def __init__(self,madad_number,printMadad=False):
        """Create a MADA objet."""
        self._vlaues=[madad_number/12]*(12*30)
        self._vlauesyear=[madad_number]*(30)
        if(printMadad):
            self.GetMadad_print()
    def GetMadad(self,month):
        return self._vlaues[month]

    def GetMadad_list(self):
        return self._vlaues
    def GetMadadYear_list(self):
        year_list=[]
        sum = 0
        for i in range(len(self._vlaues)):
            sum += self._vlaues[i]
            if((i+1)%12 == 0):
                year_list.append(sum)
                sum=0

        return year_list
    def GetMadad_print(self):
        str_="Madad\nconstent of %{} per year\n".format(self._vlauesyear[0])
        print(str_)
