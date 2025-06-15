import numpy as np
import random

# Se define la funcion para crear tableros
# se deben crear dos tableros diferentes, "tablero" para el jugador y "tablero_maquina" para la máquina
def crea_tablero(lado = 10):
    tablero = np.full((lado,lado)," ")
    return tablero

#Se van a definir las funciones para el usuario de colocar los barcos y para disparar

# Se define la fuincion para crear nuestros barcos
def coloca_barco(tablero, barco):
    barco
    for pieza in barco:
        tablero[pieza] = "O"
    return tablero

#creamos la funcion para disparar a la maquina
def disparar(tablero_maquina):

    dimension = tablero_maquina.shape[0]
    coord_str = input(f"Introduce tu coordenada (fila,columna) para disparar: ")
    partes = coord_str.split(',') # separamos la posicion para utilizarlas por independientes para el proximo control
    fila = int(partes[0].strip())#aqui la primera parte del input anterior la convertimos en entero para elegir la fila
    col = int(partes[1].strip())#aqui la segunda parte del input anterior la convertimos en entero para elegir la columna
    coordenada = (fila, col)

    if tablero_maquina[coordenada] == "O":
        tablero_maquina[coordenada] = "X"
        print("Tocado")
        return tablero_maquina

    elif tablero_maquina[coordenada] == "X":
        print("Agonia, deja de perder el tiempo, dispara a otro sitio")
        return tablero_maquina

    else:
        tablero_maquina[coordenada] = "A"
        print("Agua")
        return tablero_maquina

def coloca_barco_plus(tablero_maquina, barco):
    # Nos devuelve el tablero si puede colocar el barco, si no devuelve False, y avise por pantalla
    tablero_temp = tablero_maquina.copy()
    num_max_filas = tablero_maquina.shape[0]
    num_max_columnas = tablero_maquina.shape[1]
    for pieza in barco:
        fila = pieza[0]
        columna = pieza[1]
        if fila < 0  or fila >= num_max_filas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if columna <0 or columna>= num_max_columnas:
            print(f"No puedo poner la pieza {pieza} porque se sale del tablero")
            return False
        if tablero[pieza] == "O" or tablero[pieza] == "X":
            print(f"No puedo poner la pieza {pieza} porque hay otro barco")
            return False
        tablero_temp[pieza] = "O"
    return tablero_temp

def crea_barco_aleatorio(tablero_maquina,eslora = 4, num_intentos = 100):
    num_max_filas = tablero_maquina.shape[0]
    num_max_columnas = tablero_maquina.shape[1]
    while True:
        barco = []
        # Construimos el hipotetico barco
        pieza_original = (random.randint(0,num_max_filas-1),random.randint(0, num_max_columnas -1))
        print("Pieza original:", pieza_original)
        barco.append(pieza_original)
        orientacion = random.choice(["N","S","O","E"])
        print("Con orientacion", orientacion)
        fila = pieza_original[0]
        columna = pieza_original[1]
        for i in range(eslora -1):
            if orientacion == "N":
                fila -= 1
            elif orientacion  == "S":
                fila += 1
            elif orientacion == "E":
                columna += 1
            else:
                columna -= 1
            pieza = (fila,columna)
            barco.append(pieza)
        tablero_temp = coloca_barco_plus(tablero_maquina, barco)
        if type(tablero_temp) == np.ndarray:
            return tablero_temp
        print("Tengo que intentar colocar otro barco")

def disparo_aleatorio_maquina(tablero):

    posiciones_disponibles = []
    dimension = tablero.shape[0]
    for fila in range(dimension):
        for columna in range(dimension):
            if tablero[fila, columna] != 'X' and tablero[fila, columna] != 'A':
                posiciones_disponibles.append((fila, columna))

    # 3. Elegir una coordenada al azar de la lista de disponibles
    coordenada_elegida = random.choice(posiciones_disponibles)
    print(f"La máquina dispara en la coordenada: {coordenada_elegida}")


    if tablero[coordenada_elegida] == 'O':
        tablero[coordenada_elegida] = 'X'
        print(">> Resultado: ¡TOCADO!")
    else: # Es una casilla vacía (' ')
        tablero[coordenada_elegida] = 'A'
        print(">> Resultado: ¡AGUA!")

    return tablero

#Creamos nuestro tablero y colocamos nuestros barcos con un pequeño bucle
#Me hubiese gustado poder hacer inputs para colocar cada barco pero no he sido capaz, asi que los dejamos en estas posiciones fijas
tablero = crea_tablero(10)
barco1 = [(0,1),(1,1)]
barco2= [(9,1),(9,2)]
barco3 = [(2,4),(1,4)]
barco4=[(4,3),(4,4),(4,5)]
barco5=[(6,6),(5,6),(4,6)]
barco6= [(1,3), (1,4), (1,5), (1,6)]
barcos = [barco1, barco2,barco3, barco4,barco5,barco6]
for barco in barcos:
    tablero = coloca_barco(tablero,barco)

tablero_maquina = crea_tablero(10)
tablero_maquina = crea_barco_aleatorio(tablero_maquina, eslora = 4)
tablero_maquina = crea_barco_aleatorio(tablero_maquina, eslora = 3)
tablero_maquina = crea_barco_aleatorio(tablero_maquina, eslora = 3)
tablero_maquina = crea_barco_aleatorio(tablero_maquina, eslora = 2)
tablero_maquina = crea_barco_aleatorio(tablero_maquina, eslora = 2)
tablero_maquina = crea_barco_aleatorio(tablero_maquina, eslora = 2)


#Bucle princpipal de la partida se repetira mientras queden barcos en cualquier tablero
#asignamos los turnos impares al jugador y los turnos pares a la maquina
turno = 0
while np.any(tablero == 'O') and np.any(tablero_maquina == 'O'):

    if turno % 2 == 0:
        disparo = disparo_aleatorio_maquina(tablero)
        print(tablero)
        turno = turno + 1
        print(turno)
    else:
        tablero_maquina = disparar(tablero_maquina)
        print(tablero_maquina)
        turno = turno + 1
        print(turno)
else:
    print("Fin del juego")