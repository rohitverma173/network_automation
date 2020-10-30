from netmiko import Netmiko
import re
connection = Netmiko(host="10.10.19.187", port=22, username="lab",password="lab",device_type="cisco_ios")
output = connection.send_command("sh ip interface brief")
print(output)
pattern = re.compile(r'(Tunnel|Loopback)\d+\s+\d+[.]\d+[.]\d+[.]\d+')
matches = pattern.finditer(output)
for match in matches:
    print(match)
connection.disconnect()

