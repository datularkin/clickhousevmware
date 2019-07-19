--to get details about all the tables (number of rows and size)
select table, formatReadableSize(size) as size, rows FROM ( select table, sum(bytes) AS size, sum(rows) AS rows, min(min_date) AS min_date, max(max_date) AS max_date FROM system.parts WHERE active GROUP BY table ORDER BY rows DESC )
clickhouse-client --password ubuntu --query="SELECT table, formatReadableSize(size) as size, rows FROM ( SELECT table, sum(bytes) AS size, sum(rows) AS rows, min(min_date) AS min_date, max(max_date) AS max_date FROM system.parts WHERE active GROUP BY table ORDER BY rows DESC )"
select partition, name, active from system.parts where table = 'localPlanning'

clickhouse-client --password ubuntu --query="SELECT partition, name, active FROM system.parts WHERE table = 'distributedTable'"

alter table table_name drop PARTITION partition_expr
clickhouse-client --password ubuntu --query="alter table table_name drop PARTITION '1559923200_1_6_1"
--to delete table entirely
drop table merge_tree.event_time_batch

--add column to existing table
alter table fivetuple.FIVEMAIN2 add COLUMN flowhost String

alter table flows.ORDERBYHOUR add COLUMN timeInMinute datetime

alter table flows.ORDERBYNAME add COLUMN timeInMinute datetime

alter table flows.ORDERBYTIME add COLUMN timeInMinute datetime


alter table flows.FINALFLOWSHOUR add COLUMN timeInMinute datetime

alter table flows.FINALFLOWSHOUR add COLUMN timeMinInt Int64

alter table flows.FINALFLOWSHOUR add COLUMN hourPart Int32 after name

-- update value to column
alter table FIVEMAIN2 update flowhost = 'hs1-webapp-vmware.com' where srcip = '192.168.1.2'

alter table flows.ORDERBYHOUR update timeInMinute = toStartOfMinute(toDateTime(time)) where timeInMinute = '0000-00-00 00:00:00'

alter table flows.ORDERBYNAME update timeInMinute = toStartOfMinute(toDateTime(time)) where 1

alter table flows.FINALFLOWSHOUR update timeInMinute = toStartOfMinute(toDateTime(time)) where 1

alter table flows.FINALFLOWSHOUR update timeMinInt = toUnixTimestamp(toStartOfMinute(toDateTime(time))) where 1

alter table flows.FINALFLOWSHOUR update hourPart = toHour(toDateTime(time)) where 1

--to select between time stamps
select srcIP.networkAddress,dstIP.networkAddress,srcVm.name,dstVm.name,srcSg.name,dstSg.name from FLOWVERSIONS202 where time between toUnixTimestamp('2019-06-07 00:00:00') and toUnixTimestamp('2019-06-07 01:00:00')
select srcIP.ipAddress,srcIP.networkAddress,count() from FLOWVERSIONS202 group by (srcIP.networkAddress,srcIP.ipAddress) with totals order by srcIP.ipAddress FORMAT PrettyCompact
--time series
select toHour(toDateTime(time)) as Hour, toMinute(toDateTime(time)) as Minute, sum(metricData.totalBytes) as totalBytes from flows.FINALFLOWSHOUR where time between toUnixTimestamp('2019-06-07 00:00:00') and toUnixTimestamp('2019-06-07 00:10:00') group by Hour,Minute order by Hour,Minute
--topK
select srcIP.ipAddress as sip, topK(3)(port.display) from flows.FINALFLOWSHOUR group by sip

---query_log
select event_date,event_time,query_start_time,query_duration_ms,read_rows,read_bytes,written_rows,written_bytes,result_rows,result_bytes,memory_usage,query,exception,thread_numbers,Settings.Names,Settings.Values from system.query_log where event_time between toDateTime(toUnixTimestamp(now())-100) and now() FORMAT Vertical

max_memory_usage   │ 10000000000 (9.3GiB)  │ "Maximum memory usage for processing of single query. Zero means unlimited."

select srcVm.name as sname,dstVm.name as dname,topK(20)(port.display) from vrniFlows.distributedTable where srcVm.name like '%10.0.37%' group by sname,dname order by sname

