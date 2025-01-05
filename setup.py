from pyinfra.operations import files, server

for dir_name in ["watchtower", "portainer", "pihole", "filebrowser"]:
    compose = files.put("apps/" + dir_name + "/docker-compose.yml", "docker/" + dir_name + "/docker-compose.yml")
    if dir_name == "filebrowser":
        files.put("apps/" + dir_name + "/filebrowser.json", "docker/" + dir_name + "/filebrowser.json")
        files.put("apps/" + dir_name + "/filebrowser.db", "docker/" + dir_name + "/filebrowser.db")
    if compose.changed:
        server.shell("docker-compose down --remove-orphans && docker-compose up -d",
                     _shell_executable="zsh -l", _chdir="docker/" + dir_name)

