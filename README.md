# homeserver

Code for installing and managing my homeserver.
Each app has its own directory and docker-compose.yml file as suggested by 
[Reddit](https://www.reddit.com/r/selfhosted/comments/1cb7jhg/one_big_dockercompose_file_or_multiple_smaller/).
This allows to separate the data of each app and also allows top start and stop each app
individually.

## Setup project

    $ uv sync

## Setup (or update) apps on homeserver

    $ uv run pyinfra hosts.py setup.py

## Stop all apps on homeserver

    $ uv run pyinfra hosts.py stop.py

## Restart all apps on homeserver

    $ uv run pyinfra hosts.py restart.py

## Run linter

    $ uv run ruff check

## Teardown project

    $ rm -r .venv uv.lock