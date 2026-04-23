# ---- Stage 1: Build ----
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---- Stage 2: Runtime ----
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

# Healthcheck (checks worker heartbeat in Redis)
HEALTHCHECK CMD python -c "import redis, os; r=redis.Redis(host=os.getenv('REDIS_HOST','redis'), port=6379); exit(0 if r.get('worker:heartbeat') else 1)"

CMD ["python", "worker.py"]
