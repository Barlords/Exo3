# Ajouter l'implémentation de vos opérations ici
import sys


def addition(a, b):
    return a + b


def multiplication(a, b):
    return a * b


"""
dictionnaire des opérations 
A modifier en cas d'ajout d'une opération
"""
operations = {
    '+': addition,
    '*': multiplication,
}

"""
dictionnaire de traduction des opération 
A modifier en cas d'ajout d'une opération
"""
operations_name = {
    '+': 'addition',
    '*': 'multiplication',
}


def operator_is_allowed(operator):
    if operator in operations:
        return True
    else:
        return False


def verify_operator(operator):
    if not operator_is_allowed(operator):
        print(f"L'opérateur '{operator}' n'est pas autorisé.")
        sys.exit(1)
