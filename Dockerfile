# GAIA v6.7 Production
FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY gaia_v67.py gaia_api.py ./

EXPOSE 8000 9090

CMD ["uvicorn", "gaia_api:app", "--host", "0.0.0.0", "--port", "8000"]