import argparse
import json
import os
import structlog
import sys

from dotenv import load_dotenv
from fastapi import FastAPI
from flightboard import Radar, flightstrip 
from structlog import get_logger

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso", utc=False),
        structlog.processors.add_log_level,
        structlog.dev.ConsoleRenderer(),
    ]
)
log = get_logger()
load_dotenv()


DUMP_1090_URL = os.getenv("DUMP1090_URL")
app = FastAPI()
radar = Radar(DUMP_1090_URL)


@app.get("/sweep")
def sweep():
    log.info("Radar sweep...")
    flightstrips = radar.sweep()
    for flightstrip in flightstrips:
        log.info("", strip=flightstrip)
    return flightstrips

