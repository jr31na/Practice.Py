import random

is_game = True

def quien_gano(user,mac):
    if user == 1 and mac == 3:
        print('Ha ganado la mac con papel')
    elif user == 2 and mac == 3:
        print('Ha ganado la mac con tijera')
    elif user == 3 and mac == 1:
        print('Ha ganado la mac con piedra')
    elif user == mac:
        print('Han empatado')  
    elif user >= 4 or mac >=4:
        print('Error, ingresa una opcion valida')
    else:
        print(f'Has ganado 🤩🤩🤩 FELIZITACIONES 🤩🤩🤩 la mac perdio con {mac}')    


def seguir_jugando(respuesta):
    if respuesta == 'si':
        return True
    else:
        return False


bienvenida = """ 
B I E N V E N I D O S

            T O D O S . . . 
 
                      A . . . 

██████╗ ██╗███████╗██████╗ ██████╗  █████╗ 
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
██████╔╝██║█████╗  ██║  ██║██████╔╝███████║
██╔═══╝ ██║██╔══╝  ██║  ██║██╔══██╗██╔══██║
██║     ██║███████╗██████╔╝██║  ██║██║  ██║
╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

  ██████╗  █████╗ ██████╗ ███████╗██╗     
  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║     
  ██████╔╝███████║██████╔╝█████╗  ██║     
  ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██║     
  ██║     ██║  ██║██║     ███████╗███████╗
  ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝

                   ██████╗ 
                  ██╔═══██╗
                  ██║   ██║
                  ██║   ██║
                  ╚██████╔╝

████████╗██╗     ██╗███████╗██████╗  █████╗ 
╚══██╔══╝██║     ██║██╔════╝██╔══██╗██╔══██╗
   ██║   ██║     ██║█████╗  ██████╔╝███████║
   ██║   ██║██   ██║██╔══╝  ██╔══██╗██╔══██║
   ██║   ██║╚█████╔╝███████╗██║  ██║██║  ██║
   ╚═╝   ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
________________________________________________

            -= SELECT TO START =-

1- piedra
2- papel
3- tijera

"""

print(bienvenida)

while is_game:
    mac = random.randint(1,3)
    user = int(input(bienvenida))

    print(quien_gano(user, mac))
    is_game = seguir_jugando(input('Quieres seguir jugando: '))