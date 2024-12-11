#模組module的使用(匯入tool.py)
#1.匯入自己的程式模組

import tool

print(tool.name)

print(tool.max_num(2,3,88))

#2.使用內建模組
import token
import sys
print(sys.path)#尋找內建模組位置

#3.下載外部模組(pip套件管理工具)
'''
在終端機輸入
pip install (模組名稱)
在這裡可以用
import (模組名稱) as (想要用的代稱)
就可以縮短模組的名稱放在指令上。
'''