select name, toDateTime(time), modelkey_oid, port.ianaName, Protocol, srcIP.networkAddress, dstIP.networkAddress, srcsubnet.cidr, dstsubnet.cidr, sum(metricData.totalBytes) from flows.FINALFLOWSHOUR where time between toUnixTimestamp('2019-06-07 00:00:00') and toUnixTimestamp('2019-06-07 03:00:00')

select srcIP.networkAddress as sip, dstIP.networkAddress as dip, trafficType as Ttype, port.ianaPortDisplay as port, Protocol as pcol, any(dstVm.name) as dvm, any(dstSg.name) as dsg,any(dstCluster.name) as dcluster, any(dstL2Net.name) dl2,any(dstHost.name) as dhst,any(dstManagers.name) as dm, any(attribute_rule.name) as arn,any(attribute_firewallmanager.name) as afm, tuple(toStartOfMinute(toDateTime(time)), sum(metricData.totalBytes)) from vrniFlows.distributedTable where toStartOfHour(toDateTime(time))='2019-06-07 23:00:00' and modelkey_oid in (select distinct modelkey_oid from vrniFlows.distributedTable limit 10)group by sip,dip,time
------------------------------------------------------------------
select (sum(metricData.totalBytes))/1000000000000 as TB from vrniFlows.localTable
select port.ianaPortDisplay as port,count(*) as flowsCount,sum(metricData.totalBytes)/100000000 as dataInGB from vrniFlows.localTable group by port order by dataInGB
select (sum(metricData.totalBytes))/1000000000000 as TB_Switched from vrniFlows.localTable where networkLayer = 'LAYER_3'
select (sum(metricData.totalBytes))/1000000000000 as TB_Routed from vrniFlows.localTable where networkLayer = 'LAYER_2'
select count(*) from vrniFlows.distributedTable where withinhost=0
select srcL2Net.name as sl2, dstL2Net.name as dl2, count(*) as relatedFlows, sum(metricData.totalBytes) as totalBytes,sum(metricData.allowedSessionCount) as countSessions from vrniFlows.distributedTable group by sl2,dl2
select srcsubnet.cidr as ssubnet, dstsubnet.cidr as dsubnet, count(*) as relatedFlows, sum(metricData.totalBytes) as totalBytes,sum(metricData.allowedSessionCount) as countSessions from vrniFlows.distributedTable group by ssubnet,dsubnet
select srcCluster.name as sC, dstCluster.name as dC, count(*) as relatedFlows, sum(metricData.totalBytes) as totalBytes,sum(metricData.allowedSessionCount) as countSessions from vrniFlows.distributedTable group by sC,dC
select srcVm.name as svm, dstVm.name as dvm, count(*) as relatedFlows, sum(metricData.totalBytes) as totalBytes,sum(metricData.allowedSessionCount) as countSessions from vrniFlows.distributedTable group by sC,dC
select count(*) from vrniFlows.metadata2 where hasAny([vm_oid,k8s_service_oid, k8s_cluster_oid, k8s_namespace_oid, k8s_node_oid, sg_oid, IP_set_oid,STag_oid, L2net_oid, cluster_oid],[0])
select count(*) from vrniFlows.localPlanning where
select count(*) from vrniFlows.distributedPlanning where trafficType = 'EAST_WEST_TRAFFIC' and hasAny([srck8Info_k8sservice.modelkey_oid, srck8Info_k8scluster.modelkey_oid, srck8Info_k8snamespace.modelkey_oid, srck8Info_k8snode.modelkey_oid, srcVm.modelkey_oid, srcSg.modelkey_oid, srcIpSet.modelkey_oid, srcSt.modelkey_oid, srcL2Net.modelkey_oid, srcCluster.modelkey_oid, dstk8Info_k8sservice.modelkey_oid, dstk8Info_k8scluster.modelkey_oid, dstk8Info_k8snamespace.modelkey_oid, dstk8Info_k8snode.modelkey_oid, dstVm.modelkey_oid, dstSg.modelkey_oid, dstIpSet.modelkey_oid, dstSt.modelkey_oid, dstL2Net.modelkey_oid, dstCluster.modelkey_oid], [0])
--select srcL2Net.modelkey_oid as sl2, dstL2Net.modelkey_oid as dl2,if(sl2 and dl2 and trafficType='EAST_WEST_TRAFFIC', 'unset','internet'),trafficType, count(*) as flows,sum(metricData.totalBytes) as bytes, max(metricData.nsxTcpRtt_abs_max_ms) as maxTrate, sum(metricData.allowedSessionCount) as sessioncount from vrniFlows.distributedPlanning group by sl2,dl2,trafficType
--select multiIf(srcL2Net.name = '' and trafficType = 'EAST_WEST_TRAFFIC',srcsubnet.cidr,srcL2Net.name = '' and trafficType = 'INTERNET_TRAFFIC', 'Internet',srcVm.name='' and shared=1,'Shared Physical',srcVm.name='' and shared=0,'Physical',srcL2Net.name) as sourceL2Network,multiIf(dstL2Net.name = '' and trafficType = 'EAST_WEST_TRAFFIC',dstsubnet.cidr,dstL2Net.name = '' and trafficType = 'INTERNET_TRAFFIC','Internet',dstVm.name='' and shared=1,'Shared Physical',dstVm.name='' and shared=0,'Physical',dstL2Net.name) as destinationL2Network, count(*) as relatedFlows, sum(metricData.totalBytes) as sumOfBytes, max(metricData.nsxTcpRtt_abs_max_ms) as maxOfTrafficRate, sum(metricData.allowedSessionCount) as countOfSessions from vrniFlows.distributedPlanning group by sourceL2Network,destinationL2Network
--select multiIf(srcL2Net.name = '' and trafficType = 'EAST_WEST_TRAFFIC' and srcVm.name='' and shared=1,'Shared Physical', srcL2Net.name = '' and trafficType = 'EAST_WEST_TRAFFIC',srcsubnet.cidr,srcL2Net.name = '' and trafficType = 'INTERNET_TRAFFIC', 'Internet',srcVm.name='' and shared=0,'Physical',srcL2Net.name) as sourceL2Network,multiIf(dstL2Net.name = '' and trafficType = 'EAST_WEST_TRAFFIC',dstsubnet.cidr,dstL2Net.name = '' and trafficType = 'INTERNET_TRAFFIC','Internet',dstVm.name='' and shared=1,'Shared Physical',dstVm.name='' and shared=0,'Physical',dstL2Net.name) as destinationL2Network, count(*) as relatedFlows, sum(metricData.totalBytes) as sumOfBytes, max(metricData.nsxTcpRtt_abs_max_ms) as maxOfTrafficRate, sum(metricData.allowedSessionCount) as countOfSessions from vrniFlows.distributedPlanning group by sourceL2Network,destinationL2Network
select c,sum(f) from (select distinct c,f from (select ssg as c,flowVolume as f from (select srcSg.name as ssg, dstSg.name as dsg, sum(metricData.totalBytes) as flowVolume from vrniFlows.distributedPlanning where trafficType = 'EAST_WEST_TRAFFIC' and ssg != '' and dsg != '' group by ssg,dsg order by flowVolume) union all select dsg as c, flowVolume as f from (select srcSg.name as ssg, dstSg.name as dsg, sum(metricData.totalBytes) as flowVolume from vrniFlows.distributedPlanning where trafficType = 'EAST_WEST_TRAFFIC' and ssg != '' and dsg != '' group by ssg,dsg order by flowVolume))) group by c order by sum(f)
select sg, sum(bytes) from (select srcSg.name as sg, sum(metricData.totalBytes) as bytes from vrniFlows.distributedPlanning where sg != '' and srcSg.name != dstSg.name group by sg union all select dstSg.name as sg, sum(metricData.totalBytes) as bytes from vrniFlows.distributedPlanning where sg != '' and srcSg.name != dstSg.name group by sg union all select dstSg.name as sg, sum(metricData.totalBytes) as bytes from vrniFlows.distributedPlanning where sg != '' and srcSg.name = dstSg.name group by sg) group by sg
select multiIf(srcsubnet.cidr = '','Internet',srcL2Net.name = '' and srcVm.name != '','L2 UNSET', srcVm.name = '' and shared=0,'Physical',srcVm.name = '' and shared=1,'Shared_physical',srcL2Net.name) as srcL2, multiIf(dstsubnet.cidr = '','Internet',dstL2Net.name = '' and dstVm.name != '','L2 UNSET', dstVm.name = '' and shared=0,'Physical',dstVm.name = '' and shared=1,'Shared_physical',dstL2Net.name) as dstL2,groupUniqArray(port.ianaName) as ports, count(*) as relatedFlows, sum(metricData.totalBytes) as sumOfBytes, max(metricData.nsxTcpRtt_abs_max_ms) as maxOfTrafficRate, sum(metricData.allowedSessionCount) as countOfSessions from vrniFlows.distributedPlanning group by srcL2,dstL2 order by srcL2,dstL2
---------------------------------------------------------------------
select srcSg.name as ssg, dstSg.name as dsg,groupUniqArray(port.ianaName) as ports, count(*) as relatedFlows, sum(metricData.totalBytes) as sumOfBytes, max(metricData.nsxTcpRtt_abs_max_ms) as maxOfTrafficRate, sum(metricData.allowedSessionCount) as countOfSessions from vrniFlows.distributedTable group by sl2,dl2
-->select svm, dvm, countMerge(relatedFlows) as count, sumMerge(sumOfBytes) as data, maxMerge(maxOfTrafficRate) as maxTrate, sumMerge(countOfSessions) as sessions from vrniFlows.srcDstPair group by svm,dvm
-->
start query on (count, data, maxTrate,sessions):

