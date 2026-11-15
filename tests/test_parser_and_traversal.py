from spiral_matrix.parser import parse_matrix
from spiral_matrix.traversal import spiral_traversal

TABLE = """+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
"""
EXPECTED = [10, 50, 90, 130, 140, 150, 160, 120, 80, 40, 30, 20, 60, 100, 110, 70]


def test_parse_matrix():
    assert parse_matrix(TABLE)[0] == [10, 20, 30, 40]
    assert len(parse_matrix(TABLE)) == 4


def test_spiral_4x4():
    assert spiral_traversal(parse_matrix(TABLE)) == EXPECTED


def test_spiral_1x1():
    assert spiral_traversal([[7]]) == [7]


def test_spiral_2x2():
    assert spiral_traversal([[1, 2], [3, 4]]) == [1, 3, 4, 2]


def test_spiral_3x3():
    assert spiral_traversal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 4, 7, 8, 9, 6, 3, 2, 5]