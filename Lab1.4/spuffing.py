import random
from ipaddress import IPv4Network


class Spuffer(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self, (random.randint(0x0b000000, 0xdf000000), random.randint(8, 24)), strict=False)


def key_sort(network):
    return int(network.netmask) * 2**32 + int(network.network_address)


def gen_pool(i):
    gen = [Spuffer() for i in range(i)]
    return sorted(gen, key=key_sort)


net1 = gen_pool(50)
for i in net1:
    print(i)
