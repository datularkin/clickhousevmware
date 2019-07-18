#!/usr/bin/env bash
clickhouse-client --password ubuntu --query="create database $*"
mkdir /var/extra-disk/$*
sudo chown clickhouse:clickhouse -R /var/extra-disk/$*/
rm -r /var/lib/clickhouse/data/$*
ln -s /var/extra-disk/$* /var/lib/clickhouse/data/
sudo chown clickhouse:clickhouse -R /var/lib/clickhouse/data/
