
# Best way to connect network devices over SSH and send commands
# https://pynet.twb-tech.com/blog/netmiko-python-library.html
# https://ktbyers.github.io/netmiko/docs/netmiko/index.html#netmiko.ConnectHandler


from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host':   '172.16.140.145',
    'username': 'admin',
    'password': 'admin123',
    'port' : 22,          # optional, defaults to 22
    'secret': 'secret',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_device)

output = net_connect.send_command("show version")
print(output)

# creating an ACL
cfg_list = [
    "ip access-list extended TEST1",
    "permit ip any host 1.1.1.1",
    "permit ip any host 1.1.1.2",
    "permit ip any host 1.1.1.3",
    "permit ip any host 1.1.1.4",
    "permit ip any host 1.1.1.5",
]
# send command and save output to a variables
output = net_connect.send_config_set(cfg_list)
print(output)

# send command and directly display on the console
print(net_connect.send_command("show ip access-list"))

# save config with the 
net_connect.save_config()

# save config with "write memory" command


