from pysnmp.hlapi import *

snmp_name = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_interface = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')
resault = getCmd(SnmpEngine(),
                 CommunityData('public', mpModel=0),
                 UdpTransportTarget(('10.31.70.209', 161)),
                 ContextData(),
                 ObjectType(snmp_name))

resault2 = nextCmd(SnmpEngine(),
                 CommunityData('public', mpModel=0),
                 UdpTransportTarget(('10.31.70.209', 161)),
                 ContextData(),
                 ObjectType(snmp_interface),
                 lexicographicMode=False)

for answer in resault:
   for s in answer[3]:
       print(s)

for answer in resault2:
   for s in answer[3]:
       print(s)