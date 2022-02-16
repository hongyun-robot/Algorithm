# -*- coding: UTF-8 -*-
# 计算数组总和

# 循环调用
# def sum(arr):
#   total = 0
#   for x in arr:
#     total += x
#   return total

# 递归调用
def arrSum(arr):
    if len(arr) <= 1:
        return arr[0]
    return arr[0] + arrSum(arr[1:len(arr)])


print(arrSum([1, 2, 3, 4, 5]))
