# clickhousevmware
Clickhouse setup:
```https://docs.google.com/document/d/1J7RQ2MttdJpAEJ8kddOB7FkXBouzBv3Mp2SH5wvG2rs/edit?usp=sharing```

-----------------------------------------------------------------------------------------------------------------------------

Extra disk space take need to link it with database table path:
``` 1.Create a db and find its data storage path , for example /opt/clickhouse/data/fastdb
    2.Create a path in another ssd ,for example /mnt/ssd/fastdb
    3.Delete file fastdb that under /opt/clickhouse/data/fastdb   --> /opt/clickhouse/data/fastdb must be blank and no file exists
    4.Run ln -s /mnt/ssd/fastdb /opt/clickhouse/data/ in terminal
    
-----------------------------------------------------------------------------------------------------------------------------
    
Setup Anaconda environment in all the setups to run scripts:
--> sudo apt-get update -y && sudo apt-get upgrade -y
--> cd /tmp/
--> wget https://repo.continuum.io/archive/Anaconda3-2019.03-Linux-x86_64.sh
--> bash Anaconda3-5.0.1-Linux-x86_64.sh (type 'yes' and 'enter' whenever asked) 
--> source ~/.bashrc
--> conda list (to check installation)

-----------------------------------------------------------------------------------------------------------------------------

--> Generate MetaData using 'ipMetaDataGen.py'
``python3 ipMetaDataGen.py``
--> Generate FourTuple Data using '4TupleGen.py' and send two system arguments while running code
``python3 4TupleGen.py 0 1000 & python3 4TupleGen.py 1000 2000 & python3 4TupleGen.py 2000 3000 & python3 4TupleGen.py 3000 4000 & python3 4TupleGen.py 4000 5000 & python3 4TupleGen.py 5000 6000 & python3 4TupleGen.py 6000 7000 & python3 4TupleGen.py 8000 9000 & python3 4TupleGen.py 9000 10000 & python3 4TupleGen.py 10000 11000 & python3 4TupleGen.py 11000 12000 & python3 4TupleGen.py 12000 12500``
--> Generate flows per hour using 'flowGenPerHour.py' and send two arguments (hour and number of already created files)(each script run will create 500 files for the given hour starting from files_created param)

In setup1: ``python3 flowGenPerHour.py 0 0 & python3 flowGenPerHour.py 0 500 & python3 flowGenPerHour.py 1 0 & python3 flowGenPerHour.py 1 500 & python3 flowGenPerHour.py 2 0 & python3 flowGenPerHour.py 2 500 & python3 flowGenPerHour.py 3 0 & python3 flowGenPerHour.py 3 500 & python3 flowGenPerHour.py 4 0 & python3 flowGenPerHour.py 4 500 &  python3 flowGenPerHour.py 5 0 & python3 flowGenPerHour.py 5 500 & python3 flowGenPerHour.py 6 0 & python3 flowGenPerHour.py 6 500 & python3 flowGenPerHour.py 7 0 & python3 flowGenPerHour.py 7 500``

In setup2: ``python3 flowGenPerHour.py 8 0 & python3 flowGenPerHour.py 8 500 & python3 flowGenPerHour.py 9 0 & python3 flowGenPerHour.py 9 500 & python3 flowGenPerHour.py 10 0 & python3 flowGenPerHour.py 10 500 & python3 flowGenPerHour.py 11 0 & python3 flowGenPerHour.py 11 500 & python3 flowGenPerHour.py 12 0 & python3 flowGenPerHour.py 12 500 &  python3 flowGenPerHour.py 13 0 & python3 flowGenPerHour.py 13 500 & python3 flowGenPerHour.py 14 0 & python3 flowGenPerHour.py 14 500 & python3 flowGenPerHour.py 15 0 & python3 flowGenPerHour.py 15 500``

In setup3: ``python3 flowGenPerHour.py 16 0 & python3 flowGenPerHour.py 16 500 & python3 flowGenPerHour.py 17 0 & python3 flowGenPerHour.py 17 500 & python3 flowGenPerHour.py 18 0 & python3 flowGenPerHour.py 18 500 & python3 flowGenPerHour.py 19 0 & python3 flowGenPerHour.py 19 500 & python3 flowGenPerHour.py 20 0 & python3 flowGenPerHour.py 20 500 & python3 flowGenPerHour.py 21 0 & python3 flowGenPerHour.py 21 500 &  python3 flowGenPerHour.py 22 0 & python3 flowGenPerHour.py 22 500 & python3 flowGenPerHour.py 23 0 & python3 flowGenPerHour.py 23 500``

--> Better run these three scripts in three different setups usually taking hours of time (approx 20hrs each)

--> move files to separate directory with hour name using '16directoriesperhour.sh' need to pass 'hour' as an argument
`` it will create 16 directories per hour each directory having aroud 64 files``
In setup1: ``./16directoriesperhour.sh 1 & ./16directoriesperhour.sh 2 & ./16directoriesperhour.sh 3 & ./16directoriesperhour.sh 4 & ./16directoriesperhour.sh 5 & ./16directoriesperhour.sh 6 & ./16directoriesperhour.sh 7 & ./16directoriesperhour.sh 8``
In setup2: ``./16directoriesperhour.sh 9 & ./16directoriesperhour.sh 10 & ./16directoriesperhour.sh 11 & ./16directoriesperhour.sh 12 & ./16directoriesperhour.sh 13 & ./16directoriesperhour.sh 14 & ./16directoriesperhour.sh 15 & ./16directoriesperhour.sh 16``
In setup3: ``./16directoriesperhour.sh 17 & ./16directoriesperhour.sh 18 & ./16directoriesperhour.sh 19 & ./16directoriesperhour.sh 20 & ./16directoriesperhour.sh 21 & ./16directoriesperhour.sh 22 & ./16directoriesperhour.sh 23 & ./16directoriesperhour.sh 24``
---------------------------------------------------------------------------------------------------------------------------
--> insert data hour wise into clickhouse use 'insertHourWise.sh'
``send 'hour' as an argument 
for all 8 hours in each setup:
Run only one script at a time  coz this script itself triggers 16 child scripts 'insertIntoClickhouse.sh'
eg: ./insertHourWise.sh 1
do with all hours from 1 to 24
--------------------------------------------------------------------------------------------------------------------------



