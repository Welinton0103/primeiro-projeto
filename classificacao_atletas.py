idade = int(input("Digite a idade do atleta: "))
if idade <= 9:
    print("Atleta Mirim")

elif idade > 9 and idade <=14:
    print("Atleta Infantil")

elif idade > 14 and idade <= 19:
    print ("Atleta Junior")

elif idade > 19 and idade <= 25:
    print ("Atleta Senior")

else:
    print ("Atleta Master")

