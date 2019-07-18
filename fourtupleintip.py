from ipaddress import ip_network, ip_address
import csv
import time
import random

listOfPrivateIp = []
for k in ip_network("10.0.0.0/16"):
    listOfPrivateIp.append(str(k))
#print(len(listOfPrivateIp))
listOfPrivateIp_src = random.sample(listOfPrivateIp, 3500)
listOfPrivateIp = list(set(listOfPrivateIp)-set(listOfPrivateIp_src))
listOfPrivateIp_dst = random.sample(listOfPrivateIp,1500)
# listOfPrivateIp_src = listOfPrivateIp[:3500]
# listOfPrivateIp_dst = listOfPrivateIp[3501:5000]

listOfPublicIp = []
for k in ip_network("14.141.56.0/21"):
    listOfPublicIp.append(str(k))
#print(len(listOfPublicIp))
listOfPublicIp_src = random.sample(listOfPublicIp, 1500)
listOfPublicIp = list(set(listOfPublicIp)-set(listOfPublicIp_src))
listOfPublicIp_dst = random.sample(listOfPublicIp, 500)
src_ip = listOfPrivateIp_src + listOfPublicIp_src
dst_ip = listOfPrivateIp_dst + listOfPublicIp_dst
info = 'src_dst_ip_info.csv'
with open(info,'a') as infofile:
    writer = csv.writer(infofile)
    writer.writerows([[src_ip],[dst_ip]])

#print(len(src_ip))
#print(len(dst_ip))

ports_name_protocol = [(80, 'http', 'TCP'), (443, 'https', 'TCP'), (123, 'ntp', 'UDP'), (22, 'ssh', 'TCP'),
                       (53, 'dns', 'UDP'), (445, 'microsoft-ds', 'TCP'), (389, 'ldap', 'UDP'), (514, 'syslog', 'TCP'),
                       (137, 'netbios-ns', 'TCP'), (902, 'ideafarm-door', 'TCP'), (23, 'telnet', 'TCP'), (2049,'nfs','TCP'),
                       (88,'kerberos','TCP'), (111,'sunrpc', 'TCP'), (135,'epmap', 'TCP'), (1433, 'ms-sql-server', 'TCP'),
                       (3306,'mysql','TCP'), (67,'bootps','UDP'), (161, 'snmp', 'UDP'), (138, 'netbios-dgm', 'UDP'), (1434, 'ms-sql-m', 'UDP'),
                       (25,'smtp', 'TCP'), (21, 'ftp', 'TCP'), (179,'bgp','TCP'), (110,'pop3','TCP'), (500,'isakmp', 'UDP'),
                       (465,'igmpv3lite','TCP'), (19,'chargen','UDP'), (139,'netbios-ssn', 'TCP')]
i = 0
j = 0
fourTupleForPlanning = []
start = time.time()
while (len(fourTupleForPlanning) < 30000000):
    srcip = int(ip_address(src_ip[i]))
    dstip = int(ip_address(dst_ip[j]))
    rand = random.randint(1,100)
    if rand == 1:
        portsSet = random.sample(ports_name_protocol,2)
    elif rand == 2:
        portsSet = random.sample(ports_name_protocol,3)
    elif rand == 3:
        portsSet = random.sample(ports_name_protocol,4)
    else:
        portsSet = random.sample(ports_name_protocol[:10],4)
    for set in portsSet:
        port = set[0]
        portName = set[1]
        protocol = set[2]
        fourTupleForPlanning.append([srcip, dstip, port, portName, protocol])
        if len(fourTupleForPlanning) == 30000000:
            break
    j = j+1
    if (j == 2000):
        i = i + 1
        j = 0
filename = 'fourTupleIntIpPlanning.csv'
with open (filename, 'a') as file:
    writer = csv.writer(file)
    writer.writerows(fourTupleForPlanning)
end = time.time()
took = round(end-start,2)
print(f'inserted into {filename} 30million entries took {took} seconds')
