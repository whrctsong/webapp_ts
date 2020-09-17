# -*- coding: utf-8 -*-

__author__ = 'Song Tian'

'''
async web application.
'''

import logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome,Tian Song</h1>',headers={'content-type':'text/html'})

def hello(request):
    text = '<h1>Hello, %s!</h1>' % request.match_info['name']
    print('用户名称：%s' % text)
    return web.Response(body=text.encode('utf8'),headers={'content-type':'text/html'})

async def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    # srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 9000)
    srv = await site.start()
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.new_event_loop()
loop.run_until_complete(init())
loop.run_forever()


