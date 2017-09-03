def funcion1():
    print('Salut tout le monde')
    print('nice to meet you')
    print('que onda weyes')

funcion1()
####################################
def funcion2(cadena,numero):
    print(cadena*numero)

funcion2('Toluca ',10)
#####################################
def funcion3(cadena,default=8):
    print(cadena * default)

funcion3('Pachuca ',11)
######################################
def cuadro1(num):
    print(num*num)

cuadro1(9)

def cuadro2():
    n = int(input('mete numero'))
    cuadro1(n)

cuadro2()
##########################################
def cuadro3():
    n = int(input('choose a number'))
    return n*n

cuadrin = cuadro3()
print(cuadrin)
