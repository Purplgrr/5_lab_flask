import math
import constants

def solve_operation_type_1(operation: str, operands: tuple) -> float:
    base, side_a, side_b, height = operands
    x_1 = round(math.sqrt(side_a**2  - height**2), 2)
    x_2 = round(math.sqrt(side_b**2 - height**2), 2)
    unknown_side = base - x_1 - x_2

    match operation:
        case 'Периметр':
            P = unknown_side + base + side_a + side_b
            return P
        case 'Неизвестные стороны':
            return unknown_side
        case 'Угол между диагоналями':
            m = (unknown_side + base) / 2
            d_1 = math.sqrt((base - x_2)**2 + height**2)
            d_2 = math.sqrt((base - x_1)**2 + height**2)
            alpha = math.asin(2 * m * height / (d_1 * d_2))

            return round(180 * alpha / math.pi, 2)

def solve_operation_type_2(operation: str, operands: tuple) -> float|str:
    base, angle_a, angle_b, height = operands

    angle_a = math.pi * angle_a / 180
    angle_b = math.pi * angle_b / 180

    side_a = round(height / math.sin(angle_a), 2)
    side_b = round(height / math.sin(angle_b), 2)

    x_1 = round(math.sqrt(side_a**2  - height**2), 2)
    x_2 = round(math.sqrt(side_b**2  - height**2), 2)

    another_base = round(base - x_1 - x_2, 2)

    match operation:
        case 'Периметр':
            P = another_base + base + side_a + side_b
            return P
        case 'Неизвестные стороны':
            return f'Другое основание: {another_base} Боковая сторона 1: {side_a} Боковая сторона 2: {side_b}'
        case 'Угол между диагоналями':
            m = (another_base + base) / 2
            d_1 = math.sqrt((base - x_2)**2 + height**2)
            d_2 = math.sqrt((base - x_1)**2 + height**2)
            alpha = math.asin(2 * m * height / (d_1 * d_2))

            return round(180 * alpha / math.pi, 2)

def solve_operations(input_type: str, operations: list[str], operands: tuple) -> str:
    base, height, side_a, side_b, angle_a, angle_b = operands
    res = ''

    if input_type == '1':
        for operation in operations:
            index = int(operation)
            operation_name = constants.operations[index]

            res += f'{operation_name}: {solve_operation_type_1(operation_name, (base, side_a, side_b, height))} '
    else:
        for operation in operations:
            index = int(operation)
            operation_name = constants.operations[index]

            res += f'{operation_name}: {solve_operation_type_2(operation_name, (base, angle_a, angle_b, height))} '
    
    return res