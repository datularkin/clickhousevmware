#!/usr/bin/env bash

for k in 51 52 53 54 55 56 57 58 59 60 71 72 73 74 75 76 77 78 79 80
do
    zcat planningFlowData_"$*"_${k}.* | clickhouse-client --password ubuntu --query="insert into vrniFlows.distributedPlanning FORMAT CSV"

done
