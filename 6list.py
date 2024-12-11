#列表list、列表的用法
scores = [90,70,60,50,80]
friends = ["小黑","小黃","小綠"]
things = [30,"小黑",True]
print(scores)
print(friends)
print(things)
print(scores[-1])#python列表或字串都是從0開始算，負號是從後面的元素開始讀取
print(scores[1:4])#從第1位(第二個元素)開始取，但不包含第4位
print(scores[1:])#從第1個元素取到結束
print(scores[:4])#從最初開始取，取到第四位前(不包含第四位)

phrase = "Hello Mr.White"#換成英文字串也是相同概念
print(phrase[0:5])
print(phrase[6:])

scores[0] = 30#修改字列表第0位的值
print(scores)

scores.extend(friends)#將scores列表後面加上friends列表內的元素
print(scores)

list = [10,20,30,40,50]
list.append(30)#將list列表後面加一個元素為30
print(list)
list.insert(2,80)#將list列表第二位(第三個元素)加一個元素為80，原第三個元素之後都往後移
print(list)
list.remove(40)#將列表裡有40的元素移除
print(list)
list.clear()#清除列表上全部的元素
print(list)

list = [10,90,80,50,30]
list.pop()#清除列表上最後一個的元素
print(list)
list.sort()#將列表上的元素由小到大排列
print(list)
list.reverse()#將列表上的元素顛倒排列
print(list)

print(list.index(50))#尋找50值在第幾位
print(list.count(50))#尋找50值有幾個