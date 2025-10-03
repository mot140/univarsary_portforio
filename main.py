
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from back.api_class import test
import requests, json

app = FastAPI()
user = "Mt"
app.mount("/css", StaticFiles(directory="K_tern/css"), name="static")

templates = Jinja2Templates(directory="K_tern/html")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/HOME", response_class=HTMLResponse)
async def read_root(request: Request):
    data = test.json()
    return templates.TemplateResponse("Top.html", {"request": request,"user":user,"wether_today":data["forecasts"][0]["telop"],"weather_tomorrow":data["forecasts"][1]["telop"],"weather_aftertomorrow":data["forecasts"][2]["telop"]})

@app.get("/risy", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("risy.html", {"request": request,"user":user})

