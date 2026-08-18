## Calcular Segundos 
total = int(input("Digite a quantidade de segundos:  "))
horas = total // 3600
minutos = (total % 3600) // 60
segundos = (total % 60)
print(f"{horas} horas, {minutos} minutos, {segundos} segundos")