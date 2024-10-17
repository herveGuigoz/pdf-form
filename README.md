# PDF Form Filler

This is a simple project to fill PDF forms using FastAPI and pypdfform.

## Installation

1. Generate JWT key

Open your terminal and write the command given below, this will give you a secret key which we will for authentication.

```sh
echo "JWT_SECRET=$(openssl rand -hex 32)" >> .env
```

2. Run docker containers

```sh
docker compose build --pull --no-cache
docker compose up --detach
```

## Commands

#### Poetry commands

```sh
poetry env info --path
```

```sh
poetry env list
```

## Production

```sh
docker compose -f compose.yaml up -d --wait
```