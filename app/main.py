from fastapi import FastAPI

from .address import models
from .address.database import engine
from .address.routers import address

app = FastAPI()

# creates table if model does not exist in DB
models.Base.metadata.create_all(engine)

app.include_router(address.router)
