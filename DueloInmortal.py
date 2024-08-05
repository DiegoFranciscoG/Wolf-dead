import random
import time

def simular_batalla(vida_deadpool, vida_wolverine):
    turno = 1
    
    while vida_deadpool > 0 and vida_wolverine > 0:
        print(f"\nTurno {turno}:")
        
        # Determinar si Deadpool evita el ataque
        evade_deadpool = random.random() < 0.25
        # Determinar si Wolverine evita el ataque
        evade_wolverine = random.random() < 0.20
        
        # Deadpool ataca a Wolverine
        if not evade_wolverine:
            danio_deadpool = random.randint(10, 100)
            if danio_deadpool == 100:
                print("Deadpool golpea a Wolverine con un daño máximo de 100!")
                print("Wolverine debe regenerarse y no puede atacar este turno.")
                vida_wolverine -= danio_deadpool
                turno += 1
                continue
            else:
                vida_wolverine -= danio_deadpool
                print(f"Deadpool ataca a Wolverine con {danio_deadpool} puntos de daño.")
        else:
            print("Wolverine evita el ataque de Deadpool.")
        
        # Wolverine ataca a Deadpool
        if not evade_deadpool:
            danio_wolverine = random.randint(10, 120)
            if danio_wolverine == 120:
                print("Wolverine golpea a Deadpool con un daño máximo de 120!")
                print("Deadpool debe regenerarse y no puede atacar este turno.")
                vida_deadpool -= danio_wolverine
                turno += 1
                continue
            else:
                vida_deadpool -= danio_wolverine
                print(f"Wolverine ataca a Deadpool con {danio_wolverine} puntos de daño.")
        else:
            print("Deadpool evita el ataque de Wolverine.")
        
        # Mostrar la vida restante de cada personaje
        print(f"Vida de Deadpool: {vida_deadpool}")
        print(f"Vida de Wolverine: {vida_wolverine}")
        
        # Incrementar el turno
        turno += 1
        
        # Pausa de 1 segundo entre turnos
        time.sleep(1)
    
    # Determinar el ganador
    if vida_deadpool <= 0 and vida_wolverine <= 0:
        print("\n¡La batalla termina en empate!")
    elif vida_deadpool <= 0:
        print("\n¡Wolverine es el ganador!")
    else:
        print("\n¡Deadpool es el ganador!")

if __name__ == "__main__":
    # Solicitar al usuario la vida inicial de cada personaje
    vida_deadpool = int(input("Ingrese la vida inicial de Deadpool: "))
    vida_wolverine = int(input("Ingrese la vida inicial de Wolverine: "))
    
    # Simular la batalla
    simular_batalla(vida_deadpool, vida_wolverine)
