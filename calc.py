import sys
from file_converter import convert_file_to_values
from logger import print_operation, print_result
from operations import operations, verify_operator


def compute(values, operator):
    total = values[0]
    print(total)
    for value in values[1:]:
        total = operations[operator](total, value)
        print_operation(value, operator, total)
    print_result(total, operator)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python calc.py <chemin_du_fichier> '<operation>'")
        sys.exit(1)

    path = sys.argv[1]
    operator = sys.argv[2]

    verify_operator(operator)
    values = convert_file_to_values(path)

    compute(values, operator)
