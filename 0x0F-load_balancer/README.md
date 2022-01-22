# 0x0F. Load balancer

## General

### Concepts

* Load balancer
* Web stack debugging

## Environment

<!-- ubuntu -->
[![Ubuntu](https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A)](https://ubuntu.com/) <!-- bash -->
[![Bash](https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A)](https://www.gnu.org/software/bash/) <!-- vim -->
[![Vim](https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A)](https://www.vim.org/) <!-- vs code -->
[![VS Code](https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A)](https://code.visualstudio.com/)

* Ubuntu 16.04 LTS
* Shell: Bash 4.3
* Style guidelines: ``shellcheck`` 0.3.7
* ``vim``, ``VS Code``
* ``haproxy`` 1.6.*

## Run the code

```bash
vagrant@ubuntu-xenial:~$ curl -sI 35.231.236.4 | grep X-Served-By
X-Served-By: 3284-web-01
vagrant@ubuntu-xenial:~$ curl -sI 34.74.187.179 | grep X-Served-By
X-Served-By: 3284-web-02
vagrant@ubuntu-xenial:~$
```

_On load balancer server_

```bash
vagrant@ubuntu-xenial:~$ curl -sI 54.165.191.52
HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Sat, 22 Jan 2022 00:17:36 GMT
content-type: text/html
content-length: 13
last-modified: Tue, 11 Jan 2022 02:41:04 GMT
etag: "61dcee40-d"
x-served-by: 3284-web-01
accept-ranges: bytes
connection: close

vagrant@ubuntu-xenial:~$ curl -sI 54.165.191.52
HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Sat, 22 Jan 2022 00:17:44 GMT
content-type: text/html
content-length: 612
last-modified: Fri, 21 Jan 2022 21:05:10 GMT
etag: "61eb2006-264"
x-served-by: 3284-web-02
accept-ranges: bytes
connection: close

vagrant@ubuntu-xenial:~$ 
```

## Author

<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+21K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
