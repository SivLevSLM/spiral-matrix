from typing import List

def parse_matrix(text: str)-> List[List[int]]:
    matrix: List[List[int]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        matrix.append([int(c) for c in cells])
    return matrix