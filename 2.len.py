# -*- coding: UTF-8 -*-
# 计算数组长度
# 递归实现
def arrLen(arr):
    if not arr:
        return 0
    return 1 + arrLen(arr[1:])


print arrLen([1, 2, 3, 4, 5, 6])
