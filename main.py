import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, select
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import asyncio


app = FastAPI()
app.mount("/K_tern/css", StaticFiles(directory="K_tern/css"), name="static")

templates = Jinja2Templates(directory="K_tern/html")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, id: str = Form(...), password: str = Form(...)):
    return templates.TemplateResponse(
        
    )

#ベースクラスの定義
Base = declarative_base()
#DB関連設定
base_dir = os.path.dirname(__file__) + "/db"
#データベースのURL
DATABASE_URL = "sqlite+aiosqlite:///" + os.path.join(base_dir, "unvsvdb.sqlite")

#非同期エンジン作成
engine = create_async_engine(DATABASE_URL, echo=True)
#非同期セッションの作成
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)
async def init_db():
    async with engine.begin() as conn:
        #新規にテーブルを作成
        await conn.run_sync(Base.metadata.create_all)
        print(">>>Create All Tables")

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(200), nullable=True)

async def get_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        return users

#ユーザー追加関数
async def add_user(name):
    print(f'{name}をデータベースに追加します。')
    async with async_session() as session:
        async with session.begin():
            user = User(user_name=name)  
            session.add(user)
            print(f'{name}を追加しました。')
async def main():
    await init_db()
    await add_user("testuser")
    await add_user("anotheruser")
    users = await get_users()
    for user in users:
        print(f'User ID: {user.user_id}, User Name: {user.user_name}')

asyncio.run(main())