# coding:utf-8
import random
import time

arr = [j * random.randint(1, 100000) for j in range(1000)]

'''
复杂度为O(N^2)的方法，算法很简单。dp[i]表示在以arr[i]这个数结尾的情况下，arr[0....i]中的最大递增子序列
'''

def getdp1(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


'''
getdp函数的复杂度太高，我们尝试下将其降到O(NlogN)
我们利用二分查找的思想

我们试着用一个数组ends保存，在所有长度为i的递增序列中，最小的结尾数为ends[i-1]
初始化一个ends[]和一个int型right，并规定ends[0,...,right]为有效区，否则为无效区
遍历arr，假设当前为i，
在ends的有效区从最左边开始找，找到大于arr[i]的数，则表示arr[i]结尾的最长递增序列长度=right+1
最后还有修改ends对应的值为arr[i]，以便下次遍历


如
arr = [2, 1, 5, 3, 6, 4, 8, 9, 7]
ends[0]=arr[0]=2
right=0

i=1,ends有效区=[2]
从左开始,ends[0]>arr[1],
表示arr[i]结尾的最长递增序列长度=right+1=1,
ends[0]=arr[1]=1

i=2,ends有效区=[1]
从左开始,ends[0]<arr[2],
没有发现，最长递增序列长度=right+1=2
right++
ends[right]=arr[2]

i=3,ends有效区=[1,5]
从左开始,ends[1]>arr[3],
表示arr[i]结尾的最长递增序列长度=right+1=2,
ends[0]=arr[3]=3

i=4,ends有效区=[1,3]
....

'''


def getdp2(arr):
    n = len(arr)
    dp, ends = [0] * n, [0] * n
    ends[0], dp[0] = arr[0], 1
    right, l, r, m = 0, 0, 0, 0
    for i in range(1, n):
        l = 0
        r = right
        # 二分查找,若找不到则ends[l或r]是比arr[i]大而又最接近其的数
        # 若arr[i]比ends有效区的值都大，则l=right+1
        while l <= r:
            m = (l + r) / 2
            if arr[i] > ends[m]:
                l = m + 1
            else:
                r = m - 1

        right = max(right, l)
        ends[l] = arr[i]
        dp[i] = l + 1
    return dp


def generateLIS(arr, dp):
    n = max(dp)
    index = dp.index(n)
    lis = [0] * n
    n -= 1
    lis[n] = arr[index]

    # 从右向左
    for i in range(index, 0 - 1, -1):
        # 关键
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:
            n -= 1
            lis[n] = arr[i]
            index = i

    return lis


'''
别小看了从O(N^2)到O(NlogN)
在8000的规模下
算法1和算法2的运行时间为8.28299999237和0.0190000534058
两者相差436倍！！
'''
begin = time.time()
print generateLIS(arr, getdp1(arr))
print '-----------------------------'
print time.time() - begin

begin = time.time()
print generateLIS(arr, getdp2(arr))
print '-----------------------------'
print time.time() - begin
