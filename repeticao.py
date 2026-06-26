continuar = "s"

while continuar.lower() == "s":
    num = float(input("Digite um número: "))
    print(num % 2)
    if num % 2 == 0:
        print("PAR")
    else:
        print("ÍMPAR")

    continuar = input ("Deseja Continuar ? ")