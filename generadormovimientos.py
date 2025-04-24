import random

# Lista de comentarios en ciclo
ghosts = ['PAC', 'BLINKY', 'PINKY', 'INKY', 'CLYDE']

for i in range(1, 200):
    movimiento = random.randint(1, 4)
    # Selecciona el comentario según la iteración (i-1) módulo el número de ghosts
    comentario = ghosts[(i - 1) % len(ghosts)]
    # Imprime con tabulaciones y el formato deseado
    print(f"DEC {movimiento}\t\t/−{comentario}−/")

# Línea final
print("DEC 100")