import paramiko
import os

hostname = "52.47.84.139"
port = 22
user = 'admin'

try:
    client = paramiko.SSHClient()
    client.load_host_keys('mxmd.pem')
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname, port=port, username=user)

    while True:
        try:
            cmd = input("$> ")
            if cmd == "exit" : break
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break
except Exception as err:
    print(str(err))