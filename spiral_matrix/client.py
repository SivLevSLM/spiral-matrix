from typing import List
import aiohttp

from spiral_matrix.parser import parse_matrix
from spiral_matrix.traversal import spiral_traversal

async def get_matrix(url: str)-> List[int]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            text = await response.text()
        return spiral_traversal(parse_matrix(text))