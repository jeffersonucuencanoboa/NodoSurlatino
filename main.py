from task_automator.core import organize_folder

if __name__ == "__main__":
    path = input("Escribe la ruta de la carpeta que quieres organizar: ")
    dry_run_answer = input("¿Quieres probar sin mover archivos? s/n: ")

    dry_run = dry_run_answer.lower() == "s"

    result = organize_folder(path, dry_run=dry_run)
    print(result)
import argparse
from task_automator.core import organize_folder

def main():
    parser = argparse.ArgumentParser(
        description="Organiza archivos por extensión"
    )

    parser.add_argument(
        "--path",
        required=True,
        help="Ruta de la carpeta a organizar"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simula sin mover archivos"
    )

    args = parser.parse_args()

    try:
        result = organize_folder(args.path, dry_run=args.dry_run)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
