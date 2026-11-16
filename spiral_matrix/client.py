import asyncio
from typing import List
import aiohttp

from spiral_matrix.parser import parse_matrix
from spiral_matrix.traversal import spiral_traversal


class MatrixFetchError(Exception):
    """Не удалось получить матрицу с сервера."""


class MatrixFormatError(Exception):
    """Сервер ответил, но это не квадратная матрица из чисел."""


async def get_matrix(url: str) -> List[int]:
    try:
        client_timeout = aiohttp.ClientTimeout(total=timeout)
        async with aiohttp.ClientSession(timeout=client_timeout) as session:
            async with session.get(url) as response:
                response.raise_for_status()
                text = await response.text()
    except asyncio.TimeoutError as error:
        raise MatrixFetchError(f'Сервер не ответил за {timeout} сек.') from error
    except aiohttp.ClientError as error:
        raise MatrixFetchError(f'Ошибка запроса: {error}') from error

    try:
        matrix = parse_matrix(text)
    except ValueError as error:
        raise MatrixFormatError('В таблице есть не числа') from error
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise MatrixFormatError('Матрица пустая или не квадратная')
    return spiral_traversal(matrix)