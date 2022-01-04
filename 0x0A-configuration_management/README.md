# 0x0A. Configuration management

```puppet
                              _
 _ __  _   _ _ __  _ __   ___| |_
| '_ \| | | | '_ \| '_ \ / _ \ __|
| |_) | |_| | |_) | |_) |  __/ |_
| .__/ \__,_| .__/| .__/ \___|\__|
|_|         |_|   |_|

```

## Learning Objectives

### General

* Intro to Configuration Management
* Puppet’s Declarative Language: Modeling Instead of Scripting
* Puppet lint
* Puppet emacs mode

## Environment

<div>
<!-- Ubuntu --> <a href="https://ubuntu.com/" target="_blank"><img height="36px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/ubuntu-icon.svg" alt="Ubuntu"> </a> <!-- GNU Bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"><img height="36px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/gnu-bash-logo.svg" alt="GNU Bash">
<!-- Puppet --> <a href="https://puppet.com/" target="_blank"><img height="36px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/puppet.svg" alt="Puppet configuration manager">
</div>

* OS: Ubuntu 20.04 LTS
* Terminal: Bash 5.0.17
* Puppet
* Style guidelines: [Puppet Style Guide](https://docs.puppet.com/puppet/latest/style_guide.html)
* [Puppet lint](https://docs.puppet.com/puppet/latest/reference/puppet_lint.html)

## Install puppet

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$
$ apt-get install -y ruby-augeas
$
$ apt-get install -y ruby-shadow
$
$ apt-get install -y puppet
$
```

## Install puppet-lint

```bash
$ gem install puppet-lint
$
```

## execute scripts

```bash
# puppet-lint --version
puppet-lint 2.5.2
# puppet-lint 0-create_a_file.pp
#
# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
#
# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
# cat /tmp/school
I love Puppet
$
```

```bash
# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for d391259bf577 in environment production in 0.14 seconds
Notice: Applied catalog in 0.20 seconds
# gem list

*** LOCAL GEMS ***

puppet-lint (2.5.0)
#
```

```bash
Terminal #0 - starting my process

# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

# ./killmenow
```

Terminal #1 - executing my manifest

```bash
# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
#
```

Terminal #0 - process has been terminated

```bash
# ./killmenow
Terminated
#
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
