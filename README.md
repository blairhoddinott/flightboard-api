# flightboard-api

## Overview

This is a library to pull data from a few sources to correlate current dump1090 traffic. We assemble flight strips using raw dump1090 data, and combining it with results from ADSBDB to get aircraft type, airline, origin, destination. This gives a more complete picture from your dump1090 setup. 

## Usage

To get this running, you will need to change the .env.template to .env and update the URL to your dump1090 aircraft.json. If you are running PiAware (like I am), this URL will be something like `http://<ip_of_your_piaware>/skyaware/data/aircraft.json`

Once this has been updated, you should be able to run the sample main.py to pull the data. `uv run src/main.py`

### API

I will be working on making a FastAPI endpoint that uses this library so that this data can be pulled programtically. The goal will be to make a Frontend for it to display flight strips kind of like an ATC station. Would be cool if I knew anything about Frontend Development :)

## Frontend Development

I will have another repository (flightboard-frontend) that will have my ham-fisted approach to frontending this thing. If you wish to contribute, please get in touch with me, or open an issue and we can collaborate or maybe even just PR your code right in. Would be nice to have a pretty FE for this. I'd like to have this running on a display in my house. 
