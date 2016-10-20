# coding:utf-8
'''
给定数组arr[i]==k代表可以从位置i向右条1~k个距离。返回最少跳几次能跳到arr最后的位置上。
如：arr = [3, 2, 3, 1, 1, 4]
arr[0] = 3,选择跳到2;arr[2] = 3,可以跳到最后，所以返回2。

dp[i]表示：从i位置开始跳到arr最后的位置上最少需要多少步。
dp[aim]=0除外
'''


def jump(l):
    length = len(l)
    aim = length - 1
    dp = [0] * length

    for i in range(aim - 1, 0 - 1, -1):
        dp[i] = min([dp[i + x] + 1 for x in range(1, l[i] + 1)])

    return dp[0]


test = [3, 2, 3, 1, 1, 4]

print jump(test)
