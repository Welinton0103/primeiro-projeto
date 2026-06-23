valor_compra = float(input("Informe o valor da sua compra: "))

if valor_compra <= 100:
    print(f"Sua compra foi de {valor_compra} e vc n teve desconto")
elif valor_compra <= 300:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f"Sua compra foi de {valor_compra} pois vc teve um desconto de {desconto} e o seu pagamento final ficou de {valor_final}")

elif valor_compra <=500:
    desconto = valor_compra * 0.01
    valor_final = valor_compra - desconto
    print(
        f"Sua compra foi de {valor_compra} pois vc teve um desconto de {desconto} e o seu pagamento final ficou de {valor_final}")

else:
    desconto = valor_compra * 0.15
    valor_final = valor_compra - desconto
    print(
        f"Sua compra foi de {valor_compra} mas vc teve um desconto de {desconto} e o seu pagamento final ficou de {valor_final}")
