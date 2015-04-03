"""
Copyright Lukasz Szybalski
VIN Vehicle information number checker, and now a decoder.
"""
import os
import csv
class Vin(object):
    """Vin class object"""
    def __new__(cls, *p, **k):
        inst = object.__new__(cls)
        #Initialize code,year
        inst._yeardata_alpha={}
        inst._yeardata_num={}
        #Passenger Auto
        with open(os.path.join(os.path.dirname(__file__),'year.csv')) as csvyear:
            reader=csv.DictReader(csvyear)   
            for row in reader:
                if int(row['year'])<2010:
                    inst._yeardata_num[row['code']]=row['year']
                else:
                    inst._yeardata_alpha[row['code']]=row['year']
        #Initilize wmi,manufacturer
        inst._wmidata={}
        with open(os.path.join(os.path.dirname(__file__),'wmi.csv')) as csvwmi:
            reader=csv.DictReader(csvwmi)   
            for row in reader:
                inst._wmidata[row['wmi']]=row['manufacturer']
        return inst
    def __init__(self,vin=None):
    #def decode(self,vin=None):
        #Decoding
        self.vin = (str(vin).upper())
        self.check = check_vin(self.vin)
        if len(self.vin)>2:
            self.wmi = self._vin_wmi(self.vin[:3])
        if len(self.vin)>9:
            self.year = self._vin_year(self.vin[9],self.vin[6])
    def _vin_year(self,position10=None,position7=None):
        """Input: position 10 of vin number. Output: Four digit year
        http://www.gpo.gov/fdsys/granule/CFR-2011-title49-vol6/CFR-2011-title49-vol6-part565
        """
        if not position10 or len(position10)!=1:
            return False
        else:
            try:
                if str(position7).isalpha():
                    return self._yeardata_alpha[position10]
                else:
                    return self._yeardata_num[position10]
            except KeyError:
                return False
    def _vin_wmi(self,position123=None):
        """Input: position 123 of vin number. Output: Manufacturer"""
        if not position123 or len(position123)!=3:
            return False
        else:
            try:
                return self._wmidata[position123]
            except KeyError:
                return False
                
                

def check_vin(vin=None):
    """Vehicle Information Number. This will return whether the entered vin number is authentic/correct.
    Example:
    import vin
    vin.check_vin(my_vin_number)
    """
    if not vin:
        return False
    vin=str(vin).strip()
    if len(vin) != 17:
        return False
    else:
        converted=[]
        vin=vin.upper()
        for i in range(len(vin)):
            converted.insert(i,_convert_vin(vin[i]))
        multiplier=[8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
        add=0
        for i in range(len(vin)):
            add+=(converted[i]*multiplier[i])
        final= (add%11)
        if final ==10:
            final='X'
        if str(final)==vin[8]:
            return True
        else:
            return False
        

def _convert_vin(field):
    """Stores alpha to number conversion as defined by the vehicle information number standard.
    """
    if not field.isalpha():
        return int(field)
    else:
        if field == "A":
            return 1
        elif field=="B":
            return 2    
        elif field=="C":
            return 3    
        elif field=="D":
            return 4    
        elif field=="E":
            return 5    
        elif field=="F":
            return 6    
        elif field=="G":
            return 7    
        elif field=="H":
            return 8    
        elif field=="I":
            return 9    
        elif field=="J":
            return 1    
        elif field=="K":
            return 2    
        elif field=="L":
            return 3    
        elif field=="M":
            return 4    
        elif field=="N":
            return 5    
        elif field=="O":
            return 6    
        elif field=="P":
            return 7    
        elif field=="Q":
            return 8    
        elif field=="R":
            return 9    
        elif field=="S":
            return 2    
        elif field=="T":
            return 3    
        elif field=="U":
            return 4    
        elif field=="V":
            return 5    
        elif field=="W":
            return 6    
        elif field=="X":
            return 7    
        elif field=="Y":
            return 8    
        elif field=="Z":
            return 9
        else:
            return False


    
def decode_vin(vin=None):
    """Vehicle Information Number. This will return object that will contain additional information. 
    Example:
    import vin
    vin.check_vin(my_vin_number)
    decodedvin=vin.decode_vin('my_vin_number')
    decodedvin.year
    decodedvin.wmi_code
    decodedvin.manufacturer
    decodedvin.country
    """
    if not vin:
       return False
    if check_vin(vin):
        return Vin(vin)
    else: 
        #special case
        return Vin(vin)
