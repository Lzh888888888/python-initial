#string 字串
print("Hello \nMr.White")#\n 可在字串中換行

print("hello\" Mr.White ")#\加"可在字串中顯示"

print("hello " + "Mr.White")#可用+來合併字串

phrase = "hello"
print(phrase  + "Mr.White")#利用變數加進字串內

#函式function
phrase = "Hello Mr.White"
print(phrase.upper())#利用函式將字串改變狀態(lower=變小寫,upper=變大寫)

print(phrase.isupper())#利用函式判斷字串字母是否符合函式(islower=是否全小寫,isupper=是否全大寫)

print(phrase.lower().islower())#上面綜合

print(phrase[0])#回傳字串上第幾個數(0為第一個字)

print(phrase.index("H"))#尋找字元上的位置(從0開式數)

print(phrase.replace("M","m"))#尋找且替換字元