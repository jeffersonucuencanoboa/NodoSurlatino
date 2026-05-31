import shutil
from pathlib import Path
def organize_folder(folder_path, dry_run=False):
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError("La carpeta no existe.")

    if not folder.is_dir():
        raise NotADirectoryError("La ruta no es una carpeta.")

    actions = []

    for item in folder.iterdir():
        if item.is_file():
            extension = item.suffix.lower().replace(".", "")

            if extension == "":
                extension = "sin_extension"

            destination = folder / extension
            target = destination / item.name

            actions.append(f"{item.name} -> {extension}/{item.name}")

            if not dry_run:
                destination.mkdir(exist_ok=True)
                shutil.move(str(item), str(target))

    if dry_run:
        return "\n".join(actions) if actions else "No hay archivos para organizar."

    return "Carpeta organizada correctamente."
