#物件函式
#前面類別程式與18相同
class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
    
    def is_ios(self):#在class裡面寫入其他的函式使用(此為確認使否為ios)
        if self.os == "ios":
            return True
        else:
            return False
        
    def add(self,number1,number2):
        return number1 + number2

phone1 = Phone("ios",123,True)
print(phone1.is_ios())
print(phone1.add(5,6))