from fastapi import FastAPI
from gaia_v67 import GAIA, Config
import asyncio, random

app=FastAPI(title="GAIA v6.7 API")
gaia=GAIA(Config())

@app.get("/health")
async def health(): return {"status":"ok","cycles":gaia.cycle_count}

@app.post("/event")
async def event(cpu:float=0.5,memory:float=0.5,network:float=0.0):
    ev={"cpu":cpu,"memory":memory,"network":network}
    return await gaia.process_event(ev)

@app.get("/status")
async def status(): return {"consciousness":gaia.consciousness,"cycles":gaia.cycle_count}

from fastapi.responses import PlainTextResponse  # + import

@app.get("/metrics", response_class=PlainTextResponse)
async def metrics():
    # métriques simples lisibles par Prometheus
    m = gaia
    # sécurité: pas de tenant_id ici
    lines = [
        '# HELP gaia_cycles_total Total cycles processed',
        '# TYPE gaia_cycles_total counter',
        f'gaia_cycles_total {m.cycle_count}',

        '# HELP gaia_consciousness Current consciousness level (0..1)',
        '# TYPE gaia_consciousness gauge',
        f'gaia_consciousness {m.consciousness}',

        '# HELP gaia_threat_mean Approx last threat sample (event-driven)',
        '# TYPE gaia_threat_mean gauge',
        (f"gaia_threat_mean {gaia.threats[-1]:.6f}" if len(gaia.threats) else "gaia_threat_mean 0"),

        '# HELP gaia_latency_ms_last Last event latency in milliseconds',
        '# TYPE gaia_latency_ms_last gauge',
        (f"gaia_latency_ms_last {gaia.latencies[-1]:.6f}" if len(gaia.latencies) else "gaia_latency_ms_last 0"),
    ]
    return "\n".join(lines) + "\n"