# Prometheus - Dynamic Targets

Start services with `docker compose up`

We have a setup that simulates
- a mock server that provides
    - an endpoint to discover services `http://localhost:8000/discovery`
    - an endpoint to dynamically create new services `http://localhost:8000/service/{name}`
    - an endpoint to get Prometheus metrics (random walk) from a service `http://localhost:8000/service/{name}/metrics`
- a Prometheus server that
    - polls the server for new services
    - polls all known services for metrics
- a Grafana server that
    - sets up a default dashboard that displays all metrics from Prometheus `http://localhost:3000/`
