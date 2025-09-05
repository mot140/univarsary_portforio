from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 静的ファイルの読み込み設定（/static パスでアクセス可能に）
app.mount("/K_tern/css", StaticFiles(directory="K_tern/css"), name="static")

templates = Jinja2Templates(directory="K_tern/html")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # テンプレートにrequestを渡す必要がある（URL生成などに使用）
    return templates.TemplateResponse("login.html", {"request": request})