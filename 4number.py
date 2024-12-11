#如何使用數字，數字的用法
print(8+5)
print(8-5)
print(8*5)
print(8/5)
print(8//5)#取整數

print((8+8)*5)#未括號會先乘除後加減

number = 8
print(number*5)
print(number%5)#8除以5取餘數

print("會印出數字" + str(number))

number = -8
print(abs(number))#取絕對值
print(pow(2,4))#pow(x,y)是x的y次方
print(max(2,4,5,8,100,101))#回傳最大的數
print(min(2,4,5,8,100,101))#回傳最小的數
print(round(4.4))#四捨五入

from math import * #需匯入此模組才能使用下列功能
print(floor(4.8))#無條件捨去
print(ceil(4.4))#無條件進位
print(sqrt(64))#開根號


