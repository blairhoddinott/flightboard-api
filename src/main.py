import argparse
import json
import os
import structlog
import sys

from dotenv import load_dotenv
from flightboard import Radar, plane
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


def run():
    log.info("Running")
    radar = Radar("http://fa.weepytests.com/skyaware/data/aircraft.json")
    results = radar._get_radar_dump()
    for plane in results:
        log.info("", callsign=plane["flight"], altitude=plane["alt_baro"], speed=plane["gs"])
        
    # log.info(results)


if __name__ == "__main__":
    run()
