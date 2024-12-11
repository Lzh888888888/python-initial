#for迴圈
"""
for 變數 in 字串or列表:
                要重複執行的字串代碼
"""
for letter in "小明你好":#會把字一個個放入變數再分別印出來
        print(letter)

for num in [0,1,2,3,4]:
        print(num)

for num in range(100):#用range取代上一個做法(一樣從0開始算起)
        print(num)

#進階，利用def和for做出和[pow(底數,次方)]一樣的效果(number檔案第18行)
def power(base_num,pow_num):
        result = base_num
        for index in range(pow_num-1):
                result = result * base_num
        return result

print(power(5,2))
