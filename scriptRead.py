def leer_coordenadas_desde_archivo(nombre_archivo): #introducir nº de líneas para bucle for
    try:
        with open(nombre_archivo, 'r') as archivo:
            # Lee la línea y divide las coordenadas
            linea = archivo.readline().strip()
            linea = linea.replace(',', '')                 #Quitarle la coma para manejarlo como float
            coordenadas = list(map(float, linea.split()))         
            return tuple(coordenadas[1:])
        
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
        return None
    except Exception as e:
        print(f"Error al leer las coordenadas desde {nombre_archivo}: {e}")
        return None

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
if coordenadas_rectangulo is not None:
    print(f"Coordenadas del rectángulo leídas desde {nombre_archivo}: {coordenadas_rectangulo}") 
else:
    print("No se pudieron leer las coordenadas.")