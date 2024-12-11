#問答程式
from question import Question #指引入Question的class(此檔案class外的程式都不會匯入)

test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1公尺是幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是什麼顏色?\n(a) 黑色\n(b) 黃色\n(c)白色\n\n"
]#建立題目

questions = [
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"b")
]#建立答案

def run_test(questions):
    score = 0
    for question in questions:#這裡的question和questions都不是上面的變數
        i = input(question.description)#將i設為答對次數
        if i == question.answer:
            score += 1 

    print("你得到" + str(score) + "分，共" + str(len(questions)) + "題")

run_test(questions)