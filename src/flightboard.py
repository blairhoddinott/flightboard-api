import httpx
import json

from dataclasses import dataclass

@dataclass
class plane:
    registration: str
    callsign: str
    origin: str
    destination: str
    altitutde: str
    speed: str
    heading: str

class Radar():
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
