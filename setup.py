from pyinfra import host
from pyinfra.operations import files, server

DIR_DOCKER = "docker"
DIR_STORAGE = "storage"

home = host.get_fact(server.Home, "")
storage_path = home + "/" + DIR_STORAGE

files.directory(DIR_DOCKER)
files.directory(DIR_STORAGE)

for dir_name in ["umbrel"]:
    compose = files.put("apps/" + dir_name + "/docker-compose.yml", DIR_DOCKER + "/" + dir_name + "/docker-compose.yml")
    if compose.changed:
        server.shell("docker-compose down --remove-orphans && docker-compose up -d",
                     _shell_executable="zsh -l",
                     _chdir=DIR_DOCKER + "/" + dir_name,
                     _env={"DIR_STORAGE": storage_path})

