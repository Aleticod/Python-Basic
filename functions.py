def conversation(mensaje):
  print('Hola')
  print('Cómo estás')
  print(mensaje)
  print('Adiós')


option = int(input('Elige una opcion (1, 2, 3): '))

if option == 1:
  conversation('Elegiste la opción 1')
elif option == 2:
  conversation('Elegiste la opción 2')
elif option == 3:
  conversation('Elegiste la opción 3')
else:
  print('Ingrese la opción correcta')