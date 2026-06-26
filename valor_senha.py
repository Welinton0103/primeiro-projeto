senha_correta = 123456

for i in range(3):
    senha_digitada = int(input("Digite a sua senha: "))
    if senha_digitada == senha_correta:
        print("Acesso Permitido")
        break
else:
    print("ACESSO BLOQUEADO")