# clickhousevmware
Clickhouse setup:
```https://docs.google.com/document/d/1J7RQ2MttdJpAEJ8kddOB7FkXBouzBv3Mp2SH5wvG2rs/edit?usp=sharing```
Extra disk space take need to link it with database table path
``` create a db and find its data storage path , for example /opt/clickhouse/data/fastdb
    create a path in another ssd ,for example /mnt/ssd/fastdb
    delete file fastdb that under /opt/clickhouse/data/fastdb   --> /opt/clickhouse/data/fastdb must be blank and no file exists
    run ln -s /mnt/ssd/fastdb /opt/clickhouse/data/ in terminal ```
--> Generate MetaData
--> Generate FourTuple Data
--> Generate flows per hour
--> move files to separate directory with hour name
--> insert data hour wise into clickhouse
