idade = int(input("Digite sua idade: "))

if idade < 1 or idade > 120:
    print("idade invalida")
elif idade < 16:
    print("não eleitor")
elif idade >= 18 and idade <= 65:
    print("eleitor obrigatorio")
else:
    print("eleitor facultativo")