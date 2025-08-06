import argparse
import json
import os
import structlog
import sys

from dotenv import load_dotenv
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
def run():
    log.info("Running")
    radar = Radar(DUMP_1090_URL)
    flightstrips = radar.sweep()
    for flightstrip in flightstrips:
        log.info("", strip=flightstrip)


if __name__ == "__main__":
    run()
