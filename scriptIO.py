import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def punto_dentro_del_rectangulo(coordenadas_rectangulo, punto):
    x1, y1, x2, y2 = coordenadas_rectangulo
    x, y = punto
    if x2 <= x <= x1 and y2 <= y <= y1:
        return True
    else:
        return False

# Coordenadas del rectángulo
coordenadas_rectangulo = (0.557083, 0.551111, 0.0291667, 0.0266667)

# Punto aleatorio
punto_aleatorio = (random.uniform(0, 1), random.uniform(0, 1))

# Verificar si el punto está dentro del rectángulo
resultado = punto_dentro_del_rectangulo(coordenadas_rectangulo, punto_aleatorio)

# Crear el gráfico
fig, ax = plt.subplots()

# Dibujar el rectángulo
rectangulo = patches.Rectangle((coordenadas_rectangulo[0], coordenadas_rectangulo[1]),
                               coordenadas_rectangulo[2] - coordenadas_rectangulo[0],
                               coordenadas_rectangulo[3] - coordenadas_rectangulo[1],
                               linewidth=1, edgecolor='r', facecolor='none')

ax.add_patch(rectangulo)

# Marcar el punto aleatorio
ax.plot(punto_aleatorio[0], punto_aleatorio[1], 'bo', label='Punto Aleatorio')

# Ajustes del gráfico
ax.set_xlim(0, 1)  # Ajusta según las coordenadas x que necesites
ax.set_ylim(0, 1)  # Ajusta según las coordenadas y que necesites
ax.set_aspect('equal', adjustable='datalim')

# Mostrar leyenda y el gráfico
plt.legend()
plt.show()

# Imprimir el resultado
if resultado:
    print("El punto está dentro del rectángulo.")
else:
    print("El punto está fuera del rectángulo.")
