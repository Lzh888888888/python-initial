#猜數字遊戲
secret_num = 77
guess = None

while secret_num != guess:#答案不等於自己選的，就繼續執行迴圈
        guess =int( input("請輸入數字:"))#用int把數字字元變數整數
        if guess > secret_num:
                print("小一點")
        elif guess < secret_num:
                print("大一點")


print("你贏了")