FROM ghcr.io/astral-sh/uv:alpine AS base
WORKDIR /srv/flightboard-api
COPY . .
EXPOSE 8000
ENTRYPOINT ["uv", "run", "src/api.py"]
