#/usr/bin/python

def arabic_to_roman(numero):
    valores={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    valores_m={4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
    roman=''

    if numero in valores:
        print (valores[numero])
        return valores[numero]
    elif numero in valores_m:
        print (valores_m[numero])
        return valores_m[numero]
    else:
        while numero>0:
            #print ("Numero vale: " + str(numero))
            if numero>=1000:
                roman=roman+valores[1000]
                numero-=1000
            elif numero>=500 and numero<1000:
                if numero>=900:
                    roman=roman+valores_m[900]
                    numero=numero-900
                else:
                    roman=roman+valores[500]
                    numero=numero-500
            elif numero>=100 and numero<500:
                if numero>=400:
                    roman=roman+valores_m[400]
                    numero=numero-400
                    print (numero)
                else:
                    roman=roman+valores[100]
                    numero=numero-100
            elif numero>=50 and numero<100:
                if numero>=90:
                    roman=roman+valores_m[90]
                    numero=numero-90
                else:
                    roman=roman+valores[50]
                    numero=numero-50
            elif numero>=10 and numero<50:
                if numero>40:
                    roman=roman+valores_m[40]
                    numero=numero-40
                else:
                    roman=roman+valores[10]
                    numero=numero-10
            elif numero>=5 and numero<10:
                if numero==9:
                    roman=roman+valores_m[9]
                    numero=numero-9
                else:
                    roman=roman+valores[5]
                    numero=numero-5
            elif numero>=1 and numero<5:
                if numero==4:
                    roman=roman+valores_m[4]
                    numero=numero-4
                else:
                    roman=roman+valores[1]
                    numero=numero-1
            else:
                print ('')
        # for index in range(numero):
        #     try:
        #         a=valores[numero[index]]
        #         #print (a)
        #         b=valores[numero[index+1]]
        #         #print (b)
        #         if a >= b:
        #             roman=roman+a
        #             #print ("Suma: " + str(roman))
        #         else:
        #             roman=roman-a
        #             #print ("Resta: " + str(roman))
        #     except IndexError:
        #         roman += a

        print (roman)
        #return valores[numero]  
        return roman

arabic_to_roman(485)