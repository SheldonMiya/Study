FROM ubuntu:latest

# タイムゾーンの設定（インタラクティブプロンプトを回避）
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# システムパッケージの更新とPython、pip関連のインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# uvのインストール
RUN pip install --no-cache-dir --break-system-packages uv

# 作業ディレクトリの設定
WORKDIR /workspace

# コンテナ起動時のデフォルトコマンド
CMD ["/bin/bash"]
