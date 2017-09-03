condicion = 'si'


while condicion=='si':
    numero = int(input('ingresa numero'))
    if numero >0:
        print 'numero positivo'
    elif numero <0:
        print 'numero negativo'
    else:
        print 'ingresas mamadas we'
    numero = input("otra vez? <si - no>")
