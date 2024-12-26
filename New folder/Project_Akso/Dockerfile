FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libmariadb-dev-compat \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]
