import random

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

services = {}
metrics = {}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/discovery")
async def get_services():
    return list(services.values())


@app.post("/service/{name}")
async def create_service(name: str):
    services[name] = {
        "targets": ["localhost:8000"],
        "labels": {
            "name": name,
            "__metrics_path__": f"/service/{name}/metrics",
            "__scrape_interval__": "1s",
        }
    }
    metrics[name] = 0
    return {"message": f"Service {name}"}


@app.get("/service/{name}/metrics", response_class=PlainTextResponse)
async def get_service_metrics(name: str):
    metrics[name] += random.gauss()
    return f"metric {metrics[name]}"
