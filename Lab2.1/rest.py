import requests
import pprint
import glob

LOGIN_FILE = r'..\..\..\config_files\login'
# Login info contains in "login" file.
# File must have 3 string:
#   1 - host ip
#   2 - login name
#   3 - password
host_info_login = []
for filename_login in glob.glob(LOGIN_FILE):
    with open(filename_login) as fil:
        for string in fil:
            host_info_login.append(string.replace("\n", ""))

headers = {
    "accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

r = requests.get(
    'https://' + host_info_login[0] + '/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces',
    auth=(host_info_login[1], host_info_login[2]),
    headers=headers,
    verify=False
)
interface = r.json().get(
    "Cisco-IOS-XE-interfaces-oper:interfaces"
).get("interface")
keys_statistics = ["in-unicast-pkts", "in-octets", "out-unicast-pkts", "out-octets"]
result = {i['name']: {k: i["statistics"][k] for k in keys_statistics} for i in interface}
pprint.pprint(result)
