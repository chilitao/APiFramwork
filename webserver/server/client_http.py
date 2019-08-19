import asyncio
import aiohttp
async def foo(times):
 data = {'foo': 1}
 async with aiohttp.ClientSession() as session:
  for x in range(times):
   resp = await session.post('http://localhost:8080', json=data)
   if not x % 100:
    print(await resp.json())
loop = asyncio.get_event_loop()
loop.run_until_complete(foo(100000))
loop.close()