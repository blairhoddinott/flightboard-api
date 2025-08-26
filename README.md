# flightboard-api

## Overview

This is a library to pull data from a few sources to correlate current dump1090 traffic. We assemble flight strips using raw dump1090 data, and combining it with results from ADSBDB to get aircraft type, airline, origin, destination. This gives a more complete picture from your dump1090 setup. 

## Usage

To get this running, you will need to change the .env.template to .env and update the URL to your dump1090 aircraft.json. If you are running PiAware (like I am), this URL will be something like `http://<ip_of_your_piaware>/skyaware/data/aircraft.json`

Once this has been updated, you should be able to run the sample main.py to pull the data. `uv run src/main.py`

## Dockerfile

There is a `Dockerfile` supplied which can be used to build this. There is a `docker-compose.yaml` which can be used to run it. I will eventually be making this a public Docker image which you will need to override the environment variables. Just not there quite yet. You will need to populate your .env file **before** you Docker build it.

Docker Build command:
```bash
docker build -t weepyadmin/flightboard-api:latest .
```

### API

The API is running in the api.py file. This will reach out to [ADSBDB](https://www.adsbdb.com/) and augment the flight information from Dump1090. This helps to provide a more complete picture of the aircraft around your station, with Origin/Destination information.

## Frontend Development

The UI for this is located [here](https://github.com/blairhoddinott/flightboard-ui). I am not a proper frontend developer, and this is not the prettiest thing. It can connect to this API and provide data in a flightstrip, like what may be seen within a TRACON. The idea is cool, even if the execution isn't amazing. PRs, feedback and/or help with the UI is very much appreciated.

## Future plans

I would like to flesh out the details more. The next major feature I'd like to build is the ability to scrape the route from a **very** popular flight tracking website ;)
