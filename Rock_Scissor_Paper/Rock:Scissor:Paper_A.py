import random 

def run():
    pc_age = random.randint(1,100)
    name = input('What is your name? ')
    user_age = int(input('What is your age? '))
    while pc_age != user_age:
        if pc_age > user_age:
            print(f'Pc is older than {name}')
        elif user_age > pc_age:
            print(f'{name} is older than Pc')
        else:
            print('You have the same age')
        name = input('Plase insert a new name? ')
        user_age = int(input('Plase insert a new age: '))
        print('Thank you and wellcome again')

if __name__ == '__main__':
    run()


def run():
    number_a = int(input('Please type a number: '))
    number_b = int(input('Please type a number: '))

    operation = number_a / number_b

    if operation % 2 == 0:
        print(f'El resultado de la divicion de los numeros ingresados {number_a} / {number_b} es {operation} y es par')
    else:
        print(f'El resultado de la divicion de los numeros ingresados {number_a} / {number_b} es {operation} y es impar')

if __name__ == '__main__':
    run()



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = int(input('Pls insert a number: '))
    
def run():
    for i in a:
        if i < 5:
            print(f'list {i}')


if __name__ == '__main__':
    run()


num = int(input('Pls write a number: '))
list_range = list(range(1,num+1))

run = []

for i in list_range:
    if num % i == 0:
        run.append(i)

print(run)            

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for num in b:
    if num in a:
        print(f'chao {num}')
        c.append(num)

print(c)



def palindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palindromo = palabra[::-1]
    if palabra == palindromo:
        return True
    else:
        return False


def run():
    palabra = input('Por favor ingresa una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def run():
    for i in a:
        if i % 2 == 0:
            print(f'los numero pares son: {i}')
            continue 
        else:
            if i % 3 == 0:
                print(f'los numeros impares son: {i}')

if __name__ == '__main__':
    run()

PIEDRA PAPEL O TIJERA

menu = '''

Elige una opcion:
1- rock
2- scissors
3- paper

'''

import random

user = int(input(menu))
print(f'Elegiste {user}')
mac = random.randint(1, 3)
print(f'mac eligio {mac}')

if user == mac:
        print('Han empatado') 
while user != mac:
    if user == 2 & mac == 1:
        print('Ha ganado la mac con piedra')
    elif user == 2 & mac == 2:
        print('Ha ganado la mac con tijera')
    elif user == 1 & mac == 3:
        print('Ha ganado la mac con papel')
    elif user >= 4:
        print(f'Por favor ingresa una opcion valida {menu}')    
    else:
        print('Has ganado ***FELIZITACIONES***')    
    break
print('Gracias por participar')