import matplotlib.pyplot as plt
from tqdm import tqdm
import os

''' Crear y personalizar un gráfico
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label='Función seno')
plt.title('Gráfico de la función seno')
plt.legend()
# Mostrar el gráfico con plt.show()
plt.show()
'''


def contar_archivos_en_carpeta(ruta):
    try:
        archivos = os.listdir(ruta)       # Lista todos los archivos en la carpeta
        return len(archivos)              # Devuelve el número de archivos
    except OSError:
        # Manejo de errores en caso de que la carpeta no exista o haya problemas de acceso
        return -1

# Especifica la ruta de la carpeta
carpeta = "runs/detect"
# Llama a la función y muestra el resultado
num_archivos = contar_archivos_en_carpeta(carpeta)
if num_archivos >= 0:
    print(f"El número de experimentos en la carpeta {carpeta} es: {num_archivos}")
else:
    print(f"No hay experimentos que mostrar {carpeta}")

for i in tqdm(range(499, 499+num_archivos), desc="Procesando imagen"):

    nombre_img = f"{i:06d}.png"
    print("\n" + nombre_img)

    if(i == 499):
        dir = "runs/detect/exp"
    else:
        num = i-498
        dir = "runs/detect/exp"+str(num)

    img_path = dir+"/"+ nombre_img

    img = plt.imread(img_path)
    plt.imshow(img)
    #plt.show(block=True)
    plt.pause(0.1)
    plt.clf()