import csv
import time
import datetime
import random
from ipaddress import ip_network, ip_address
import pandas as pd
import sys


total_events = 0
modelkey_oid_range = range(9876543219876,9883743219876)
collector_id_range = range(9883743219876,9890943219876)
attribute_model_oid_range = range(9890943219876,9898143219876)
firewall_manager_model_oid_range = range(9898143219876,9905343219876)
reporter_entity_oid_range = range(9905343219876,9912543219876)
flowdomain_modelkey_oid_range = range(9912543219876,9919743219876)
srvcEP_oid_range = range(9919743219876,9926943219876)
lastactivity_range = range(3647281617, 10847281617)


event_date = datetime.datetime(2019, 8, 26)


metaDataFile = 'metaDataForPlanning.csv'
with open(metaDataFile) as csvIPData:
    ipMetaData = list(csv.reader(csvIPData))
privateIpList = [int(ipMetaData[i][0]) for i in range(50000)]


def fetch_metadata(eachtuple, tuple_count):
    sip = eachtuple[0]
    dip = eachtuple[1]
    port = eachtuple[2]
    portname = eachtuple[3]
    protocol = eachtuple[4]
    flow_tag_list = ['TAG_TRAFFIC_TYPE_UNKNOWN', 'TAG_INTERNET_TRAFFIC', 'TAG_EAST_WEST_TRAFFIC', 'TAG_VM_VM_TRAFFIC', 'TAG_VM_PHY_TRAFFIC', 'TAG_PHY_PHY_TRAFFIC', 'TAG_SRC_IP_VMKNIC', 'TAG_DST_IP_VMKNIC', 'TAG_SRC_IP_ROUTER_INT', 'TAG_DST_IP_ROUTER_INT', 'TAG_SRC_IP_VM', 'TAG_DST_IP_VM', 'TAG_SRC_IP_INTERNET', 'TAG_DST_IP_INTERNET', 'TAG_SRC_IP_PHYSICAL', 'TAG_DST_IP_PHYSICAL', 'TAG_SAME_HOST', 'TAG_DIFF_HOST', 'TAG_COMMON_HOST_INFO_UNKNOWN', 'TAG_SHARED_SERVICE', 'TAG_NOT_SHARED_SERVICE', 'TAG_NETWORK_SWITCHED', 'TAG_NETWORK_ROUTED', 'TAG_NETWORK_UNKNOWN', 'TAG_SRC_IP_VTEP', 'TAG_DST_IP_VTEP', 'TAG_UNICAST', 'TAG_BROADCAST', 'TAG_MULTICAST', 'TAG_SRC_IP_LINK_LOCAL', 'TAG_DST_IP_LINK_LOCAL', 'TAG_SRC_IP_CLASS_E', 'TAG_DST_IP_CLASS_E', 'TAG_SRC_IP_CLASS_A_RESERVED', 'TAG_DST_IP_CLASS_A_RESERVED', 'TAG_INVALID_IP_PACKETS', 'TAG_NOT_ANALYZED', 'TAG_GENERIC_INTERNET_SRC_IP', 'TAG_SNAT_DNAT_FLOW', 'TAG_NATTED', 'TAG_MULTINICS', 'TAG_MULTI_NATRULE', 'TAG_SRC_VC', 'TAG_DST_VC', 'TAG_SRC_AWS', 'TAG_DST_AWS', 'TAG_WITHIN_DC', 'TAG_DIFF_DC', 'TAG_SRC_IP_IN_SNAT_RULE_TARGET', 'TAG_DST_IP_IN_DNAT_RULE_ORIGINAL', 'TAG_SRC_IP_MULTI_NAT_RULE', 'TAG_DNAT_IP_MULTI_NAT_RULE', 'DEPRECATED_TAG_DST_IP_IN_SNAT_RULE_TARGET', 'DEPRECATED_TAG_SRC_IP_IN_DNAT_RULE_ORIGINAL', 'TAG_INVALID_IP_DOMAIN', 'TAG_WITHIN_VPC', 'TAG_DIFF_VPC', 'TAG_SRC_IP_IN_MULTIPLE_SUBNETS', 'TAG_DST_IP_IN_MULTIPLE_SUBNETS', 'TAG_SFLOW', 'TAG_PRE_NAT_FLOW', 'TAG_POST_NAT_FLOW', 'TAG_LOGICAL_FLOW', 'TAG_SRC_K8S_POD', 'TAG_DST_K8S_POD', 'TAG_POD_POD_TRAFFIC', 'TAG_VM_POD_TRAFFIC', 'TAG_POD_PHYSICAL_TRAFFIC']
    modelKey = modelkey_oid_range[tuple_count]
    collector_id = collector_id_range[tuple_count]
    shared = random.choice([1, 0])
    port_display = '[' + str(port) + '] ' + portname
    if ((int(sip) not in privateIpList) and (int(dip) not in privateIpList)):
        flow_name = sip + dip + '-' + portname + '-' + protocol
        flow_data = [flow_name, 8912345, 515, modelKey, port, port, str(port), portname, port_display, protocol, 32, int(sip), '255.255.255.255', str(ip_address(int(sip))), str(ip_network(int(sip))), sip, sip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 32, dip, '255.255.255.255', str(ip_address(int(dip))), str(ip_network(int(dip))), dip, dip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 'INTERNET_TRAFFIC', shared, 'UNKNOWN_LAYER', '', '', '', '', '', '', '', 'SUBNET', 1, '', '', '', '', '', '', '', '', '', '', 'SUBNET', 1, '', '', '', '', random.sample(flow_tag_list, 4), [flow_name, '', ''], ['flows', 'traffic'], ['admin@vmware.com', 'root@vmware.com'], ['vmware@vmware.com', 'vrni@vmware.com'], 'ALLOW', 'RID-' + str(modelKey), collector_id, 'AT_RULE' + str(modelKey), 7, attribute_model_oid_range[tuple_count], 'AT_firewall_manager' + str(modelKey), 8, firewall_manager_model_oid_range[tuple_count], collector_id, 'KCC0IABACBAA', 'PROTECTED', 'ALLOW', '', '', '', '', '', '', '', '', '', '', collector_id, 'reporter' + str(modelKey), 603, reporter_entity_oid_range[tuple_count], collector_id, '', '', '', '', '', '', '', '', '', '', '', '', collector_id, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', dip + port_display, 6065, srvcEP_oid_range[tuple_count], '', '', '', '', '', '', 'GLOBAL', 658, flowdomain_modelkey_oid_range[tuple_count], '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        #print('net to net')
    elif ((int(sip) not in privateIpList) and (int(dip) in privateIpList)):
        q = privateIpList.index(int(dip))
        dst_vm_name = str(ipMetaData[q][1])
        flow_name = sip + dst_vm_name + '-' + portname + '-' + protocol
        flow_data = [flow_name, 8912345, 515, modelKey, port, port, str(port), portname, port_display, protocol, 32, int(sip), '255.255.255.255', str(ip_address(int(sip))), str(ip_network(int(sip))), sip, sip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 32, dip, '255.255.255.255', str(ip_address(int(dip))), str(ip_network(int(dip))), dip, dip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 'INTERNET_TRAFFIC', shared, 'UNKNOWN_LAYER', '', '', '', '', '', '', '', 'SUBNET', 1, '', '', '', ipMetaData[q][6], ipMetaData[q][4], ipMetaData[q][5], ipMetaData[q][7], ipMetaData[q][8], ipMetaData[q][9], ipMetaData[q][10], 'SUBNET', 1, ipMetaData[q][13], ipMetaData[q][14], ipMetaData[q][15], '', random.sample(flow_tag_list, 4), [flow_name, '', dst_vm_name], ['flows', 'traffic'], ['admin@vmware.com', 'root@vmware.com'], ['vmware@vmware.com', 'vrni@vmware.com'], 'ALLOW', 'RID-' + str(modelKey), collector_id, 'AT_RULE' + str(modelKey), 7, attribute_model_oid_range[tuple_count], 'AT_firewall_manager' + str(modelKey), 8, firewall_manager_model_oid_range[tuple_count], collector_id, 'KCC0IABACBAA', 'PROTECTED', 'ALLOW', '', '', '', '', '', ipMetaData[q][19], ipMetaData[q][20], ipMetaData[q][21], ipMetaData[q][22], ipMetaData[q][23], collector_id, 'reporter' + str(modelKey), 603, reporter_entity_oid_range[tuple_count], collector_id, '', '', '', '', '', '', '', '', '', '', '', '', collector_id, ipMetaData[q][24], ipMetaData[q][25], ipMetaData[q][26], ipMetaData[q][27], ipMetaData[q][28], ipMetaData[q][29], ipMetaData[q][30], ipMetaData[q][31], ipMetaData[q][32], ipMetaData[q][33], ipMetaData[q][34], ipMetaData[q][35], '', '', '', ipMetaData[q][36], ipMetaData[q][37], ipMetaData[q][38], '', '', '', ipMetaData[q][39], ipMetaData[q][40], ipMetaData[q][41], '', '', '', dst_vm_name, ipMetaData[q][2], ipMetaData[q][3], '', '', '', ipMetaData[q][42], ipMetaData[q][43], ipMetaData[q][44], '', '', '', ipMetaData[q][45], ipMetaData[q][46], ipMetaData[q][47], '', '', '', ipMetaData[q][48], ipMetaData[q][49], ipMetaData[q][50], '', '', '', ipMetaData[q][51], ipMetaData[q][52], ipMetaData[q][53], '', '', '', ipMetaData[q][54], ipMetaData[q][55], ipMetaData[q][56], '', '', '', ipMetaData[q][57], ipMetaData[q][58], ipMetaData[q][59], '', '', '', ipMetaData[q][60], ipMetaData[q][61], ipMetaData[q][62], '', '', '', ipMetaData[q][63], ipMetaData[q][64], ipMetaData[q][65], '', '', '', ipMetaData[q][16], ipMetaData[q][17], ipMetaData[q][18], dip + port_display, 6065, srvcEP_oid_range[tuple_count], '', '', '', ipMetaData[q][66], ipMetaData[q][67], ipMetaData[q][68], 'GLOBAL', 658, flowdomain_modelkey_oid_range[tuple_count], '', '', '', ipMetaData[q][69], ipMetaData[q][70], ipMetaData[q][71], '', '', '', ipMetaData[q][72], ipMetaData[q][73], ipMetaData[q][74], '', '', '', ipMetaData[q][75], ipMetaData[q][76], ipMetaData[q][77], '', '', '', ipMetaData[q][78], ipMetaData[q][79], ipMetaData[q][80], '', '', '', ipMetaData[q][81], ipMetaData[q][82], ipMetaData[q][83]]
        #print('net to private')
    elif ((int(sip) in privateIpList) and (int(dip) not in privateIpList)):
        p = privateIpList.index(int(sip))
        src_vm_name = str(ipMetaData[p][1])
        flow_name = src_vm_name + dip + '-' + portname + '-' + protocol
        flow_data = [flow_name, 8912345, 515, modelKey, port, port, str(port), portname, port_display, protocol, 32, int(sip), '255.255.255.255', str(ip_address(int(sip))), str(ip_network(int(sip))), sip, sip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 32, dip, '255.255.255.255', str(ip_address(int(dip))), str(ip_network(int(dip))), dip, dip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 'INTERNET_TRAFFIC', shared, 'UNKNOWN_LAYER', ipMetaData[p][6], ipMetaData[p][4], ipMetaData[p][5], ipMetaData[p][7], ipMetaData[p][8], ipMetaData[p][9], ipMetaData[p][10], 'SUBNET', 1, ipMetaData[p][13], ipMetaData[p][14], ipMetaData[p][15], '', '', '', '', '', '', '', 'SUBNET', 1, '', '', '', int(ipMetaData[p][16] == ''), random.sample(flow_tag_list, 4), [flow_name, '', ''], ['flows', 'traffic'], ['admin@vmware.com', 'root@vmware.com'], ['vmware@vmware.com', 'vrni@vmware.com'], 'ALLOW', 'RID-' + str(modelKey), collector_id, 'AT_RULE' + str(modelKey), 7, attribute_model_oid_range[tuple_count], 'AT_firewall_manager' + str(modelKey), 8, firewall_manager_model_oid_range[tuple_count], collector_id, 'KCC0IABACBAA', 'PROTECTED', 'ALLOW', ipMetaData[p][19], ipMetaData[p][20], ipMetaData[p][21], ipMetaData[p][22], ipMetaData[p][23], '', '', '', '', '', collector_id, 'reporter' + str(modelKey), 603, reporter_entity_oid_range[tuple_count], collector_id, ipMetaData[p][24], ipMetaData[p][25], ipMetaData[p][26], ipMetaData[p][27], ipMetaData[p][28], ipMetaData[p][29], ipMetaData[p][30], ipMetaData[p][31], ipMetaData[p][32], ipMetaData[p][33], ipMetaData[p][34], ipMetaData[p][35], collector_id, '', '', '', '', '', '', '', '', '', '', '', '', ipMetaData[p][36], ipMetaData[p][37], ipMetaData[p][38], '', '', '', ipMetaData[p][39], ipMetaData[p][40], ipMetaData[p][41], '', '', '', src_vm_name, ipMetaData[p][2], ipMetaData[p][3], '', '', '', ipMetaData[p][42], ipMetaData[p][43], ipMetaData[p][44], '', '', '', ipMetaData[p][45], ipMetaData[p][46], ipMetaData[p][47], '', '', '', ipMetaData[p][48], ipMetaData[p][49], ipMetaData[p][50], '', '', '', ipMetaData[p][51], ipMetaData[p][52], ipMetaData[p][53], '', '', '', ipMetaData[p][54], ipMetaData[p][55], ipMetaData[p][56], '', '', '', ipMetaData[p][57], ipMetaData[p][58], ipMetaData[p][59], '', '', '', ipMetaData[p][60], ipMetaData[p][61], ipMetaData[p][62], '', '', '', ipMetaData[p][63], ipMetaData[p][64], ipMetaData[p][65], '', '', '', ipMetaData[p][16], ipMetaData[p][17], ipMetaData[p][18], '', '', '', dip + port_display, 6065, srvcEP_oid_range[tuple_count], ipMetaData[p][66], ipMetaData[p][67], ipMetaData[p][68], '', '', '', 'GLOBAL', 658, flowdomain_modelkey_oid_range[tuple_count], ipMetaData[p][69], ipMetaData[p][70], ipMetaData[p][71], '', '', '', ipMetaData[p][72], ipMetaData[p][73], ipMetaData[p][74], '', '', '', ipMetaData[p][75], ipMetaData[p][76], ipMetaData[p][77], '', '', '', ipMetaData[p][78], ipMetaData[p][79], ipMetaData[p][80], '', '', '', ipMetaData[p][78], ipMetaData[p][79], ipMetaData[p][80], '', '', '']
        #print('priv to internet')
    else:
        p = privateIpList.index(int(sip))
        src_vm_name = str(ipMetaData[p][1])
        q = privateIpList.index(int(dip))
        dst_vm_name = str(ipMetaData[q][1])
        flow_name = src_vm_name + dst_vm_name + '-' + portname + '-' + protocol
        if (ipMetaData[p][7] == ipMetaData[q][7]):
            networkLayer = 'LAYER_2'
        else:
            networkLayer = 'LAYER_3'
        flow_data = [flow_name, 8912345, 515, modelKey, port, port, str(port), portname, port_display, protocol, 32, int(sip), '255.255.255.255', str(ip_address(int(sip))), str(ip_network(int(sip))), sip, sip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 32, dip, '255.255.255.255', str(ip_address(int(dip))), str(ip_network(int(dip))), dip, dip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 'EAST_WEST_TRAFFIC', shared, networkLayer, ipMetaData[p][6], ipMetaData[p][4], ipMetaData[p][5], ipMetaData[p][7], ipMetaData[p][8], ipMetaData[p][9], ipMetaData[p][10], 'SUBNET', 1, ipMetaData[p][13], ipMetaData[p][14], ipMetaData[p][15], ipMetaData[q][6], ipMetaData[q][4], ipMetaData[q][5], ipMetaData[q][7], ipMetaData[q][8], ipMetaData[q][9], ipMetaData[q][10], 'SUBNET', 1, ipMetaData[q][13], ipMetaData[q][14], ipMetaData[q][15], int(ipMetaData[p][16] == ipMetaData[q][16]), random.sample(flow_tag_list, 4), [flow_name, src_vm_name, dst_vm_name], ['flows', 'traffic'], ['admin@vmware.com', 'root@vmware.com'], ['vmware@vmware.com', 'vrni@vmware.com'], 'ALLOW', 'RID-' + str(modelKey), collector_id, 'AT_RULE' + str(modelKey), 7, attribute_model_oid_range[tuple_count], 'AT_firewall_manager' + str(modelKey), 8, firewall_manager_model_oid_range[tuple_count], collector_id, 'KCC0IABACBAA', 'PROTECTED', 'ALLOW', ipMetaData[p][19], ipMetaData[p][20], ipMetaData[p][21], ipMetaData[p][22], ipMetaData[p][23], ipMetaData[q][19], ipMetaData[q][20], ipMetaData[q][21], ipMetaData[q][22], ipMetaData[q][23], collector_id, 'reporter' + str(modelKey), 603, reporter_entity_oid_range[tuple_count], collector_id, ipMetaData[p][24], ipMetaData[p][25], ipMetaData[p][26], ipMetaData[p][27], ipMetaData[p][28], ipMetaData[p][29], ipMetaData[p][30], ipMetaData[p][31], ipMetaData[p][32], ipMetaData[p][33], ipMetaData[p][34], ipMetaData[p][35], collector_id, ipMetaData[q][24], ipMetaData[q][25], ipMetaData[q][26], ipMetaData[q][27], ipMetaData[q][28], ipMetaData[q][29], ipMetaData[q][30], ipMetaData[q][31], ipMetaData[q][32], ipMetaData[q][33], ipMetaData[q][34], ipMetaData[q][35], ipMetaData[p][36], ipMetaData[p][37], ipMetaData[p][38], ipMetaData[q][36], ipMetaData[q][37], ipMetaData[q][38], ipMetaData[p][39], ipMetaData[p][40], ipMetaData[p][41], ipMetaData[q][39], ipMetaData[q][40], ipMetaData[q][41], src_vm_name, ipMetaData[p][2], ipMetaData[p][3], dst_vm_name, ipMetaData[q][2], ipMetaData[q][3], ipMetaData[p][42], ipMetaData[p][43], ipMetaData[p][44], ipMetaData[q][42], ipMetaData[q][43], ipMetaData[q][44], ipMetaData[p][45], ipMetaData[p][46], ipMetaData[p][47], ipMetaData[q][45], ipMetaData[q][46], ipMetaData[q][47], ipMetaData[p][48], ipMetaData[p][49], ipMetaData[p][50], ipMetaData[q][48], ipMetaData[q][49], ipMetaData[q][50], ipMetaData[p][51], ipMetaData[p][52], ipMetaData[p][53], ipMetaData[q][51], ipMetaData[q][52], ipMetaData[q][53], ipMetaData[p][54], ipMetaData[p][55], ipMetaData[p][56], ipMetaData[q][54], ipMetaData[q][55], ipMetaData[q][56], ipMetaData[p][57], ipMetaData[p][58], ipMetaData[p][59], ipMetaData[q][57], ipMetaData[q][58], ipMetaData[q][59], ipMetaData[p][60], ipMetaData[p][61], ipMetaData[p][62], ipMetaData[q][60], ipMetaData[q][61], ipMetaData[q][62], ipMetaData[p][63], ipMetaData[p][64], ipMetaData[p][65], ipMetaData[q][63], ipMetaData[q][64], ipMetaData[q][65], ipMetaData[p][16], ipMetaData[p][17], ipMetaData[p][18], ipMetaData[q][16], ipMetaData[q][17], ipMetaData[q][18], dip + port_display, 6065, srvcEP_oid_range[tuple_count], ipMetaData[p][66], ipMetaData[p][67], ipMetaData[p][68], ipMetaData[q][66], ipMetaData[q][67], ipMetaData[q][68], 'GLOBAL', 658, flowdomain_modelkey_oid_range[tuple_count], ipMetaData[p][69], ipMetaData[p][70], ipMetaData[p][71], ipMetaData[q][69], ipMetaData[q][70], ipMetaData[q][71], ipMetaData[p][72], ipMetaData[p][73], ipMetaData[p][74], ipMetaData[q][72], ipMetaData[q][73], ipMetaData[q][74], ipMetaData[p][75], ipMetaData[p][76], ipMetaData[p][77], ipMetaData[q][75], ipMetaData[q][76], ipMetaData[q][77], ipMetaData[p][78], ipMetaData[p][79], ipMetaData[p][80], ipMetaData[q][78], ipMetaData[q][79], ipMetaData[q][80], ipMetaData[p][78], ipMetaData[p][79], ipMetaData[p][80], ipMetaData[q][81], ipMetaData[q][82], ipMetaData[q][83]]
        #print('priv to priv')
    return flow_data

records_per_file = 300000
number_of_versions_per_hour = 2
if __name__ == '__main__':
    start = time.time()
    with open('fourTupleIntIpPlanning.csv', 'r') as f:
        tuple_count = 0
        files_count = int(sys.argv[1])
        max_tuples = ((files_count + 10) * 300000) / 2
        events = [[] for _ in range(8)]
        for eachtuple in csv.reader(f):
            if tuple_count < files_count*records_per_file/number_of_versions_per_hour:
                tuple_count = tuple_count + 1
                continue
            else:
                flowmetadata = fetch_metadata(eachtuple, tuple_count)
                for version in range(2):
                    for i in range(8):
                        flow_version = flowmetadata[:]
                        event_datetime = event_date.replace(hour=i, minute=random.randint(0, 59))
                        active_timestamp = int(event_datetime.timestamp())
                        srcBytes = random.randint(2500000, 28000000)
                        dstBytes = random.randint(2500000, 28000000)
                        totalBytes = srcBytes + dstBytes
                        totalPackets = random.randint(1, 100)
                        sessionCount = random.randint(100, 300)
                        rttMax = random.randint(20000, 70000)
                        rttAvg = (rttMax * 2) // 3
                        sch_version = 2
                        all_metrics_active = [totalBytes, srcBytes, dstBytes, totalPackets, sessionCount, rttMax, rttAvg]
                        flow_version.insert(1, active_timestamp)
                        flow_version.insert(95, sch_version)
                        flow_version.insert(96, lastactivity_range[tuple_count])
                        flow_version.insert(97, active_timestamp + lastactivity_range[tuple_count])
                        flow_version = flow_version + all_metrics_active
                        events[i].append(flow_version)
                    total_events = total_events + 1
                    #print(f'{total_events} created')
                    if total_events/records_per_file == total_events//records_per_file:
                        files_count = files_count+1
                        for i in range(8):
                            df = pd.DataFrame(events[i])
                            df.to_csv(f'planningFlowData_{i+1}_{files_count}.csv.gz', header=False, index=False, compression='gzip')
                            #print(f'{files_count} file is created in {i+1} th hour')
                            events[i] = events[i][records_per_file:]
                tuple_count = tuple_count + 1
                if (tuple_count == max_tuples): break
    if (len(events[0]) < records_per_file and len(events[0]) > 0):
        for i in range(8):
            df = pd.DataFrame(events[i])
            df.to_csv(f'planningRemainingData{i}.csv.gz', header=False, index=False, compression='gzip')
    end = time.time()
    took = end - start
    with open(f'log_details.txt', 'a') as logfile:
        text = f"{time.ctime(end)} - " \
            f"took{took} seconds - " \
            f"created {files_count} files - " \
            f"a total of {total_events} rows per file \n"
        logfile.write(text)


