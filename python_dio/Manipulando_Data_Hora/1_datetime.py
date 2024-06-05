from datetime import date, datetime, time

data = date(2005, 5, 19)
print(f'Rafael nasceu em {data}')

print(date.today()) # pega o dia atual

data_hora = datetime(2024, 6, 5, 10, 39, 20)
print(data_hora)

print(datetime.today()) # pega o dia e a hora atual

hora = time(10, 40, 20)
print(hora)