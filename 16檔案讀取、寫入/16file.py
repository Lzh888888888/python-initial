#檔案讀取、寫入
'''
open("檔案路徑",mode="開啟模式")
'''
#絕對路徑 ex:C:\Users\MSI\Documents\123.txt
#相對路徑 以程式的位置做延伸 ex:123.txt

#mode="r" 讀取
#mode="w"覆寫
#mode="a" 在原先的資料後寫東西

file = open("16.txt",mode="r")#讀取

"""
把下面的指令複製到open和close之間做測試
print(file.readline())#只讀一行
print(file.readline())#第二次會接著讀出下一行

print(file.read())#讀出剩下的東西

for line in file:
    print(line)#類似readline把全部都讀取完

print(file.readlines())#把檔案內的值用列表印出來
"""
file = open("16.txt",mode="w")#覆寫
file.write("hi")

file = open("16.txt",mode="a",encoding="utf-8")#在原先的資料後寫東西#用encoding uttf-8讓中文也可以寫入
file.write("Mike")
file.write("\n你好")



file.close()#使用完檔案後要關掉，避免佔用電腦資源

with open("16.txt",mode = "a",encoding="utf-8") as file:
    file.write("\n早安")#使用這串可以省去close的指令