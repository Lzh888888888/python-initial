#猜數字遊戲(限制次數版)
secret_num = 77
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False#偵測次數有沒有超過三次

while secret_num != guess and not(out_of_limit):
        guess_count += 1 
        if guess_count <= guess_limit:
                guess =int( input("請輸入數字:"))
                if guess > secret_num:
                        print("小一點")
                elif guess < secret_num:
                        print("大一點")
        else:
                        out_of_limit = True

if out_of_limit:
        print("你輸了")
else:
        print("你贏了")