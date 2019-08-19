from aiohttp import web
async def hello(request):
 return web.json_response(await request.json())
app = web.Application()
app.add_routes([web.post('/', hello)])
web.run_app(app)