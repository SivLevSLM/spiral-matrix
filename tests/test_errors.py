import asyncio
import pytest

from aiohttp import web
from aiohttp.test_utils import TestServer

from spiral_matrix import get_matrix
from spiral_matrix.client import MatrixFetchError, MatrixFormatError


def run_with_server(handler, check):
    async def main():
        app = web.Application()
        app.router.add_get('/matrix', handler)
        server = TestServer(app)
        await server.start_server()
        try:
            return await check(str(server.make_url('/matrix')))
        finally:
            await server.close()
    return asyncio.run(main())


def test_server_error_500():
    async def handler(request):
        return web.Response(status=500)

    async def check(url):
        with pytest.raises(MatrixFetchError):
            await get_matrix(url)

    run_with_server(handler, check)


def test_timeout():
    async def handler(request):
        await asyncio.sleep(1)
        return web.Response(text='|1|')

    async def check(url):
        with pytest.raises(MatrixFetchError):
            await get_matrix(url, timeout=0.1)

    run_with_server(handler, check)


def test_connection_refused():
    with pytest.raises(MatrixFetchError):
        asyncio.run(get_matrix('http://127.0.0.1:1/matrix'))


def test_not_square_matrix():
    async def handler(request):
        return web.Response(text='|1|2|\n')

    async def check(url):
        with pytest.raises(MatrixFormatError):
            await get_matrix(url)

    run_with_server(handler, check)


def test_not_numbers():
    async def handler(request):
        return web.Response(text='|a|\n')

    async def check(url):
        with pytest.raises(MatrixFormatError):
            await get_matrix(url)

    run_with_server(handler, check)