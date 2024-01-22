import glob
import re
from ipaddress import IPv4Interface

FILES_FOLDER = r"..\..\..\config_files\*.log"


def find_ip(string):
    if "ip address" in string:
        ip_plus_netmask = re.findall(
            r"((?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])(?:\.?|$)){4})",
            string
        )
        if len(ip_plus_netmask) == 2:
            ip_addr = ip_plus_netmask[0]+'/'+ip_plus_netmask[1]
            res = IPv4Interface(ip_addr)
            return res
    return None


result = []

for filename in glob.glob(FILES_FOLDER):
    with (open(filename) as fil):
        for string in fil:
            tango = find_ip(string.strip())
            if tango:
                result.append(tango)



for s in result:
    print(s)