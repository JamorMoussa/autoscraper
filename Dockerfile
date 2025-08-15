FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app

COPY .python-version pyproject.toml uv.lock ./ 

RUN uv sync

EXPOSE 8000

COPY . . 

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]

