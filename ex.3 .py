print(f"\n" + ("-"*60))
contPar = int(0)
contImpar = int(0) 
somaPar = int(0)
qtdImpar = int(0)
while contPar < 5 and contImpar < 30:
            num = int(input("\nInsira um número inteiro positivo: "))
            if num < 0:
                   print(f"\nValor inválido, insira um número inteiro positivo !\n\n" + ("-"*60))
            if (num%2) == 0:
                print(f"\nO número {num} é par !\n")
                contPar += 1
                somaPar += num
            elif (num%2) != 0:
                print(f"\nO número {num} é ímpar !\n")
                contImpar += num
                qtdImpar += 1
print(f"\n" + ("-"*60))
print(f"\nNúmeros pares digitados: {contPar}\n\nNúmeros Impares digitados: {qtdImpar}")
print(f"\nSoma dos números pares: {somaPar}\n\nSoma dos números impares: {contImpar}")
print(f"\n" + ("-"*60))