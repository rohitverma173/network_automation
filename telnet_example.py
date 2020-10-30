from telnetlib import Telnet
import time

host_ip = "10.10.19.178"
port = 23
uname = "lab"
passwd = "lab"

tn = Telnet(host=host_ip, port=port)
tn.read_until(b"Username: ")
tn.write(uname.encode() + b"\n")
tn.read_until(b"Password: ")
tn.write(passwd.encode() + b"\n")
tn.write(b"terminal length 0\n")
tn.write(b"sh ip interface brief\n")
tn.write(b"exit\n")
time.sleep(1)

output = tn.read_all()
output = output.decode()
print(output)
