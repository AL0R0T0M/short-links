import uvicorn
from fastapi import FastAPI
from app.cutLink.router import router_shortcut_link


app = FastAPI()
app.include_router(router_shortcut_link)

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
