import os
import shutil

def organize_folder(path):
    if not os.path.exists(path):
        print("La ruta no existe")
        return

    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if os.path.isfile(full_path):
            ext = file.split('.')[-1]

            folder_name = os.path.join(path, ext)

            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            shutil.move(full_path, os.path.join(folder_name, file))

    print("Archivos organizados correctamente")
