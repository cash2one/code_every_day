# coding:utf-8
'''
小东所在公司要发年终奖，而小东恰好获得了最高福利，他要在公司年会上参与一个抽奖游戏，游戏在一个6*6的棋盘上进行，上面放着36个价值不等的礼物，每个小的棋盘上面放置着一个礼物，他需要从左上角开始游戏，每次只能向下或者向右移动一步，到达右下角停止，一路上的格子里的礼物小东都能拿到，请设计一个算法使小东拿到价值最高的礼物。

给定一个6*6的矩阵board，其中每个元素为对应格子的礼物价值,左上角为[0,0],请返回能获得的最大价值，保证每个礼物价值大于100小于1000。

'''

test = [
    [1, 3, 5, 9],
    [8, 1, 3, 4],
    [5, 0, 6, 1],
    [8, 8, 4, 0]
]


def getMost(border):
    each_path = []
    col = len(border[0])
    row = len(border)

    def most_momey(i=0, j=0, the_sum=0):
        # 向右走
        if j < col - 1:
            most_momey(i, j + 1, border[i][j] + the_sum)
        # 向左走
        if i < row - 1:
            most_momey(i + 1, j, border[i][j] + the_sum)

        # 到达右下角
        if i == row - 1 and j == col - 1:
            each_path.append(the_sum + border[i][j])
        else:
            return

    most_momey()
    return max(each_path)


# 动态规划求解
'''
根据题意，从(0,0)到(i,j)的路径必然经过位置(i-1,j)或(i,j-1)。
dp[n][m] = max(dp[n - 1][m], dp[n][m - 1]) + border[n][m]
的含义也就是比较从(0,0)位置开始，经过(i-1,j)位置最终到达(i,j)的最大路径和经过(i,j-1)位置最终到达(i,j)的最大路径之间，哪条路径的路径和最大

就题目中的例子，我们先生成第一行和第一列的dp，也就是
1   4   9   18
9
14
22
然后从(1,1)开始，计算从(0,0)到自己的最大路径和，计算的时候只是比较上边和左边哪个最大。

时间复杂度O(M*N)，空间复杂度O(M*N)

'''


def getMost_dp(border):
    col = len(border[0])
    row = len(border)
    # dp标识走到(i,j)位置的最大路径和
    dp = [[0] * col for i in range(row)]
    dp[0][0] = border[0][0]

    # 求出dp[0][1]-dp[0][col]
    for i in range(1, col):
        dp[0][i] = dp[0][i - 1] + border[0][i]

    # 求出dp[1][0]-dp[row][0]
    for j in range(1, row):
        dp[j][0] = dp[j - 1][0] + border[j][0]

    for n in range(1, row):
        for m in range(1, col):
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1]) + border[n][m]

    return dp[row - 1][col - 1]


# print getMost_dp(test)

'''
空间压缩

上述的代码，空间复杂度为O(M*N)，我们还可以对其进行空间压缩，使复杂度降到O(min{M,N})

就上面的例子，我们先生成一个arr[min(rol,row)]数组。在这个例子里面是arr[4]
我们根据row和col的数量进行滚动，row多的话，向下滚动；否则向右滚动。
我们这里向下滚动。
所以求出arr[i] = arr[i - 1] + border[0][i] = [1,4,9,18]
然后我们向下滚动i=1。
arr[0] = arr[0] + border[i][0] = 9
arr[1] = max(arr[1 - 1], arr[1]) + border[i][1]    # arr[1 - 1], arr[1]分别代表border[i][1]的左边和上边
arr[2] = max(arr[2 - 1], arr[1]) + border[i][2]
....
arr[j] = max(arr[j - 1], arr[j]) + border[i][j]


没有优化之前，取得某个位置动态规划值的过程是在矩阵中进行两次寻址，优化后，这一过程只需要一次寻址。
'''


def getMost_dp2(border):
    col = len(border[0])
    row = len(border)
    more = max(col, row)
    less = min(col, row)
    rowmore = bool(more == len(border))

    arr = [0] * less
    arr[0] = border[0][0]

    # row多的话，向下滚动；否则向右滚动
    for i in range(1, less):
        arr[i] = arr[i - 1] + border[0][i] if rowmore else border[i][0]

    for i in range(1, more):
        arr[0] = arr[0] + border[i][0] if rowmore else border[0][i]
        for j in range(1, less):
            arr[j] = max(arr[j - 1], arr[j]) + border[i][j] if rowmore else border[j][i]

    return arr[less-1]