# 0x13. Firewall

```bash
███████ ██ ██████  ███████ ██     ██  █████  ██      ██ 
██      ██ ██   ██ ██      ██     ██ ██   ██ ██      ██ 
█████   ██ ██████  █████   ██  █  ██ ███████ ██      ██ 
██      ██ ██   ██ ██      ██ ███ ██ ██   ██ ██      ██ 
██      ██ ██   ██ ███████  ███ ███  ██   ██ ███████ ███████ 
```

## General

* web stack debugging
* firewall configuration

## Environment

<!-- ubuntu -->
[![Ubuntu](https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A)](https://ubuntu.com/) <!-- bash -->
[![Bash](https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A)](https://www.gnu.org/software/bash/) <!-- vim -->
[![Vim](https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A)](https://www.vim.org/) <!-- vs code -->
[![VS Code](https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A)](https://code.visualstudio.com/)

* ``ubuntu``
* ``bash``
* ``ssh``
* ``vim`` ``VS Code``
* ``ufw``
* ``telnet``
* ``netstat``

## Run the code

> check if a given socket is open

```bash
vagrant@ubuntu-xenial:~$ telnet web-01.xelar.tech 22
Trying 35.231.236.4...
Connected to web-01.xelar.tech.
Escape character is '^]'.
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.4
Connection closed by foreign host.
vagrant@ubuntu-xenial:~$ telnet web-01.xelar.tech 2222
Trying 35.231.236.4...
^C
vagrant@ubuntu-xenial:~$
```

> blocks all incoming traffic, except the following TCP ports:
>
> 22 (SSH)
>
> 443 (HTTPS SSL)
>
> 80 (HTTP)
>

```bash
ubuntu@3284-web-01:~$ ufw --version
ufw 0.36
Copyright 2008-2015 Canonical Ltd.
ubuntu@3284-web-01:~$ man ufw
ubuntu@3284-web-01:~$ sudo ufw allow 22/tcp
Rules updated
Rules updated (v6)
ubuntu@3284-web-01:~$ sudo ufw allow 443/tcp
Rules updated
Rules updated (v6)
ubuntu@3284-web-01:~$ sudo ufw allow 80/tcp
Rules updated
Rules updated (v6)
ubuntu@3284-web-01:~$ sudo ufw status verbose
Status: inactive
ubuntu@3284-web-01:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
ubuntu@3284-web-01:~$ sudo ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), disabled (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
80/tcp (Nginx HTTP)        ALLOW IN    Anywhere
22/tcp                     ALLOW IN    Anywhere
443/tcp                    ALLOW IN    Anywhere
80/tcp                     ALLOW IN    Anywhere
80/tcp (Nginx HTTP (v6))   ALLOW IN    Anywhere (v6)
22/tcp (v6)                ALLOW IN    Anywhere (v6)
443/tcp (v6)               ALLOW IN    Anywhere (v6)
80/tcp (v6)                ALLOW IN    Anywhere (v6)
```

> install netstat

```bash
ubuntu@3284-web-01:~$ sudo apt-get update
ubuntu@3284-web-01:~$ sudo apt-get install net-tools
```

```bash
ubuntu@3284-web-01:~$ netstat --version
```

> listening server sockets, PID/program name for socket, dont resolve names

```bash
ubuntu@3284-web-01:~$ netstat -lpn
```
```bash
ubuntu@3284-web-01:~$ grep listen /etc/nginx/sites-enabled/default
	listen 80 default_server;
	listen [::]:80 default_server;
	# listen 443 ssl default_server;
	# listen [::]:443 ssl default_server;
#	listen 80;
#	listen [::]:80;
ubuntu@3284-web-01:~$
```

```bash
vagrant@ubuntu-xenial:~$ curl -sI web-01.xelar.tech:80
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 24 Jan 2022 22:10:07 GMT
Content-Type: text/html
Content-Length: 17
Last-Modified: Mon, 24 Jan 2022 06:34:06 GMT
Connection: keep-alive
ETag: "61ee485e-11"
X-Served-By: 3284-web-01
Accept-Ranges: bytes

vagrant@ubuntu-xenial:~$ curl -sI web-01.xelar.tech:8080
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 24 Jan 2022 22:10:13 GMT
Content-Type: text/html
Content-Length: 17
Last-Modified: Mon, 24 Jan 2022 06:34:06 GMT
Connection: keep-alive
ETag: "61ee485e-11"
X-Served-By: 3284-web-01
Accept-Ranges: bytes

vagrant@ubuntu-xenial:~$
```

> firewall redirects port 8080/TCP to port 80/TCP.

> change config file

```bash
ubuntu@3284-web-01:~$ sudo vim /etc/ufw/before.rules
```

> add at the top

```
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT
```

```bash
ubuntu@3284-web-01:~$ sudo ufw reload
Firewall reloaded
```
## Author

<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+24K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
