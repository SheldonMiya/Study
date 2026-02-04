# projectC-uv

devcontainer + Python + uv のシンプルなサンプルプロジェクト

## 特徴

- **devcontainer環境**: Docker を使った開発環境
- **Ubuntu 最新**: ベースイメージとして Ubuntu 最新版を使用
- **uv**: Rust で実装された高速な Python パッケージマネージャーをインストール
- **VS Code 統合**: Python 拡張機能が事前に設定されている

## プロジェクト構成

```
projectC-uv/
├── .devcontainer/
│   ├── Dockerfile           # コンテナイメージの定義
│   └── devcontainer.json    # devcontainer設定
├── src/
│   └── main.py              # サンプル Python コード
├── pyproject.toml           # プロジェクト設定
└── README.md                # このファイル
```

## セットアップ

### 前提条件

- Docker Desktop がインストールされていること
- VS Code が インストールされていること
- VS Code Remote - Containers 拡張機能がインストールされていること

### 環境構築手順

1. **VS Code でプロジェクトを開く**

   ```bash
   cd projectC-uv
   code .
   ```

2. **devcontainer で再度開く**

   - コマンドパレット (`Ctrl+Shift+P` / `Cmd+Shift+P`) を開く
   - "Reopen in Container" を検索して実行

3. **Docker コンテナの構築と起動**

   初回の起動時は、Docker コンテナがビルドされ、数分かかる場合があります。

## 使用方法

### サンプルコードの実行

devcontainer 内のターミナルで以下を実行：

```bash
python3 src/main.py
```

### uv を使用したパッケージ管理

```bash
# パッケージの追加
uv pip install requests

# 依存関係のインストール
uv pip install -e .

# 開発用依存関係のインストール
uv pip install -e ".[dev]"
```

### Python のバージョン確認

```bash
python3 --version
uv --version
```

## Docker イメージの詳細

`Dockerfile` では以下の処理を行っています：

- Ubuntu の最新イメージをベースとして使用
- Python 3 と pip をインストール
- `pip install --no-cache-dir --break-system-packages uv` で uv をインストール
- `/workspace` を作業ディレクトリとして設定

## トラブルシューティング

### uv が見つからない場合

devcontainer を再度開き、以下を実行：

```bash
pip install --no-cache-dir --break-system-packages uv
```

### パッケージインストール時にエラーが発生する場合

`--break-system-packages` オプションを使用してください：

```bash
uv pip install --break-system-packages パッケージ名
```

## ライセンス

MIT

## 参考リンク

- [UV GitHub Repository](https://github.com/astral-sh/uv)
- [Dev Containers](https://containers.dev/)
- [VS Code Remote Containers](https://code.visualstudio.com/docs/remote/containers)
