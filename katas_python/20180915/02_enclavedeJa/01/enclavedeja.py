#/usr/bin/python

def get_price(numero):
    precio=5
    num=len(numero)
    if (num > 2 and num <= 4):
        return desc_2(num)
    elif num > 4:
        return desc_4(num)
    else:
        return num*precio

def desc_2(num):
    total=num*5
    desc=total*0.1
    return total-desc

def desc_4(num):    
    total=num*5
    desc=total*0.2
    return total-desc
