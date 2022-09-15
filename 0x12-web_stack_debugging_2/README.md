# 0x12. Web stack debugging #2

```bash

         ((((c,               ,7))))
        (((((((              ))))))))
         (((((((            ))))))))
          ((((((@@@@@@@@@@@))))))))
           @@@@@@@@@@@@@@@@)))))))
        @@@@@@@@@@@@@@@@@@))))))@@@@
       @@/,:::,\/,:::,\@@@@@@@@@@@@@@
       @@|:::::||:::::|@@@@@@@@@@@@@@@
       @@\':::'/\':::'/@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@@\
             /    \        (     \
            (      )        \     \
             \    /          \
```

## General

* Web stack debugging

## Environment

<!-- ubuntu -->
[![Ubuntu](https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A)](https://ubuntu.com/) <!-- bash -->
[![Bash](https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A)](https://www.gnu.org/software/bash/) <!-- vim -->
[![Vim](https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A)](https://www.vim.org/) <!-- vs code -->
[![VS Code](https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A)](https://code.visualstudio.com/)

* OS: ``ubuntu`` 14.04 LTS
* Style guidelines: ``shelcheck`` 0.3.7
* Shell: ``bash``
* Shebang: `` #!/usr/bin/env bash``
* Editor: ``vim``, ``VS Code``
* ``ssh``
* ``whoami``
* ``sudo``

## Run the code

> run anything as another user

```bash
root@c80cd6823986:/# whoami
root
root@c80cd6823986:/# ./0-iamsomeoneelse www-data
www-data
root@c80cd6823986:/# whoami
root
root@c80cd6823986:/#
```

> run Nginx as ``nginx`` user

```bash
root@c80cd6823986:/# ps auxff
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root       141  0.0  0.0  18256  2452 pts/0    Ss   22:33   0:00 /bin/bash
root       823  0.0  0.0  15572  2080 pts/0    R+   23:26   0:00  \_ ps auxff
root         1  0.0  0.0  17976   296 ?        Ss   22:32   0:00 /bin/bash ./tmp/run.sh
root       140  0.0  0.0  61388   244 ?        S    22:32   0:00 /usr/sbin/sshd -D
root       816  0.0  0.0  85944  2768 ?        Ss   23:26   0:00 nginx: master process /usr/sbin/nginx
nobody     817  0.0  0.0  86248  3512 ?        S    23:26   0:00  \_ nginx: worker process
nobody     818  0.0  0.0  86248  3512 ?        S    23:26   0:00  \_ nginx: worker process
nobody     820  0.0  0.0  86248  3512 ?        S    23:26   0:00  \_ nginx: worker process
nobody     821  0.0  0.0  86248  3512 ?        S    23:26   0:00  \_ nginx: worker process
root@c80cd6823986:/# ps auxff | grep ngin[x]
root       816  0.0  0.0  85944  2768 ?        Ss   23:26   0:00 nginx: master process /usr/sbin/nginx
nobody     817  0.0  0.0  86248  3512 ?        S    23:26   0:00  \_ nginx: worker process
nobody     818  0.0  0.0  86248  3512 ?        S    23:26   0:00  \_ nginx: worker process
nobody     820  0.0  0.0  86248  3512 ?        S    23:26   0:00  \_ nginx: worker process
nobody     821  0.0  0.0  86248  3512 ?        S    23:26   0:00  \_ nginx: worker process
root@c80cd6823986:/# nc -z 0 8080 ; echo $?
0
root@c80cd6823986:/# nc -z 0 80 ; echo $?
```

## Author

<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+27K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
