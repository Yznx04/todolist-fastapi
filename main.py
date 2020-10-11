from fastapi import FastAPI

from user.views import router

api = FastAPI()
api.include_router(router=router, prefix="/user", tags=["User"])
