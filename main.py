
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()
app.mount("/K_tern/css", StaticFiles(directory="K_tern/css"), name="static")

templates = Jinja2Templates(directory="K_tern/html")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/HOME", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("Top.html", {"request": request})

@app.get("/risy", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("risy.html", {"request": request})
