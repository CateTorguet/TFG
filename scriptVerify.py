import matplotlib.pyplot as plt
import argparse
import matplotlib.patches as patches
import matplotlib.image as mpimg
import os


def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            coordenadas_aux = []                                        


            for i in range(len(lineas)):
                lineas[i] = lineas[i].replace(',','')


            coordenadas_aux = [tuple(map(float, linea.strip().split()[1:])) for linea in lineas]    # línea = (x, y, width, height)   [(x, y, width, height),(x, y, width, height),...]
                                                                                                    # map (type converter) + strip/split
            return coordenadas_aux                                                                  # Devuelve una lista de cada fila (file)
   
    except FileNotFoundError:
        return f"El archivo '{nombre_archivo}' no fue encontrado."
    except Exception as e:
        return f"Ocurrió un error: {e}"


def count_dir():
    try:
        archivos = os.listdir("runs/detect")       # Lista todos los archivos en la carpeta
        return len(archivos)              # Devuelve el número de archivos
    except OSError:
        return -1


def Ubicar_img(j):
    if(j == 499):
        nombre_img = "runs/detect" + "/exp/" + f"{j:06d}.png"
    else:
        num = j-498
        nombre_img = "runs/detect" + "/exp"+str(num) + "/" + f"{j:06d}.png"
    return nombre_img


def ubicar_txt(i):
    if(i == 499):
        dir = "runs/detect" + "/exp" + "/labels/"+ f"{i:06d}.txt"
    else:
        num = i-498
        dir = "runs/detect" + "/exp"+str(num) + "/labels/" + f"{i:06d}.txt"
    return dir


def draw_rect(coordenadas, i, file, ax):
    colores = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    x2 = coordenadas[file][i][0] - coordenadas[file][i][2] / 2
    y2 = coordenadas[file][i][1] - coordenadas[file][i][3] / 2
       
    rectangulo = patches.Rectangle((x2, -y2),
                                    coordenadas[file][i][2],
                                    -coordenadas[file][i][3],
                                    linewidth=1, edgecolor=colores[i % len(colores)], facecolor='none')
    ax.add_patch(rectangulo)
   
def main(leer_archivo, count_dir, Ubicar_img, ubicar_txt, draw_rect):
    parser = argparse.ArgumentParser(description="Comprobación sobre el control de las coordenadas en las que se detecto actividad.")
    parser.add_argument("-img", action="store_true", help="Mostrar imagen de fondo.")
    parser.add_argument("-s", action="store_true", help="Mostrar gráfico.")
    parser.add_argument("--n", type=int, default=float('inf'), help="Número máximo de rectángulos a dibujar.")
    args = parser.parse_args()


    #Lista[][][] Coordenadas de todos los experimentos a trazar
    coordenadas = []


    for i in range(499, 499+count_dir()):
        #Read  
        nombre_archivo = ubicar_txt(i)
        coordenadas_rectangulo = leer_archivo(nombre_archivo)          
        nombre_img = Ubicar_img(i)
        background_img = mpimg.imread(nombre_img)
        coordenadas.append(coordenadas_rectangulo)                      # Se añade la lectura de un fichero


        #Draw
        fig, ax = plt.subplots()
        ax.set_xlim(0, 1)
        ax.set_ylim(-1, 0)
        ax.set_aspect('equal', adjustable='datalim')
        ax.set_frame_on(False)
        plt.title(f'Verificación de funcionamiento - Archivo-{str(i - 498)}')
        for line in range(len(coordenadas_rectangulo)):
            if(line < args.n):
                draw_rect(coordenadas,line, i - 499, ax)                 # Eje y  invertido
       


        # Guarda y mostrar
        if(args.img):
            ax.imshow(background_img, extent=[0, 1, -1, 0])
        plt.savefig('results/Comprobación-' + str(i - 498), bbox_inches='tight')
        if(args.s):
            plt.show()
        plt.close()


if __name__ == "__main__":
    main(leer_archivo, count_dir, Ubicar_img, ubicar_txt, draw_rect)
