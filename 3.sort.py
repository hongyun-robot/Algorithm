# -*- coding: UTF-8 -*-
# 快速排序算法
# [4, 2, 6]
# 基准值为 4
# 小于基准值的数组为 [2]
# 大于j
def quicksort(arr):
    # 基线条件 当一个数组为一个或没有元素时就是正确的排序
    if len(arr) < 2:
        return arr
    # 基准值
    poivt = arr[0]
    # 小于基准值的数组
    less_arr = [i for i in arr[1:] if i <= poivt]
    # 大于基准值的数组
    greater_arr = [i for i in arr[1:] if i > poivt]
    return quicksort(less_arr) + [poivt] + quicksort(greater_arr)


print quicksort([2, 1, 4, 6, 8])