--select svm, dvm, sumMerge(sumOfBytes) as data from vrniFlows.srcDstPair group by svm,dvm order by data DESC limit 100
-->Elapsed: 5.149 sec. Processed 50.00 million rows, 3.98 GB (9.71 million rows/s., 772.44 MB/s.)
or

select svm,dvm,data from toptalkers_vmvmPair_main order by data desc limit 100
-->100 rows in set. Elapsed: 5.043 sec. Processed 50.00 million rows, 3.98 GB (9.92 million rows/s., 788.77 MB/s.)
select srcc,dstc,data from toptalkers_cluster_main order by data desc limit 100
-->100 rows in set. Elapsed: 0.030 sec. Processed 1.32 thousand rows, 72.96 KB (44.80 thousand rows/s., 2.47 MB/s.)
select ssub,dsub,data from toptalkers_subnet_main order by data desc limit 100
-->100 rows in set. Elapsed: 0.025 sec. Processed 49.27 thousand rows, 3.24 MB (2.01 million rows/s., 131.93 MB/s.)
select sl2,dl2,data from toptalkers_vlan_main order by data desc limit 100
-->100 rows in set. Elapsed: 0.013 sec. Processed 31.61 thousand rows, 2.59 MB (2.50 million rows/s., 204.61 MB/s.)
---------------
select srcVm.name as svm, dstVm.name as dvm, sum(metricData.totalBytes) as sumOfBytes from vrniFlows.distributedPlanning where svm != '' and  dvm!= '' group by svm,dvm  order by svm,dvm
--1606462 rows in set. Elapsed: 5.434 sec. Processed 240.00 million rows, 10.47 GB (44.17 million rows/s., 1.93 GB/s.)
select srcVm.name as svm, dstVm.name as dvm, max(metricData.nsxTcpRtt_abs_max_ms) as maxOfTrafficRate from vrniFlows.distributedPlanning where svm != '' and  dvm!= '' group by svm,dvm  order by svm,dvm
--1606462 rows in set. Elapsed: 5.612 sec. Processed 240.00 million rows, 11.19 GB (42.76 million rows/s., 1.99 GB/s.)
select srcVm.name as svm, dstVm.name as dvm, count(*) as relatedFlows from vrniFlows.distributedPlanning where svm != '' and  dvm!= '' group by svm,dvm  order by svm,dvm
--1606462 rows in set. Elapsed: 5.080 sec. Processed 240.00 million rows, 9.76 GB (47.24 million rows/s., 1.92 GB/s.)
select srcVm.name as svm, dstVm.name as dvm, sum(metricData.allowedSessionCount) as countOfSessions from vrniFlows.distributedPlanning where svm != '' and  dvm!= '' group by svm,dvm  order by svm,dvm
--1606462 rows in set. Elapsed: 5.248 sec. Processed 240.00 million rows, 10.47 GB (45.73 million rows/s., 2.00 GB/s.)
-----------------
select vm, sum(bytes) from (select srcVm.name as vm, sum(metricData.totalBytes) as bytes from vrniFlows.distributedPlanning where vm != '' and srcVm.name != dstVm.name group by vm union all select dstVm.name as vm, sum(metricData.totalBytes) as bytes from vrniFlows.distributedPlanning where vm != '' and srcVm.name != dstVm.name group by vm union all select dstVm.name as vm, sum(metricData.totalBytes) as bytes from vrniFlows.distributedPlanning where vm != '' and srcVm.name = dstVm.name group by vm) group by vm
--2550 rows in set. Elapsed: 2.479 sec. Processed 720.00 million rows, 28.58 GB (290.42 million rows/s., 11.53 GB/s.)
select srcVm.name as vm, sum(metricData.totalBytes) as bytes from vrniFlows.distributedPlanning where vm != '' group by vm union all select dstVm.name as vm, sum(metricData.totalBytes) as bytes from vrniFlows.distributedPlanning where vm != '' group by vm
--2550 rows in set. Elapsed: 1.296 sec. Processed 480.00 million rows, 12.32 GB (370.44 million rows/s., 9.51 GB/s.)
select vm, sum(bytes) from (select srcVm.name as vm, sum(metricData.totalBytes) as bytes from vrniFlows.distributedTable where vm != '' and srcVm.name != dstVm.name group by vm union all select dstVm.name as vm, sum(metricData.totalBytes) as bytes from vrniFlows.distributedTable where vm != '' and srcVm.name != dstVm.name group by vm union all select dstVm.name as vm, sum(metricData.totalBytes) as bytes from vrniFlows.distributedTable where vm != '' and srcVm.name = dstVm.name group by vm) group by vm

