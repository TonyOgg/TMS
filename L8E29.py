import re

# 5

def timer(a):
    p = re.match("^(1[0-9]{3}|20[0-1][0-9]|2020)-(((0[13578])|(10|12))-"
                 "(0[1-9]|1[0-9]|2[0-9]|3[0-1])|((0[469])|(11))-"
                 "(0[1-9]|1[0-9]|2[0-9]|30]))\s"
                 "([0-1][0-9]|2[0-3]):([0-5][0-9]):[0-5][0-9]$", a)
    if p:
        return p.groups()[11]
    else:
        return 'Its not time!'


# print(timer('2019-12-31 00:00:00'))

# 6

def calc(a):
    p = re.match("^([-+]?\d+[.]?[\d+]?)\s([+-/*])\s([-+]?\d+[.]?[\d+]?)$", a)
    if p == None:
        return 'Its no calculate'
    s1 = p.groups()[0]
    s2 = p.groups()[1]
    s3 = p.groups()[2]
    if '.' in s1:
        s1 = float(s1)
    else:
        s1 = int(s1)
    if '.' in s3:
        s3 = float(s3)
    else:
        s3 = int(s3)
    if s2 == '+':
        return s1 + s3
    elif s2 == '/':
        return s1 / s3
    elif s2 == '-':
        return s1 - s3
    elif s2 == '*':
        return s1 * s3

print('Result -', calc('343 * 3.1'))