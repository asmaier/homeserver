from pyinfra.operations import server

for dir_name in ["umbrel"]:
    server.shell("docker-compose down --remove-orphans", _shell_executable="zsh -l", _chdir="docker/" + dir_name)

