import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
#---DBアクセス設定---
#---DB接続---
Base = declarative_base()

#--DBファイル作成---
base_dir = os.path.dirname(__file__)
DATABASE_URL = "sqlite+aiosqlite:///" + os.path.join(base_dir, "unvsvdb.sqlite")

#非同期エンジン作成
engine = create_async_engine(DATABASE_URL, echo=True)
#非同期セッションの作成
async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_ = AsyncSession
)

#DBとの非同期的に扱うことが出来る関数
async def get_dbsession():
    async with async_session as session:
        yield session