from pyinfra.operations import server

for dir_name in ["watchtower", "portainer", "pihole", "nextcloud", "filebrowser"]:
    server.shell("docker-compose down --remove-orphans", _shell_executable="zsh -l", _chdir="docker/" + dir_name)

