import random
from turtle import up


def password_generator():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    number = ['1', '2', '3', '4', '5', '6', '7']
    simbol = ['#', '%', '@', '&']
    caracteres =uppercase + lowercase + number + simbol

    password = []
    for i in range(12):
        char = random.choice(caracteres)
        password.append(char)
    
    password = ''.join(password)
    return password

def run():
    password = password_generator()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()