import glob
import re
from ipaddress import IPv4Interface


def find_ip(string):
    if "ip address" in string:
        ip_plus_netmask = re.findall(r"((?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])(?:\.?|$)){4})", string)
        if len(ip_plus_netmask) == 2:
            ip_addr = ip_plus_netmask[0]+'/'+ip_plus_netmask[1]
            res = IPv4Interface(ip_addr)
            return res
    return


result = []

for filename in glob.glob(r"..\..\config_files\*.log"):
    with (open(filename) as fil):
        for string in fil:
            tango = find_ip(string.strip())
            if tango is not None:
                result.append(tango)

s_old = ""

for s in sorted(result):
    if s != s_old:
        print(s)
    s_old = s
