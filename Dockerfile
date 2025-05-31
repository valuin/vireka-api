FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

RUN apt-get update && apt-get install -y \
    curl \
    libglib2.0-0 \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

EXPOSE ${PORT:-8000}

CMD ["sh", "-c", "uv run gunicorn -b 0.0.0.0:${PORT:-8000} -k uvicorn.workers.UvicornWorker src.api:app"]
