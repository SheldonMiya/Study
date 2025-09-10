FROM ubuntu:24.04

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    php-cli php-mbstring php-xml php-curl php-zip \
    npm nodejs \
    git unzip apt-transport-https ca-certificates curl gnupg2 lsb-release \
    docker.io docker-compose-v2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*