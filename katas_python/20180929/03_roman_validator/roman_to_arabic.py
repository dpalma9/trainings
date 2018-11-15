#/usr/bin/python

def roman_to_arabic(numero):
    basic={"I":3,"X":3,"C":3,"M":3}
    extend={"V":1,"L":1,"D":1}
    valores={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    arabe=0
    temp=''

    for index in range(len(numero)):
        #print(indice)
        #print(nunero[indice])
        try:
            a=valores[numero[index]]
            #print (a)
            b=valores[numero[index+1]]
            #print (b)
            if a >= b:
                arabe=arabe+a
                #print ("Suma: " + str(arabe))
            else:
                arabe=arabe-a
                #print ("Resta: " + str(arabe))
        except IndexError:
            arabe += a
    # for i in valores:
    #     for j in numero:
    #         if i==j:s
    #             arabe=arabe+valores[i]

    print (arabe)
    return arabe   

roman_to_arabic('IV')