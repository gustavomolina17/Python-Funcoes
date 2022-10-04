def verificaPositivo(valor):
    if (valor > 0):
        return 'P'
    elif (valor==0):
        return '0'
    else:
        return 'N'

numero = int(input('Informe um numero: '))
print ("Resultado: ", verificaPositivo(numero))