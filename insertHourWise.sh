#!/usr/bin/env bash

./insertIntoClickhouse.sh "$*" 1 &   ./insertIntoClickhouse.sh "$*" 2 & ./insertIntoClickhouse.sh "$*" 3 & ./insertIntoClickhouse.sh "$*" 4 & ./insertIntoClickhouse.sh "$*" 5 & ./insertIntoClickhouse.sh "$*" 6 & ./insertIntoClickhouse.sh "$*" 7 & ./insertIntoClickhouse.sh "$*" 8 & ./insertIntoClickhouse.sh "$*" 9 & ./insertIntoClickhouse.sh "$*" 10 & ./insertIntoClickhouse.sh "$*" 11 & ./insertIntoClickhouse.sh "$*" 12 & ./insertIntoClickhouse.sh "$*" 13 & ./insertIntoClickhouse.sh "$*" 14 & ./insertIntoClickhouse.sh "$*" 15 & ./insertIntoClickhouse.sh "$*" 16
wait
