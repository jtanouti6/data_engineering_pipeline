FROM python:3.11-slim

# Installer outils + yq
RUN apt-get update && apt-get install -y bash curl jq && \
    curl -L https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -o /usr/bin/yq && \
    chmod +x /usr/bin/yq && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Étape 1 : installer les dépendances Python AVANT de copier tout le projet
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Étape 2 : copier uniquement ce dont on a besoin
COPY orchestration/ ./orchestration/
COPY monitoring/ ./monitoring/
COPY processing/ ./processing/
COPY config/ ./config/
COPY transformations/ ./transformations/
# etc., ou COPY . /app si tu veux tout

# CMD final
CMD ["bash", "orchestration/pipeline_master.sh"]
