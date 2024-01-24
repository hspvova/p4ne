from flask import Flask
import glob
import re
from ipaddress import IPv4Interface

app = Flask(__name__)
FILES_FOLDER = r"..\..\..\config_files\*.log"


def find_ip(string):
    if "ip address" in string:
        ip_plus_netmask = re.findall(
            r"((?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])(?:\.?|$)){4})",
            string
        )
        if len(ip_plus_netmask) == 2:
            ip_addr = ip_plus_netmask[0] + '/' + ip_plus_netmask[1]
            res = IPv4Interface(ip_addr)
            return res
    return None


@app.route('/')
@app.route('/index')
def index():
    return "Server is up"


@app.route('/configs')
def configs():
    global config_host
    return str(config_host.keys())


@app.route('/configs/<hostname>')
def configs_host(hostname):
    global config_host
    return str(config_host[hostname].items())


config_host = {}
hostname = ""
ips = []
i = 0

if __name__ == "__main__":
    for filename in glob.glob(FILES_FOLDER):
        with (open(filename) as fil):
            for string in fil:
                if ("hostname" in string) or ("sysname" in string):
                    host = re.match(r"^ *(?:host|sys)name ([^ ]*)$", string)
                    if host:
                        hostname = host.group(1).replace("\n","")
                else:
                    tango = find_ip(string.strip())
                    if tango:
                        ips.append(tango)
            config_host[hostname] = {str("ip"+str(i)): str(ips[i]) for i in range(0, len(ips))}
            ips = []
    app.run(port=80, debug=True)
