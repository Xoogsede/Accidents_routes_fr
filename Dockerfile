# app/Dockerfile

FROM python:3.9-slim AS slim_env

WORKDIR /app

RUN apt-get update && apt-get install nano less -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY ./Accueil.py .
COPY ./dict_correspondance.py .
COPY ./static .
COPY ./.streamlit .
COPY .streamlit/secrets.toml ./.streamlit/secrets.toml
COPY ./requirements.txt .
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.9-slim
RUN apt-get update && rm -rf /var/cache/apk/*
WORKDIR /app
COPY --from=slim_env /app/app.py /app/

ENV PASSWORD=PASSWORD
ENV neo4j_uri="bolt ://0.0.0.0:7687"

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]