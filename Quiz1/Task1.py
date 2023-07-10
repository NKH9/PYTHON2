import random as rd
Digit_list = [[rd.randint(1, 200), rd.randint(1, 200), rd.randint(1, 200)] for i in range(10)]

class tolperdaTrapecia: 
    def __init__(self,digit):
        self.zeda = digit[0]
        self.kveda =  digit[1]
        self.simagle =  digit[2]
    def __str__(self):
        return ("zeda fudze: "+ str(self.zeda)+'\n'+("kveda fudze : "+ str(self.kveda))+'\n'+ ("simagle : "+ str(self.simagle)) )

    def partobi(self):
        return (self.zeda+self.kveda)*self.simagle/2
    def __le__ (self,other):
        return self.partobi()<=other.partobi()
    def __eq__ (self,other):
        return self.partobi()==other.partobi()
    def __more__(self,other):
        return self.partobi()>=other.partobi()

class martkutxedi(tolperdaTrapecia):
    def __init__(self,digit):
        super().__init__(digit)
        self.simagle = None
    def __str__(self):
        return ("zeda fudze: "+ str(self.zeda)+'\n'+("kveda fudze : "+ str(self.kveda))+'\n')
    def partobi(self):
        return (  self.zeda*self.kveda)

class kvadrati(martkutxedi):
    def __init__(self,digit):
        super().__init__(digit)
        self.kveda = None
    def __str__(self):
        return ("gverdi:  "+ str(self.zeda))
    def partobi(self):
        return (  self.zeda**2)
    
trap1=tolperdaTrapecia(Digit_list[0])
trap2=tolperdaTrapecia(Digit_list[1])
# print(trap1.partobi())
# print(trap2.partobi())
# print(trap2>=trap1)

mart1=martkutxedi(Digit_list[0])
mart2=martkutxedi(Digit_list[1])
# print(mart1.partobi())
# print(mart2.partobi())
# print(mart1==mart2)

kvad1=kvadrati(Digit_list[0])
kvad2=kvadrati(Digit_list[1])
# print(kvad1)
# print(kvad2)
# print(kvad1.partobi())
# print(kvad2.partobi())
# print(kvad1<=kvad2)
    
