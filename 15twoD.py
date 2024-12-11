#二維列表、巢狀迴圈
#row = 行
#column = 列


nums = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [9]
]

print(nums[0][1])#第一個中括號試行、第二個是列(一樣從0開始算)

for row in nums:#把四行列表分別放入row裡面
        for col in row:#把每一行的值代到col裡面
                print(col)


