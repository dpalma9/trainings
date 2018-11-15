#/usr/bin/python

def get_price(series):

    temp0=0
    temp1=0
    temp2=0
    temp3=0
    temp4=0

    precio_total=0

    for i in series:
        if i == 0:
            temp0=temp0+1
        elif i == 1:
            temp1=temp1+1
        elif i == 2:
            temp2=temp2+1
        elif i == 3:
            temp3=temp3+1
        elif i == 4:
            temp4=temp4+1
        else:
            print ("Error. Esta temporada no esta.")
    
    total = {0:temp0, 1:temp1, 2:temp2, 3:temp3, 4:temp4}
    aux = {0:temp0, 1:temp1, 2:temp2, 3:temp3, 4:temp4}

    precio=descuento(aux)
    print ("Primer descuento es: " + str(precio))
    precio_total=precio_total+precio
    while precio != 0:
        precio=descuento(aux)
        print ("Precio es: " + str(precio))
        precio_total=precio_total+precio

    print ("Precio final es: " + str(precio_total))
    return round(precio_total,2)

def descuento(aux):
    cont=0
    precio=0
    
    for i in aux:
        if i==0 and aux[i]>0:
            precio=precio+3
        elif i==1 and aux[i]>0:
            precio=precio+3.5
        elif i==2 and aux[i]>0:
            precio=precio+4
        elif i==3 and aux[i]>0:
            precio=precio+4.5
        elif i==4 and aux[i]>0:
            precio=precio+5
        else:
            print ("")

        if aux[i]>0:
            cont=cont+1
            aux[i]=aux[i]-1

    if cont<3:
        #0%
        return precio
    if cont==3:
        #10%
        return precio*0.9

    elif cont==4:
        #20%
        return precio*0.8
    elif cont==5:
        #30%
        return precio*0.7
    else:
        #llamar a función de nuevo
        return 99

#get_price([0,1])
#get_price([0,1,2,3,1,2,3])
#get_price([0,1,2,3,3])
#get_price([0, 0, 0, 0])
get_price([0,1,2])