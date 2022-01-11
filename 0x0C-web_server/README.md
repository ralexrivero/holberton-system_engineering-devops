# 0x0C. Web server

```bash
██████╗  ██████╗  ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║  ██║██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██║  ██║██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```

## Learning Objectives

### General

* How the web works
* Nginx
* Child process
* Root and sub domain
* HTTP requests
* HTTP redirection
* Not found HTTP response code
* Logs files on Linux

## man or help

* ```scp```
* ```curl```

## Environment

<div>
<!-- Ubuntu --> <a href="https://ubuntu.com/" target="_blank"><img height="36px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/ubuntu-icon.svg" alt="Ubuntu"> </a> <!-- GNU Bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"><img height="36px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/gnu-bash-logo.svg" alt="GNU Bash">
<!-- Puppet --> <a href="https://puppet.com/" target="_blank"><img height="36px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/puppet.svg" alt="Puppet configuration manager">
</div>

* OS: Ubuntu 20.04 LTS
* Terminal: Bash 5.0.17
* Puppet
* Style guidelines puppet: [Puppet Style Guide](https://docs.puppet.com/puppet/latest/style_guide.html)
* [Puppet lint](https://docs.puppet.com/puppet/latest/reference/puppet_lint.html)
* [Shellcheck (version 0.7.0)](https://github.com/koalaman/shellcheck#installing)
* [Shellcheck issues](https://github.com/koalaman/shellcheck/wiki/SC2034)

## Execute

Server

```bash
ubuntu@3284-web-01:~$ ./1-install_nginx_web_server > /dev/null 2>&1
ubuntu@3284-web-01:~$ curl localhost
Hello World!
ubuntu@3284-web-01:~$
```

Terminal

```bash
vagrant@ubuntu-xenial:~$ curl 35.231.236.4
Hello World!
vagrant@ubuntu-xenial:~$ curl -sI 35.231.236.4/
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 11 Jan 2022 02:20:48 GMT
Content-Type: text/html
Content-Length: 13
Last-Modified: Tue, 11 Jan 2022 02:12:24 GMT
Connection: keep-alive
ETag: "61dce788-d"
Accept-Ranges: bytes
vagrant@ubuntu-xenial:~$
```

```bash
vagrant@ubuntu-xenial:~$ dig xelar.tech

; <<>> DiG 9.10.3-P4-Ubuntu <<>> xelar.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 16459
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;xelar.tech.			IN	A

;; ANSWER SECTION:
xelar.tech.		4502	IN	A	34.138.102.220

;; Query time: 1605 msec
;; SERVER: 10.0.2.3#53(10.0.2.3)
;; WHEN: Tue Jan 11 02:25:44 UTC 2022
;; MSG SIZE  rcvd: 55

vagrant@ubuntu-xenial:~$
```

```bash
vagrant@ubuntu-xenial:~$ curl -sI 35.231.236.4/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 11 Jan 2022 02:30:01 GMT
Content-Type: text/html
Content-Length: 178
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

vagrant@ubuntu-xenial:~$
```

```bash
vagrant@ubuntu-xenial:~$ curl -sI 35.231.236.4/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 11 Jan 2022 02:45:07 GMT
Content-Type: text/html
Content-Length: 24
Connection: keep-alive
ETag: "61dcee40-18"

vagrant@ubuntu-xenial:~$ curl 35.231.236.4/xyz
Ceci n'est pas une page
vagrant@ubuntu-xenial:~$
```

## Autor

>```Ronald Rivero```

## Connect

<br>
<div>
<!-- Twitter -->
<a href="https://twitter.com/ralex_uy" target="_blank"> <img align="left" alt="Ronald Rivero | Twitter" src="https://img.shields.io/twitter/follow/ralex_uy?style=social"/> </a>
<!-- Linkedin -->
<a href="https://www.linkedin.com/in/ronald-rivero/" target="_blank"> <img align="left" alt="Ronald Rivero | LinkedIn" src="https://img.shields.io/badge/LinkedIn-Follow-blue?style=social&logo=linkedin"/> </a>
<!-- Github -->
<a href="https://github.com/ralexrivero/" target="_blank"> <img align="left" src="https://img.shields.io/github/followers/ralexrivero?style=social" alt="Ralex | Github"> </a>
</br>
</div>
