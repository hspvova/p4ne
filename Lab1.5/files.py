import glob


result = []
res = []

for filename in glob.glob(r"..\..\..\config_files\*.log"):
    with open(filename) as fil:
        for string in fil:
            if "ip address" in string:
                lists = string.split(" ")
                for word in lists:
                    ip_oct = word.split(".")
                    if len(ip_oct) == 4 and ip_oct[0].isnumeric():
                        ip = ".".join(ip_oct)
                        res.append(ip)
                if len(res) == 2:
                    string = " ".join(res)
                    result.append(string.strip())
                res = []
s_old = ""

for s in sorted(result):
    if s != s_old:
        print(s)
    s_old = s
