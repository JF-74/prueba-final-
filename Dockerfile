FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /workspace/data/raw && \
    curl -L "https://gist.github.com/nnbphuong/38db511db14542f3ba9ef16e69d3814c/raw/3a77ff9d97c504d3ec3210b12fde7242b8c6ab63/Superstore.csv" \
     -o data/raw/superstore.csv
COPY . .

ENV PYTHONPATH=/workspace
ENV PREFECT_HOME=/workspace/.prefect
