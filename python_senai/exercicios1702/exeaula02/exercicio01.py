#Crie um programa em Python que peça a temperatura em graus Celsius e o programa deve exibir a temperatura em graus Fahrenheit.
print("Escreva sua temperatura em Celsius para converter para fahrenheit")

celsius = int(input("Digite sua temperatura em celsius: "))

fahrenheit = (((celsius) * 9/5) + 32)

print("Sua temperatura em graus Celsius e: ",celsius,"°C, convertida para fahrenheit e:",fahrenheit,"°F.")