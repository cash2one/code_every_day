# coding:utf-8
'''
str1='123',str2='231'   True
str1='1123',str2='2231'   False
'''

def isDeformation(string1, string2):
    str_d = {}
    for i in string1:
        if i not in str_d:
            str_d[i] = 1
        else:
            str_d[i] += 1

    for i in string2:
        if i in str_d:
            str_d[i] -= 1

    for k, v in str_d.items():
        if v != 0:
            return False

    return True


string1 = '2313333'
string2 = '3312333'

print isDeformation(string1, string2)
