# 0x1B. Web stack debugging #4

```bash
██     ██ ███████ ██████      ██████  ███████ ██████  ██    ██  ██████   ██████  ██ ███    ██  ██████ 
██     ██ ██      ██   ██     ██   ██ ██      ██   ██ ██    ██ ██       ██       ██ ████   ██ ██      
██  █  ██ █████   ██████      ██   ██ █████   ██████  ██    ██ ██   ███ ██   ███ ██ ██ ██  ██ ██   ███ 
██ ███ ██ ██      ██   ██     ██   ██ ██      ██   ██ ██    ██ ██    ██ ██    ██ ██ ██  ██ ██ ██    ██ 
 ███ ███  ███████ ██████      ██████  ███████ ██████   ██████   ██████   ██████  ██ ██   ████  ██████  
```

## General

* web debugging

## Environment

* OS: ``ubuntu`` 14.04 LTS
* ``puppet``
* ``puppet-lint``
* ``ab`` Apache Benchmark

## Run the code

### Test with Apache Bench

> run the test

```bash
root@d785f756d8c3:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   3.513 seconds
Complete requests:      2000
Failed requests:        659
   (Connect: 0, Receive: 0, Length: 659, Exceptions: 0)
Non-2xx responses:      1341
Total transferred:      1059638 bytes
HTML transferred:       672849 bytes
Requests per second:    569.26 [#/sec] (mean)
Time per request:       175.667 [ms] (mean)
Time per request:       1.757 [ms] (mean, across all concurrent requests)
Transfer rate:          294.54 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2  11.8      0      93
Processing:     2  171  47.7    194     306
Waiting:        1  169  48.5    193     306
Total:          4  173  47.0    195     306

Percentage of the requests served within a certain time (ms)
  50%    195
  66%    199
  75%    200
  80%    200
  90%    205
  95%    207
  98%    214
  99%    289
 100%    306 (longest request)
root@d785f756d8c3:/#
```

> check services status

```bash
root@d785f756d8c3:/# sudo service --status-all
 [ ? ]  console-setup
 [ + ]  cron
 [ - ]  dbus
 [ ? ]  killprocs
 [ ? ]  kmod
 [ ? ]  networking
 [ + ]  nginx
 [ ? ]  ondemand
 [ - ]  procps
 [ - ]  puppet
 [ ? ]  rc.local
 [ + ]  resolvconf
 [ - ]  rsync
 [ - ]  rsyslog
 [ ? ]  sendsigs
 [ + ]  ssh
 [ - ]  sudo
 [ + ]  udev
 [ ? ]  umountfs
 [ ? ]  umountnfs.sh
 [ ? ]  umountroot
 [ - ]  urandom
 [ - ]  x11-common
root@d785f756d8c3:/#
```

> after multiple runs of ab with different concurrency levels, the server stop to respond

```bash
root@d785f756d8c3:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
apr_pollset_poll: The timeout specified has expired (70007)
root@d785f756d8c3:/#
```

``curl -I localhost`` never respond

> restar the server and recieve the header response

```bash
root@d785f756d8c3:/# sudo service nginx restart
 * Restarting nginx nginx                                                                                                                                         [ OK ]
root@d785f756d8c3:/# curl -I localhost
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 21 Feb 2022 10:52:48 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
Accept-Ranges: bytes

root@d785f756d8c3:/#
```

> modifiy the nginx config doesn't work

worker_process auto;
worker_connections 2000;

> check the log
>
> in ubuntu 14.04

Shows 612 error log entries

``/var/log/nginx``

> cat the nginx ulimit

```bash
root@d785f756d8c3:~# cat /etc/default/nginx
# Note: You may want to look at the following page before setting the ULIMIT.
#  http://wiki.nginx.org/CoreModule#worker_rlimit_nofile
# Set the ulimit variable if you need defaults to change.
#  Example: ULIMIT="-n 4096"
ULIMIT="-n 15"
root@d785f756d8c3:~#
```

```bash
root@3b62e26387ad:/# cat /etc/default/nginx
# Note: You may want to look at the following page before setting the ULIMIT.
#  http://wiki.nginx.org/CoreModule#worker_rlimit_nofile
# Set the ulimit variable if you need defaults to change.
#  Example: ULIMIT="-n 4096"
ULIMIT="-n 15"
```

> run puppet to fix the error

```bash
root@d785f756d8c3:~# puppet apply 0-the_sky_is_the_limit_not.pp
Notice: Compiled catalog for d785f756d8c3.ec2.internal in environment production in 0.21 seconds
Notice: /Stage[main]/Main/Exec[file limit]/returns: executed successfully
Notice: Finished catalog run in 2.90 seconds
root@d785f756d8c3:~#
```

> run the Apache Bench again

```bash
root@d785f756d8c3:~# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   3.708 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    539.44 [#/sec] (mean)
Time per request:       185.378 [ms] (mean)
Time per request:       1.854 [ms] (mean, across all concurrent requests)
Transfer rate:          449.36 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   50  55.2     13     209
Processing:     1  133  84.5    104     587
Waiting:        1  108  75.9     99     586
Total:          2  183  87.3    194     593

Percentage of the requests served within a certain time (ms)
  50%    194
  66%    204
  75%    213
  80%    285
  90%    299
  95%    305
  98%    392
  99%    400
 100%    593 (longest request)
root@d785f756d8c3:~#
```

### user limit

> allows ``holberton`` user to login

```bash
root@b7c6a09a0ae5:/# su - holberton
-su: /etc/profile: Too many open files
-su: /home/holberton/.bash_profile: Too many open files
-su-4.3$ /etc/profile
-su: start_pipeline: pgrp pipe: Too many open files
-su: /etc/profile: Permission denied
-su-4.3$ head /etc/passwd
-su: start_pipeline: pgrp pipe: Too many open files
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
-su-4.3$ start_pipeline: pgrep pipe:
-su: start_pipeline: pgrp pipe: Too many open files
-su: start_pipeline:: command not found
-su-4.3$ logout

```

> change the user limit in the ``/etc/security/limits.conf`` file

```script
holberton hard nofile unlimited
holberton soft nofile 3000
```

```bash
root@b7c6a09a0ae5:/# puppet apply 1-user_limit.pp
Notice: Compiled catalog for b7c6a09a0ae5.ec2.internal in environment production in 0.30 seconds
Notice: /Stage[main]/Main/Exec[Modify soft limit]/returns: executed successfully
Notice: /Stage[main]/Main/Exec[Modify hard limit]/returns: executed successfully
Notice: Finished catalog run in 1.00 seconds
root@b7c6a09a0ae5:/# su - holberton
holberton@b7c6a09a0ae5:~$ head /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
holberton@b7c6a09a0ae5:~$ logout
```

## Author
<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+26K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
