import sys


def convert_string_to_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"La chaîne '{value}' ne peut pas être convertie en nombre.")
        sys.exit(1)


def convert_file_to_values(path):
    values = []
    lines = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Le fichier {path} n'existe pas.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        sys.exit(1)
    for line in lines:
        values.append(convert_string_to_int(line))
    return values

