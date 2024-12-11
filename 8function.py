#函式function
def hello():
        print("hello")
hello()

def hello(name,age):
        print("hello" + name + "，你今年" + age + "歲")
hello("小王","3")#數字要用括號表字串，如果沒有會被認定是數字，數字無法與字串相加會出現error

def add(num1,num2):
        return num1+num2#return是將下面的add(2,3)變成5，因此value變數也會變成5
value = add(2,3)
print(value)

def lalala(a,b):
        print( a+b)#return是將下面的add(2,3)變成5，因此value變數也會變成5
ans=  lalala(3,4)
print(ans)
'''
執行後會出現:
7
None
是因為python會把上面的值加總後印出
且如果變數沒有return值，會預設成None
所以函式全部執行完後，ans變數會變成None並在印出一次。
(如果直接打lalala(3,4)或利用return就不會在回傳一次None......吧?)
'''
#如果函數執行到return，就會直接停止函數內的指令，所以return底下再接下去輸入指令就沒用了
