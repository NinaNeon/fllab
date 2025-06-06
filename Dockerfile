FROM arm64v8/python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential libopenblas-dev libssl-dev libffi-dev git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install torch==2.2.2 torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Trust the mounted code repo
RUN git config --global --add safe.directory /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt