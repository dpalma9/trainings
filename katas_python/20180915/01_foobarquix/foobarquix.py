#/usr/bin/python

def foobarquix(number):
    result=''
    for i in str(number):
        result=result + is_equal(i)
    if number%3 != 0 and number%5 != 0 and number%7 != 0:
        print (str(number) + result)    
    else:
        print (str(div_3(number)) + str(div_5(number)) + str(div_7(number)) + result)
    
def div_3(num):
    if num%3 == 0:
        return "Foo"
    else:
        return ""

def div_5(num):
    if num%5 == 0:
        return "Bar"
    else:
        return ""

def div_7(num):
    if num%7 == 0:
        return "Quix"
    else:
        return ""

def is_equal(num):
    if int(num) == 3:
        return "Foo"
    elif int(num) == 5:
        return "Bar"
    elif int(num) == 7:
        return "Quix"
    else:
        return ""

foobarquix(75)