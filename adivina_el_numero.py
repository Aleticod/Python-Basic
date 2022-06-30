import random


def run():
  numero_aleatorio = random.randint(1, 100) 
  numero_elegido = int(input('Ingrese un numeor dle 1 al 100: '))
  contador = 1
  while numero_aleatorio != numero_elegido:
    if numero_elegido < numero_aleatorio:
      print('Busca un numero más grande')
    else:
      print('Busca un numero más pequeño')
    numero_elegido = int(input('Ingrese un número: '))
    contador += 1
  print('Ganaste')
  print(f'El numero total es: {contador}')


if __name__ == '__main__':
  run()