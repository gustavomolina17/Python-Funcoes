def func ():
   global X
   X = 19 # Aqui está sendo alterado o objeto X global
   Y = X * 2
   print("X global existe dentro da função: valor = {0}".format(X))
   print("Y local existe dentro da função: valor = {0}".format(Y))

print("Inicio do Programa")
X = 10
print("X global existe fora da função: valor = {0}".format(X))
func()
print("X global alterado na função: valor = {0}".format(X))
print ("Fim do programa")


