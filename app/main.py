from fastapi import FastAPI
from config import db_url
from routers.tariffs import tariff_router
from routers.insurance import insurance_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(docs_url='/')

app.include_router(tariff_router)
app.include_router(insurance_router)

register_tortoise(
    app,
    db_url=db_url,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
