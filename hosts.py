import getpass
ssh_password = getpass.getpass(prompt="SSH password: ")

hosts = [
    ("192.168.178.30", {"ssh_user": "homeserver", "ssh_password": ssh_password}),
]
