FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir --break-system-packages -r /app/requirements.txt

COPY patches/__init__.py /usr/local/lib/python3.11/site-packages/flask_script/__init__.py

CMD ["bash"]