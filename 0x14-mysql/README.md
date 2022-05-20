# 0x14. MySQL

```bash
███    ███ ██    ██ ███████  ██████  ██ 
████  ████  ██  ██  ██      ██    ██ ██ 
██ ████ ██   ████   ███████ ██    ██ ██ 
██  ██  ██    ██         ██ ██ ▄▄ ██ ██ 
██      ██    ██    ███████  ██████  ███████ 
                                ▀▀    
```

## General

* Database administration
* Web stack debugging
* Primary replica cluster
* Mysql replica setup
* Robust database backup strategy

## Environment
<!-- ubuntu -->
[![Ubuntu](https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A)](https://ubuntu.com/) <!-- bash -->
[![Bash](https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A)](https://www.gnu.org/software/bash/) <!-- vim -->
[![Vim](https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A)](https://www.vim.org/) <!-- vs code -->
[![VS Code](https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A)](https://code.visualstudio.com/)

* OS: ``ubuntu`` 20.04 LTS
* Shell: ``bash``
  * shebang: ``#!/usr/bin/env bash``
* Codestyle guidelines: ``Shellcheck`` 0.3.7
* IDE: ``vim``, ``VS Code``
* ``ssh``
* DBA: ``mysql``
* ``mysqldump``

## Install mysql

* confirm that mysql is not running

```bash
$ ps ax | grep mysql
```

* install mysql

```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ apt list --upgradable
$ sudo apt upgrade
$ sudo apt install wget -y
$ wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
$ sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
$ sudo apt-get update
$ sudo apt-cache policy mysql-server
$ sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
$ sudo mysql_secure_installation
$ mysql -u root -p
$
```

> if necessary, add the key

```bash
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29
$
```

* verify mysql version

```bash
ubuntu@3284-web-02:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.37, for Linux (x86_64) using  EditLine wrapper
ubuntu@3284-web-02:~$
```


> if doesn't work the installation

```bash
sudo apt-get purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*
sudo rm -rf /etc/mysql /var/lib/mysql
sudo apt-get autoremove
sudo apt-get autoclean
wget http://repo.mysql.com/mysql-apt-config_0.8.10-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb
sudo dpkg-reconfigure mysql-apt-config
sudo apt update
sudo apt-cache policy mysql-server
sudo mkdir -p /etc/mysql/conf.d
sudo apt install -f mysql-client=5.7.30-1ubuntu18.04
sudo apt install -f mysql-community-server=5.7.30-1ubuntu18.04
sudo apt install -f mysql-server=5.7.30-1ubuntu18.04
sudo vi /etc/apt/preferences.d/mysql

    Package: mysql-server
    Pin: version 5.7.30-1ubuntu18.04
    Pin-Priority: 1001

    Package: mysql-client
    Pin: version 5.7.30-1ubuntu18.04
    Pin-Priority: 1001

    Package: mysql-community-server
    Pin: version 5.7.30-1ubuntu18.04
    Pin-Priority: 1001

    Package: mysql-community-client
    Pin: version 5.7.30-1ubuntu18.04
    Pin-Priority: 1001

    Package: mysql-apt-config
    Pin: version 0.8.10-1
    Pin-Priority: 1001
```


```bash
sudo apt update
sudo apt install wget -y
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
sudo apt-get update
sudo apt-cache policy mysql-server
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
sudo mysql_secure_installation
mysql -u root -p
```

> bash history

``sudo apt-get upgrade``
``apt list --upgradable``
``sudo apt upgrade``
``sudo apt install wget -y``
``wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb``
``sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb``
``sudo apt-get update``
``sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29``
``sudo apt-get update``
``sudo apt-cache policy mysql-server``
``sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*``
``wget http://repo.mysql.com/mysql-apt-config_0.8.10-1_all.deb``
``sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb``
``sudo apt update``
``sudo apt-cache policy mysql-server``
``sudo mkdir -p /etc/mysql/conf.d``
``sudo apt install -f mysql-client=5.7.30-1ubuntu18.04``
``sudo apt-get purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*``
``sudo rm -rf /etc/mysql /var/lib/mysql``
``sudo apt-get autoremove``
``sudo apt-get autoclean``
``wget http://repo.mysql.com/mysql-apt-config_0.8.10-1_all.deb``
``sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb``
``sudo vi /etc/apt/preferences.d/mysql``
``sudo apt update``
``sudo apt list --upgradable``
``sudo apt-get upgrade``
``sudo apt install wget -y``
``wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb``
``sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb``
``sudo apt-get update``
``sudo apt-cache policy mysql-server``
``sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*``
``sudo mysql_secure_installation``
``sudo mysql -u root -p``
``mysql --version``

## check user

```bash
ubuntu@3284-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@3284-web-01:~$
```

## configure mysql source and replica

> set firewall on source server to allow connections from replica( the ip of the replica server)

``sudo ufw allow from 54.226.88.203 to any port 3306``

> check status

```bash
ubuntu@3284-web-01:~$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
Nginx HTTP                 ALLOW       Anywhere
22/tcp                     ALLOW       Anywhere
443/tcp                    ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
3306                       ALLOW       54.226.88.203
Nginx HTTP (v6)            ALLOW       Anywhere (v6)
22/tcp (v6)                ALLOW       Anywhere (v6)
443/tcp (v6)               ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)

ubuntu@3284-web-01:~$
```

> edit mysql config on source database

``sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf``

comment ``# bind-address  = 127.0.0.1``

> add lines to the end of the file
```script
# identify server
# log_bin directive, base name and location of binary log
# include_database_name with the name of the database that wants to be replicated
server-id       = 1
log_bin         = /var/log/mysql/mysql-bin.log
binlog_do_db    = tyrell_corp
```
> restart mysql

```bash
$ sudo systemctl restart mysql
```
> show mysql status

```bash
ubuntu@3284-web-01:~$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.37-log MySQL Community Server (GPL)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show master status;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000001 |      154 | tyrell_corp  |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

mysql>
```

> replication user

> create user

```mysql
mysql> CREATE USER 'replica_user'@'localhost' IDENTIFIED BY 'password';``
mysql> GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'localhost';``
mysql> FLUSH PRIVILEGES;
```

> temporary lock on source

close all the open tables in every database on your source instance and lock them

```mysql
mysql> FLUSH TABLES WITH READ LOCK;
mysql> SHOW MASTER STATUS;
```
> creating a snapshot of the database with the mysqldump utility

> open a new terminal and open ssh conection to source server

```bash
ubuntu@3284-web-01:~$ sudo mysqldump -u root -p tyrell_corp > tyrell_corp.sql
```

> back to the mysql terminal and unlock the tables

```mysql
mysql> UNLOCK TABLES;
```

> send your snapshot file to your replica server usin ssh and scp. ip of replica server

```bash
$ scp -i ~/.ssh/id_rsa_server tyrell_corp.sql ubuntu@54.226.88.203:/tmp/
```

> on replica create database

```mysql
mysql> SHOW DATABASES;
mysql> CREATE DATABASE tyrell_corp;
exit
``

> import the snapshot

``bash
$ sudo mysql -u root -p  tyrell_corp < /tmp/tyrell_corp.sql
```

> Configure replica database

```bash
$ sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

> edit

```script
# bind-address  = 127.0.0.1
```

```script
# align values with the source machine
server-id               = 2
log_bin                 = /var/log/mysql/mysql-bin.log
binlog_do_db            = tyrell_corp
relay-log               = /var/log/mysql/mysql-relay-bin.log
```

> restart to implement

```bash
$ sudo systemctl restart mysql
```

### Start replication on replica server

```script
CHANGE MASTER TO
MASTER_HOST='web-01.xelar.tech',
MASTER_USER='replica_user',
MASTER_PASSWORD='78215617',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=951;
```

> star replication threads on replica server

```mysql
mysql> START SLAVE;
```

> show status

```mysql
mysql> SHOW SLAVE STATUS\G;
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: web-01.xelar.tech
                  Master_User: replica_user
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000001
          Read_Master_Log_Pos: 951
               Relay_Log_File: mysql-relay-bin.000002
                Relay_Log_Pos: 320
        Relay_Master_Log_File: mysql-bin.000001
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 951
              Relay_Log_Space: 527
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File:
           Master_SSL_CA_Path:
              Master_SSL_Cert:
            Master_SSL_Cipher:
               Master_SSL_Key:
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error:
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Master_Server_Id: 1
                  Master_UUID: b8a2bb2d-7f24-11ec-aaca-0aeef8871ec3
             Master_Info_File: /var/lib/mysql/master.info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind:
      Last_IO_Error_Timestamp:
     Last_SQL_Error_Timestamp:
               Master_SSL_Crl:
           Master_SSL_Crlpath:
           Retrieved_Gtid_Set:
            Executed_Gtid_Set:
                Auto_Position: 0
         Replicate_Rewrite_DB:
                 Channel_Name:
           Master_TLS_Version:
1 row in set (0.00 sec)

ERROR:
No query specified
```

## Author

<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+24K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
