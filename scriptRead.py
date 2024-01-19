def leer_coordenadas_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            # Lee la línea y divide las coordenadas
            linea = archivo.readline().strip()
            coordenadas = list(map(float, linea.split()))
            return tuple(coordenadas)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
        return None
    except Exception as e:
        print(f"Error al leer las coordenadas desde {nombre_archivo}: {e}")
        return None

# Nombre del archivo de texto
nombre_archivo = 'coordenadas.txt'

# Lee las coordenadas desde el archivo
coordenadas_rectangulo = leer_coordenadas_desde_archivo(nombre_archivo)

# Verifica si las coordenadas se leyeron correctamente
if coordenadas_rectangulo is not None:
    print(f"Coordenadas del rectángulo leídas desde {nombre_archivo}: {coordenadas_rectangulo}")
else:
    print("No se pudieron leer las coordenadas.")