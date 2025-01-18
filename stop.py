from pyinfra import host
from pyinfra.operations import server

DIR_DOCKER = "docker"
DIR_STORAGE = "storage"

home = host.get_fact(server.Home, "")
storage_path = home + "/" + DIR_STORAGE


for dir_name in ["umbrel"]:
    server.shell("docker-compose down --remove-orphans",
                 _shell_executable="zsh -l",
                 _chdir=DIR_DOCKER + "/" + dir_name,
                 _env={"DIR_STORAGE": storage_path})

