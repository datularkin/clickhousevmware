#!/usr/bin/env bash

for f in hour_"$1"_"$2"/*.gz
do
    zcat ${f} | clickhouse-client --password ubuntu --query="INSERT INTO vrniFlows.samplingTable FORMAT CSV"
done
