# coding:utf-8
'''
'A-1BC--12'=-1+12=11
'A1CD2E33'=1+2+33=36
'''

import re


def numSum(string):
    num_list = re.findall('(-*\d+)', string)
    res = 0
    for each in num_list:
        # 对于'--33'，int会出错，所以eval
        res += eval(each)
    return res


def numSum2(string):
    neg, now, res = 0, 1, 0
    result = []
    # + '?' 完全就是为了获得最后一次循环
    for i in string + '?':
        if i == '-':
            neg += 1
        if i in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            res = int(i) + res * now
            now *= 10
        elif i != '-':
            if neg % 2 != 0:
                res = -res
            result.append(res)
            res = 0
            neg, now = 0, 1

    return sum(result)


test = '-1A1CD-2E--33'

print numSum2(test)
