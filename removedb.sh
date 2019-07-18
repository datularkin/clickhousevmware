#!/usr/bin/env bash
clickhouse-client --password ubuntu --query="DROP DATABASE $*"
rmdir -r /var/extra-disk/$*
