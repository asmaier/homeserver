from pyinfra.operations import server

for dir_name in ["watchtower", "portainer", "pihole", "filebrowser"]:
    server.shell("docker-compose down --remove-orphans && docker-compose up -d",
                 _shell_executable="zsh -l", _chdir="docker/" + dir_name)

