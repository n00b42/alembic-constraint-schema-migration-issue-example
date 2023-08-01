#!/bin/bash

docker-compose up -d
poetry install
rm -f alembic/versions/*.py
poetry run alembic revision --autogenerate -m "REV1"
poetry run alembic upgrade head
poetry run alembic revision --autogenerate -m "REV2"
poetry run alembic upgrade head
poetry run alembic revision --autogenerate -m "REV3"
poetry env remove --all
docker-compose down
printf "\n\nGenerated Revisions:\n\n"
ls alembic/versions/*.py
