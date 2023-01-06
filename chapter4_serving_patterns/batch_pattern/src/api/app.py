import time
from logging import getLogger

from fastapi import FastAPI
from src.api import routers
from src.configurations import APIConfigurations
from src.db import initialize
from src.db.database import engine

logger = getLogger(__name__)

logger.info("Start initialize")
try:
    initialize.initialize_database(engine=engine, checkfirst=True)
except Exception as e:
    logger.info("Rise Error at initialize; Exit.")
    print(e)
    exit()

app = FastAPI(
    title=APIConfigurations.title,
    description=APIConfigurations.description,
    version=APIConfigurations.version,
)

app.include_router(routers.router, prefix="", tags=[""])
