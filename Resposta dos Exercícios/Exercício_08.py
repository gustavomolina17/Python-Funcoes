# A função acima nada mais é que uma pesquisa linear na lista de entrada. Em outras palavras, percorremos a lista linearmente,
# elemento por elemento, e verificamos se cada o elemento corrente é o que estamos procurando. Caso seja, retornamos True.
# Caso o laço for termine e o elemento não tenha sido encontrado, retornamos False, pois percorremos toda a lista e não encontramos
#  o elemento procurado.

def pesquisa_elemento1(numeros, numero_procurado):
    for numero in numeros:
      if numero == numero_procurado:
          return True
      else:
          return False

print(pesquisa_elemento1([1, 10, 20, 30, 50, 100], 40))
