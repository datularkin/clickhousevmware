#!/usr/bin/env bash

for f in planningFlowData_"$*"_*
do
    #echo ${f}
    zcat ${f} | clickhouse-client --password ubuntu --query="insert into vrniFlows.distributedPlanning FORMAT CSV"
done
