import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def punto_dentro_del_rectangulo(coordenadas_rectangulo, punto, i):
    x1, y1, x2, y2 = coordenadas_rectangulo[i]
    x, y = punto
    if x2 <= x <= x1 and y2 <= y <= y1:
        return True
    else:
        return False

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            coordenadas = []                                        # Cargar línea a línea 

            for i in range(len(lineas)):
                lineas[i] = lineas[i].replace(',','')

            coordenadas = [tuple(map(float, linea.strip().split()[1:])) for linea in lineas]

            return coordenadas                                      #[(0,0,0,0),(0,0,0,0),...]
    except FileNotFoundError:
        return f"El archivo '{nombre_archivo}' no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error: {e}"



nombre_archivo = 'coordenadas.txt'
coordenadas_rectangulo = leer_archivo(nombre_archivo)
i=0

while True:                                                                     #Añadir for con i
    punto_aleatorio = (random.uniform(0, 1), random.uniform(0, 1))                                             # Punto aleatorio
    
    resultado = punto_dentro_del_rectangulo(coordenadas_rectangulo, punto_aleatorio, i)                        # Verificar si el punto está dentro del rectángulo
    # Crear el gráfico
    fig, ax = plt.subplots()
    rectangulo = patches.Rectangle((coordenadas_rectangulo[i][0], coordenadas_rectangulo[i][1]),
                                coordenadas_rectangulo[i][2] - coordenadas_rectangulo[i][0],
                                coordenadas_rectangulo[i][3] - coordenadas_rectangulo[i][1],
                                linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rectangulo)
    ax.plot(punto_aleatorio[0], punto_aleatorio[1], 'bo', label='Punto Aleatorio')                                                                                                              # Ajustes del gráfico
    ax.set_xlim(-0.5, 1.5)  
    ax.set_ylim(-0.5, 1.5) 
    ax.set_aspect('equal', adjustable='datalim')
                                                                                                                # Mostrar leyenda y el gráfico
    plt.legend()
    plt.show()

    i=i+1

    if resultado:                                                                                               # Imprimir el resultado
        print("El punto está dentro del rectángulo.")
    else:
        print("El punto está fuera del rectángulo.")