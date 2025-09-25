from fastapi import FastAPI
from gaia_v67 import GAIA, Config
import asyncio
from prometheus_client import start_http_server, Gauge, Summary
import numpy as np

# Prometheus Metrics as documented in README.md
GAIA_LATENCY_P95_MS = Summary('gaia_latency_p95_ms', '95th percentile of event latency in milliseconds')
GAIA_THREAT_MEAN = Gauge('gaia_threat_mean', 'Mean of the threat score')
GAIA_EMERGENCE = Gauge('gaia_emergence', 'Emergence score of the system')
GAIA_MEMORY_MB = Gauge('gaia_memory_mb', 'Memory usage in MB')

app = FastAPI(title="GAIA v6.7 API")
gaia = GAIA(Config())

@app.on_event("startup")
async def startup_event():
    # Start the Prometheus metrics server in a background thread
    start_http_server(9090)

@app.get("/health")
async def health():
    return {"status": "ok", "cycles": gaia.cycle_count}

@app.post("/event")
async def event(cpu: float = 0.5, memory: float = 0.5, network: float = 0.0):
    ev = {"cpu": cpu, "memory": memory, "network": network}
    result = await gaia.process_event(ev)

    # Update metrics
    GAIA_LATENCY_P95_MS.observe(result['latency_ms'])
    if gaia.threats:
        GAIA_THREAT_MEAN.set(np.mean(gaia.threats[-100:]))
    GAIA_EMERGENCE.set(gaia.emergence)
    GAIA_MEMORY_MB.set(gaia.memory_mb)

    return result

@app.get("/status")
async def status():
    return {"consciousness": gaia.consciousness, "cycles": gaia.cycle_count}