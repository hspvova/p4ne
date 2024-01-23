import paramiko
import time
import glob
import re

BUF_SIZE = 20000
TIMEOUT = 2
LOGIN_FILE = r'..\..\..\config_files\login'


def command_ssh(session, command_string, time_sleep):
    session.send("\n")
    session.recv(BUF_SIZE)
    session.send(command_string)
    time.sleep(time_sleep)
    return session


host_info_login = []

# Login info contains in "login" file.
# File must have 3 string:
#   1 - host ip
#   2 - login name
#   3 - password
for filename_login in glob.glob(LOGIN_FILE):
    with open(filename_login) as fil:
        for string in fil:
            host_info_login.append(string.replace("\n", ""))

ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_connection.connect(
    host_info_login[0],
    username=host_info_login[1],
    password=host_info_login[2],
    look_for_keys=False,
    allow_agent=False
)

session = ssh_connection.invoke_shell()

session = command_ssh(session, "terminal length 0\n", TIMEOUT)
session = command_ssh(session, "show interface\n", TIMEOUT*2)

answer = session.recv(BUF_SIZE).decode()
session.close()

result_interface_name = re.findall("\n([a-zA-z0-9]+)", answer)
result_input_byte = re.findall(r"[0-9]+ packets output, ([0-9]+ byte)", answer)
result_output_byte = re.findall(r"[0-9]+ packets output, ([0-9]+ byte)", answer)
i = 0

while i < len(result_input_byte):
    result = result_interface_name[i + 1] + "\ninput: " + result_input_byte[i] + "\noutput: " + result_output_byte[i]
    print(result)
    i += 1
