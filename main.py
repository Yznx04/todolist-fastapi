from fastapi import FastAPI

from user.views import router

api = FastAPI(tags=["home"])
api.include_router(router=router, prefix="/user", tags=["User"])


@api.get("/")
def home():
    return {"yznx": "Keep coding every days!"}
