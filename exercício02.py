soma = 0
contador = 0
while contador < 10:
        nota = float(input("Digite uma nota: "))
        if nota > 0:
            soma += nota
            contador += 1
        else:
            print("ERRO , digite o número novamente")
media = soma/contador
print(f"A média das notas é {media}")