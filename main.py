from task_automator.core import organize_folder

if __name__ == "__main__":
    path = input("Escribe la ruta de la carpeta que quieres organizar: ")
    dry_run_answer = input("¿Quieres probar sin mover archivos? s/n: ")

    dry_run = dry_run_answer.lower() == "s"

    result = organize_folder(path, dry_run=dry_run)
    print(result)