select srcVm.name as svm, dstVm.name as dvm, sum(metricData.totalBytes) as sumOfBytes from vrniFlows.distributedTable where toStartOfHour(toDateTime(time)) = '2019-06-07 08:00:00' or toStartOfHour(toDateTime(time)) = '2019-06-07 00:00:00' or toStartOfHour(toDateTime(time)) = '2019-06-07 16:00:00' group by svm,dvm  order by sumOfBytes limit 100

select srcVm.name as svm, dstVm.name as dvm,count(*) as relatedFlows, sum(metricData.totalBytes) as sumOfBytes, max(metricData.nsxTcpRtt_abs_max_ms) as maxOfTrafficRate, sum(metricData.allowedSessionCount) as countOfSessions from vrniFlows.distributedTable group by svm,dvm


select modelkey_oid,tuple(toDateTime(time), metricData.totalBytes) from vrniFlows.distributedTable where modelkey_oid in (select distinct modelkey_oid from vrniFlows.localTable limit 10) group by modelkey_oid,time,metricData.totalBytes order by time

create materialized view currentstatus engine = AggregatingMergeTree() order by objid populate as select modelkey_oid as objid, argMaxState(port.ianaName,time) as port,argMaxState(Protocol,time) as pcol,argMaxState(srcIP.networkAddress,time) as srcip,argMaxState(dstIP.networkAddress,time) as dstip,argMaxState(trafficType,time) as ttype,argMaxState(srcSg.name,time)as srcsg,argMaxState(dstSg.name,time) as dstsg, argMaxState(srcL2Net.name,time) as srcl2, argMaxState(dstL2Net.name,time) as dstl2 from vrniFlows.copy group by objid
create view getstatus as select objid, argMaxMerge(port) as port, argMaxMerge(pcol) as protocol, argMaxMerge(srcip) as sourceIP, argMaxMerge(dstip) as destinationIP, argMaxMerge(ttype) as trafficType, argMaxMerge(srcsg) as srcSecGrp, argMaxMerge(dstsg) as dstSecGrp, argMaxMerge(srcl2) as srcL2, argMaxMerge(dstl2) as dstL2 from currentstatusplanninglocal group by objid
select modelkey_oid as objid, argMax(port.ianaName,time) as port,argMax(Protocol,time) as pcol,argMax(srcIP.networkAddress,time) as srcip,argMax(dstIP.networkAddress,time) as dstip,argMax(trafficType,time) as ttype,argMax(srcSg.name,time)as srcsg,argMax(dstSg.name,time) as dstsg, argMax(srcL2Net.name,time) as srcl2, argMax(dstL2Net.name,time) as dstl2 from vrniFlows.distributedTable group by objid
