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
net-tools 2.10-alpha
Fred Baumgarten, Alan Cox, Bernd Eckenfels, Phil Blundell, Tuan Hoang, Brian Micek and others
+NEW_ADDRT +RTF_IRTT +RTF_REJECT +FW_MASQUERADE +I18N +SELINUX
AF: (inet) +UNIX +INET +INET6 +IPX +AX25 +NETROM +X25 +ATALK +ECONET +ROSE -BLUETOOTH
HW:  +ETHER +ARC +SLIP +PPP +TUNNEL -TR +AX25 +NETROM +X25 +FR +ROSE +ASH +SIT +FDDI +HIPPI +HDLC/LAPB +EUI64 
```

> listening server sockets, PID/program name for socket, dont resolve names

```bash
ubuntu@3284-web-01:~$ netstat -lpn
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
udp        0      0 127.0.0.1:323           0.0.0.0:*                           -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.10.0.180:68          0.0.0.0:*                           -                   
udp6       0      0 ::1:323                 :::*                                -                   
raw6       0      0 :::58                   :::*                    7           -                   
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
unix  2      [ ACC ]     STREAM     LISTENING     343372   17522/systemd        /run/user/1000/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     343378   17522/systemd        /run/user/1000/bus
unix  2      [ ACC ]     STREAM     LISTENING     343379   17522/systemd        /run/user/1000/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     13313    -                    @/org/kernel/linux/storage/multipathd
unix  2      [ ACC ]     STREAM     LISTENING     343380   17522/systemd        /run/user/1000/gnupg/S.gpg-agent.browser
unix  2      [ ACC ]     STREAM     LISTENING     343381   17522/systemd        /run/user/1000/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     343382   17522/systemd        /run/user/1000/gnupg/S.gpg-agent.ssh
unix  2      [ ACC ]     STREAM     LISTENING     343383   17522/systemd        /run/user/1000/gnupg/S.gpg-agent
unix  2      [ ACC ]     STREAM     LISTENING     343384   17522/systemd        /run/user/1000/pk-debconf-socket
unix  2      [ ACC ]     STREAM     LISTENING     343385   17522/systemd        /run/user/1000/snapd-session-agent.socket
unix  2      [ ACC ]     STREAM     LISTENING     19471    -                    /var/snap/lxd/common/lxd/unix.socket
unix  2      [ ACC ]     STREAM     LISTENING     13300    -                    /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     13302    -                    /run/systemd/userdb/io.systemd.DynamicUser
unix  2      [ ACC ]     STREAM     LISTENING     13311    -                    /run/lvm/lvmpolld.socket
unix  2      [ ACC ]     STREAM     LISTENING     13316    -                    /run/systemd/fsck.progress
unix  2      [ ACC ]     STREAM     LISTENING     13326    -                    /run/systemd/journal/stdout
unix  2      [ ACC ]     SEQPACKET  LISTENING     13331    -                    /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     14313    -                    /run/systemd/journal/io.systemd.journal
unix  2      [ ACC ]     STREAM     LISTENING     19470    -                    @ISCSIADM_ABSTRACT_NAMESPACE
unix  2      [ ACC ]     STREAM     LISTENING     19466    -                    /run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     19473    -                    /run/snapd.socket
unix  2      [ ACC ]     STREAM     LISTENING     19475    -                    /run/snapd-snap.socket
unix  2      [ ACC ]     STREAM     LISTENING     19478    -                    /run/uuidd/request
```

> firewall redirects port 8080/TCP to port 80/TCP.

> allow 8080 traffic

```bash
sudo ufw allow 8080/tcp
```

> change config file

```bash
ubuntu@3284-web-01:~$ sudo vim /etc/ufw/before.rules
```

> add at the top

```
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
COMMIT
```

```bash
ubuntu@3284-web-01:~$ sudo ufw reload
Firewall reloaded
```
# Author

<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+21K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
