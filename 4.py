for i in range(0,10):
    dados = int(input("Digite um número: "))
    impar = [i for i in range(10) if  i % 2]
    par = [i for i in range(10) if not i % 2]
print("numeros impares: ",impar)
print("numeros pares:",par)