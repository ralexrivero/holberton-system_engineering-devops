# 0x10. HTTPS SSL 🔒

```bash
███████ ███████ ██ 
██      ██      ██ 
███████ ███████ ██ 
     ██      ██ ██ 
███████ ███████ ███████
```

## Overview

* DNS
* Web stack debugging

## Environment

<!-- ubuntu -->
[![Ubuntu](https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A)](https://ubuntu.com/) <!-- bash -->
[![Bash](https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A)](https://www.gnu.org/software/bash/) <!-- vim -->
[![Vim](https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A)](https://www.vim.org/) <!-- vs code -->
[![VS Code](https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A)](https://code.visualstudio.com/)

* OS: ``ubuntu`` 20.04
* Shell: ``bash``
* ``ssh``
* Style guidelines: ``shellcheck`` 0.3.7
* Editors: ``vim``, ``VS Code``
* ``awk``
* ``dig``
* ``snap`` snapd
* ``certbot``

## Run the code

```bash
ralex@ralex-nb:~$ dig xelar.tech | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
xelar.tech.		4151	IN	A	54.165.191.52
ralex@ralex-nb:~$ dig www.xelar.tech | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.xelar.tech.		4502	IN	A	54.165.191.52
ralex@ralex-nb:~$ dig lb-01.xelar.tech | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.xelar.tech.	4502	IN	A	54.165.191.52
ralex@ralex-nb:~$ dig web-01.xelar.tech | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.xelar.tech.	4502	IN	A	35.231.236.4
ralex@ralex-nb:~$ dig web-02.xelar.tech | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.xelar.tech.	4502	IN	A	34.74.187.179
ralex@ralex-nb:~$
ralex@ralex-nb:~$ ./0-world_wide_web xelar.tech
The subdomain www is a A record and points to 54.165.191.52
The subdomain lb-01 is a A record and points to 54.165.191.52
The subdomain web-01 is a A record and points to 35.231.236.4
The subdomain web-02 is a A record and points to 34.74.187.179
ralex@ralex-nb:~$ ./0-world_wide_web xelar.tech web-02
The subdomain web-02 is a A record and points to 34.74.187.179
ralex@ralex-nb:~$
```

## install certbot

> show linux distro, install snapd, install certbot

```bash
$ lsb_release -a
$ sudo apt update
$ sudo apt install snapd
$ sudo apt-get upgrade
$ sudo snap install hello-world
$ sudo snap install core; sudo snap refresh core
$ sudo apt-get remove certbot
$ sudo snap install --classic certbot
$ sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

> stop haproxy, install certificate and restart haproxy

```bash
$ sudo service haproxy stop
$ sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d xelar.tech -d www.xelar.tech
$ sudo ls /etc/letsencrypt/live/xelar.tech
```

> copy certificate to haproxy

```bash
$ sudo mkdir -p /etc/haproxy/certs
DOMAIN='xelar.tech' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
$ sudo chmod -R go-rwx /etc/haproxy/certs
```

> config.cfg in haproxy

_global_

```maxconn 2048```
```tune.ssl.default-dh-param 2048```

_defaults_

```option forwardfor```
```option http-server-close```

_frontend_

```
frontend loadbalancerssl
        bind *:443 ssl crt /etc/haproxy/certs/xelar.tech.pem
        http-request add-header X-Forwarded-Proto https if { ssl_fc }
        acl letsencrypt-acl path_beg /.well-known/acme-challenge/
        use_backend letsencrypt-backend if letsencrypt-acl
        default_backend webservers
```

_backend_

```redirect scheme https if !{ ssl_fc }```

only for renewal traffic

```
backend letsencrypt-backend
        server letsencrypt 127.0.0.1:54321
```

> verify if haproxy.cfg contain a valid configuration

```bash
$ sudo haproxy -f /etc/haproxy/haproxy.cfg -c
```

> resart haproxy server

```bash
$ sudo service haproxy restart
```
> test automatical renewal

```bash
$ sudo certbot renew --dry-run
```

## test ssl

```bash
vagrant@ubuntu-xenial:~$ curl -sI https://www.xelar.tech
HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Mon, 24 Jan 2022 06:38:37 GMT
content-type: text/html
content-length: 17
last-modified: Mon, 24 Jan 2022 06:34:06 GMT
etag: "61ee485e-11"
x-served-by: 3284-web-01
accept-ranges: bytes

vagrant@ubuntu-xenial:~$ curl -sI https://www.xelar.tech
HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Mon, 24 Jan 2022 06:38:42 GMT
content-type: text/html
content-length: 17
last-modified: Mon, 24 Jan 2022 06:38:25 GMT
etag: "61ee4961-11"
x-served-by: 3284-web-02
accept-ranges: bytes

vagrant@ubuntu-xenial:~$ curl https://www.xelar.tech
Holberton School
vagrant@ubuntu-xenial:~$ curl https://www.xelar.tech
Holberton School
vagrant@ubuntu-xenial:~$
```

## redirection 301 from http to https

> show header, follow redirect

```bash
vagrant@ubuntu-xenial:~$ curl -sIL http://www.xelar.tech
HTTP/1.1 301 Moved Permanently
content-length: 0
location: https://www.xelar.tech/
connection: close

HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Mon, 24 Jan 2022 17:46:49 GMT
content-type: text/html
content-length: 17
last-modified: Mon, 24 Jan 2022 06:34:06 GMT
etag: "61ee485e-11"
x-served-by: 3284-web-01
accept-ranges: bytes


vagrant@ubuntu-xenial:~$
```

# Author

<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+27K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
