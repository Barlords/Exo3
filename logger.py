from operations import operations_name


def print_operation(value, operator, result):
    print(f"{operator}{value} (={result})")


def print_result(result, operator):
    print("-------")
    print(f"total = {result} ({operations_name[operator]})")

