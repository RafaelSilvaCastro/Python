#Crie um programa em Python que simule um semáforo de trânsito. O usuário informar a cor do semáforo e logo após o programa deve exibir a mensagem correspondente a cor digitada.

cor = input("Fale a cor do semaforo: ")

#convertendo para minusculo
cor = cor.lower()

#coverter para maiusculo
cor = cor.upper()

#deixar apenas a primeira letra maiuscula
cor = cor. capitalize()

if cor == 'verde':
    print("O sinal esta verde, PODE PASSAR!")
elif cor == 'amarelo':
    print("O sinal esta amarelo, ATENÇÃO!")
elif cor == 'vermelho':
    print("O sinal esta vermelho PARE!")
else:
    print("Digite uma cor que tenha no semaforo!")
