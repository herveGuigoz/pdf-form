# PDF Form Filler

This is a simple project to fill PDF forms using [FastAPI](https://fastapi.tiangolo.com/) and [pypdfform](https://github.com/chinapandaman/PyPDFForm).

## Installation

1. Generate Credentials

Create a `.env` file with the following content:

```env
USERNAME=your_username
PASSWORD=your_password
```

2. Run docker containers

```sh
docker compose build --pull --no-cache
docker compose up --detach
```

## Production

```sh
docker compose -f compose.yaml -f compose.prod.yaml up -d --wait
```

## Poetry

### commands

```sh
poetry env info --path
```

```sh
poetry env list
```