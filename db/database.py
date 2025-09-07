import os
from sqlalchemy.ext.asyncio import create_async_engine
from memo import Base
import asyncio

#--DBファイル作成--
base_dir = os.path.dirname(__file__)
#DBのurl
DATABASE_URL = "sqlite+aiosqlite:///" + os.path.join(base_dir, "unvsvdb.sqlite")

#非同期エンジン作成
engine = create_async_engine(DATABASE_URL, echo=True)
#DB初期化
async def init_db():
    async with engine.begin() as conn:
        #既存のテーブルを削除
        await conn.run_sync(Base.metadata.drop_all)
        print(">>>Drop All Tables")
        #新規にテーブルを作成
        await conn.run_sync(Base.metadata.create_all)
        print(">>>Create All Tables")
if __name__ == "__main__":
    asyncio.run(init_db())