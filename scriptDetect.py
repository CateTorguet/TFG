import subprocess
from tqdm import tqdm

for i in tqdm(range(499, 1120), desc="Procesando imagen"):

    nombre_img = f"{i:06d}.png"
    print("\n" + nombre_img)
    
    
    script_path = "detect.py"
    img_path = "camera_rgb/" + nombre_img

    comando = ["python", script_path, "--weights", "yolov5s.pt", "--source", img_path, "--save-txt"]
    
    try:
        proceso = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        # print("Salida:", proceso.stdout) # Imprime nada.... e.e
        # print(proceso.stderr)            # Imprime los resultados de la detección
    except subprocess.CalledProcessError as e:
        print(f"Error al procesar la imagen {nombre_img}: {e.stderr}")
