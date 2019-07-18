#!/usr/bin/env bash
n=0
for k in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
do
    mkdir hour_"$*"_${k}
done
for f in flow_Data_"$*"_*
do
    val=`expr "$n" / 63 + 1`
    mv ${f} hour_"$*"_$val
    n=$(( n+1 ))
done
