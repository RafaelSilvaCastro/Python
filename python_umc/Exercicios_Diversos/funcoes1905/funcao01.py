def horario():
    opc = 1
    while opc != 0:
        escolha = int(input("Digite o horario que deseja converter: "))
        minutos = int(input("Digite os minutos: "))
        if escolha == 24:
            hora = int(input("Digite o horario em 24 horas: "))  
            if hora > 12:
                hora -= 12 
            print(f"o horario em 24, em 12 horas é {hora}:{minutos}")
        elif escolha == 12:
            hora = int(input("Digite o horario em 12 horas: "))
            am = input("1 para AM, 2 para PM")
            if hora < 12 and am ==2:
                hora+=12 
            print(f"o horario em 12, em 24 horas é {hora}:{minutos}")
        opc = int(input("Digite 0 para encerrar"))
horario()


