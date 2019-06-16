#!/usr/bin/python3

import aiohttp
import asyncio
import time
import uuid

@asyncio.coroutine
def main_loop(session):
    game_stats = {}
    uuid_ = uuid.uuid4()
    while game_stats.get('score', 0) < 1000000:
        try:
            response = yield from session.request('GET', 'http://pms.zelros.com?id={}'.format(uuid_))
            game_stats.update((yield from response.json()))
            print(game_stats)
        finally:
            response.close()
        time.sleep(1)

@asyncio.coroutine
def main():
    try:
        session = aiohttp.ClientSession()        
        yield from main_loop(session)
    finally:
        session.close()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
