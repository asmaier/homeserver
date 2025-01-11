from pyinfra.operations import files, server

for dir_name in ["umbrel"]:
    compose = files.put("apps/" + dir_name + "/docker-compose.yml", "docker/" + dir_name + "/docker-compose.yml")
    if compose.changed:
        server.shell("docker-compose down --remove-orphans && docker-compose up -d",
                     _shell_executable="zsh -l", _chdir="docker/" + dir_name)

