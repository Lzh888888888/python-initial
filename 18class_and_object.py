#類別cless，物件object
#建立類似手機型號的類別
class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = Phone("ios",123,True)#把手機型號輸入到phone1裡，稱為建立物件(object)
print(phone1.os)#單獨印出手機的版本
print(phone1.number)
print(phone1.is_waterproof)

phone2 = Phone("andriod",456,False)#可創件很多種物件
print(phone2.os)