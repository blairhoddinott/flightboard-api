import httpx
import json

from dataclasses import dataclass
from structlog import get_logger


log = get_logger()

@dataclass
class flightstrip:
    registration: str = None
    callsign: str = None
    origin: str = None
    destination: str = None
    altitude: str = None
    speed: str = None
    heading: str = None
    airline: str = None
    type: str = None
    squawk: str = None
    route: str = None
    vs_rate: str = None
    emergency: bool = None


class Radar():
    ADSBDB_CALLSIGN_ENDPOINT = "https://api.adsbdb.com/v0/callsign"
    ADSBDB_AIRCRAFT_ENDPOINT = "https://api.adsbdb.com/v0/aircraft"

    def __init__(self, dump_url):
        self.dump_url = dump_url

    def _get_radar_dump(self):
        response = httpx.get(self.dump_url)
        if response.status_code == 200:
            planes = []
            radar_dump = json.loads(response.text)
            for aircraft in radar_dump["aircraft"]:
                if "flight" in aircraft:
                    planes.append(aircraft)
            return planes
        else:
            log.critical("Something went wrong getting dump1090 output")

    def _process_flightstrip(self, plane):
        new_flightstrip = flightstrip()
        new_flightstrip.registration = plane["hex"]
        new_flightstrip.callsign = plane["flight"].strip()
        new_flightstrip.altitude = str(plane["alt_baro"])
        if "ias" not in plane:
            new_flightstrip.speed = str(plane["gs"])
        else:
            new_flightstrip.speed = str(plane["ias"])
        new_flightstrip.heading = str(plane["track"])
        if "baro_rate" in plane:
            new_flightstrip.vs_rate = str(plane["baro_rate"])
        if "emergency" in plane and plane["emergency"] != "none":
            new_flightstrip.emergency = True
        if "squawk" in plane:
            new_flightstrip.squawk = plane["squawk"]
        return new_flightstrip

    def _get_flight_route(self, callsign):
        response = httpx.get(f"{self.ADSBDB_CALLSIGN_ENDPOINT}/{callsign}")
        if response.status_code == 404:
            return None
        else:
            return json.loads(response.text)

    def _get_aircraft_details(self, registration):
        response = httpx.get(f"{self.ADSBDB_AIRCRAFT_ENDPOINT}/{registration}")
        if response.status_code == 404:
            return None
        else:
            return json.loads(response.text)

    def sweep(self):
        contacts = self._get_radar_dump()
        radar_sweep = []
        for plane in contacts:
            if "flight" in plane:
                flightstrip = self._process_flightstrip(plane)
                route_details = self._get_flight_route(flightstrip.callsign)
                if route_details:
                    flightstrip.origin = route_details["response"]["flightroute"]["origin"]["icao_code"]
                    flightstrip.destination = route_details["response"]["flightroute"]["destination"]["icao_code"]
                aircraft_details = self._get_aircraft_details(flightstrip.registration)
                if aircraft_details:
                    flightstrip.type = aircraft_details["response"]["aircraft"]["type"]
                    flightstrip.airline = aircraft_details["response"]["aircraft"]["registered_owner"]
                radar_sweep.append(flightstrip)
        return radar_sweep

