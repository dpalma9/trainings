#/usr/bin/python

from arabic_to_roman import arabic_to_roman
from roman_to_arabic import roman_to_arabic

def roman_validator(numero):
    original=numero

    arabe=roman_to_arabic(numero)
    romano=arabic_to_roman(arabe)

    if romano==original:
        return True
    else:
        return False