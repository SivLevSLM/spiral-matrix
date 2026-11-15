from typing import List


def spiral_traversal(matrix: List[List[int]]) -> List[int]:
    result: List[int] = []
    while matrix and matrix[0]:
        result += [row[0] for row in matrix] # левый столбец сверху вниз
        matrix = [row[1:] for row in matrix]
        if not matrix[0]:
            break
        
        result += matrix[-1] # нижняя строка слева направо
        matrix = matrix[:-1]
        if not matrix:
            break
        
        result += [row[-1] for row in reversed(matrix)] # правый столбец снизу вверх
        matrix = [row[:-1] for row in matrix]
        if not matrix[0]:
            break
        
        result += matrix[0][::-1] # верхняя строка справа налево
        matrix = matrix[1:]
    return result