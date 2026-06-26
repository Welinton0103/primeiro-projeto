maiores = 0
menores = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i} :"))
    idade = 2026 - ano_nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f"Os maiiores de idade sao {maiores} e os menores de idade sao {menores}")
