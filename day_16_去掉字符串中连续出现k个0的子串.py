# coding:utf-8

'''
str='A00B',k=2,返回'AB'
str='A0000B000',k=3,返回'A0000B'
'''


def removeKZeros(string, k):
    l = 0
    length = len(string)
    result = []
    res = ''

    for i, j in enumerate(string):

        if j == '0':
            l += 1
        else:
            result.append((l, i))
            l = 0

        if i == length - 1:
            result.append((l, i + 1))

    for count, index in result[1:]:
        if count == k:
            res = string[:index - count] + string[index:]

    return res


test = 'A0000B000C0'

print removeKZeros(test, 4)
