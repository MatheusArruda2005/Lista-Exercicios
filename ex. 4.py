soma = 0 
n = int(input("\nInforme n: "))
i = 1
print(f"\nO usuário deverá informar {n} números maiores que 10:")
while i <= n:
    x = float(input(f"informe X{i}: "))
    if x > 10:
        soma = soma + x
        i = i + 1
    else:
        print("Número inválido , informe novamente")
print(f"\nSoma = {soma}\n")