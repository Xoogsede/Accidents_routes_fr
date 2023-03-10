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
COPY ./pages/* ./pages/
COPY ./image .
COPY ./__init__.py .
COPY ./fonctions.py .
COPY ./setup.sh .
COPY ./Procfile .
COPY ./queries.py .
COPY ./README.md .
COPY ./LICENSE .
COPY ./static ./static
COPY ./.streamlit/* ./.streamlit/
COPY ./requirements.txt .

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

ENV neo4j_uri="bolt ://0.0.0.0:7687"

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "Accueil.py", "--server.port=8501", "--server.address=0.0.0.0"]