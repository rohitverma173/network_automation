import paramiko
import time
import re
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname='10.10.19.187',port='22',username='lab',password='lab',
                   look_for_keys=False,allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send("terminal length 0\n")
shell.send("sh module\n")
time.sleep(2)
output = shell.recv(10000).decode(encoding='UTF=8')
print(output)
stdin, stdout, stderr = ssh_client.exec_command("show version\n")

shell.close()