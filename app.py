from fastapi import FastAPI, Request
from starlette.responses import FileResponse
import uvicorn
from utilities.use_config import UseConfig

api_url = "/api/v1"
port = 8000
host = '127.0.0.1'

app = FastAPI(
    title='Web Scraper of Doom',
    openapi_url=api_url
)

@app.get("/")
async def serve_static():
    return FileResponse('static/index.html', media_type='text/html')


@app.get("/styles.css")
async def load_css():
    return FileResponse('static/styles.css')

@app.get("/script.js")
async def load_js():
    return FileResponse('static/script.js')


@app.post(f"{api_url}/scrape")
async def get_config(request: Request):
    config = await request.json()
    response = UseConfig(config)
    return response


if __name__ == '__main__':
    uvicorn.run("app:app", reload=True, port=port, host=host)