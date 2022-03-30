class Atm(object):
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
    
    def readCardnumber(self):
        print("Cardnumber = ",self.cardnumber)
    
    def readPin(self):
        print("Pin Number = ",self.pin)
    
    cash=input(int('Cash to be with drawn: '))
    print(cash)

ATM=Atm('ATM','689 123 5555',82855)
print(ATM.cardnumber(),ATM.pin())