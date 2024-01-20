import glob
import re
from ipaddress import IPv4Interface


def find_ip(string):
    ip_plus_netmask = re.findall(r"((?:(?:[0-9]{1,3})(?:\.?|$)){4})", string)
    res = 0
    if len(ip_plus_netmask) == 2:
        ip_addr = ip_plus_netmask[0]+'/'+ip_plus_netmask[1]
        res = IPv4Interface((ip_addr))
    return res


result = []

for filename in glob.glob(r"..\..\config_files\*.log"):
    with (open(filename) as fil):
        for string in fil:
            if "ip address" in string:
                tango = find_ip(string.strip())
                if tango != 0:
                    result.append(tango)

s_old = ""

for s in sorted(result):
    if s != s_old:
        print(s)
    s_old = s
