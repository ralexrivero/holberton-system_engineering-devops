# 0x14. MySQL

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
``ps ax | grep mysql
``ls -al /usr/sbin/mysql*``
``ls -al /usr/bin/mysql*``
``ls -al /usr/lib/mysql*``
``ls -al /var/lib/mysql*``
* download deb package
``curl -O https://repo.mysql.com//mysql-apt-config_0.8.22-1_all.deb``
* update
``sudo apt-get update``
* install mysql
``sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb``


## Author

<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+21K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)