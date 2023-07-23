from datetime import datetime, date

#fecha actual
fecha_hoy = datetime.now()

while True:
  fecha_str = input('Ingrese fecha "aaaa/mm/dd"...: ')
  try:
    fecha = datetime.strptime(fecha_str, '%Y/%m/%d')
    fecha_str = fecha.strftime('%d-%m-%Y')
    print(f'Tu fecha de nacimiento es: {fecha_str}')
  except ValueError:
    print(" No ha ingresado una fecha correcta...")
  else:
    break

#calcular los dias
user_days = fecha_hoy - fecha
user_days = user_days.days

#obtengo los años
years = user_days // 365
print(f'tienes {years} años')