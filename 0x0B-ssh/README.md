# 0x0B. SSH

```puppet
  ad8888888888ba
 dP'         `"8b,
 8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
 8  8' `8           "88baadP""""YbaaadP"""YbdP""Yb
 8  8   8              """        """      ""    8b
 8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
 8  `"""'       ,d8""
 Yb,         ,ad8"
  "Y8888888888P"
```

## Learning Objectives

### General

* What is a (physical) server
* SSH essentials
* SSH Config File
* Public Key Authentication for SSH

## man or help

* ```ssh```
* ```ssh-keygen```
* ```env```

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

### install the OpenSSH client

```bash
$ sudo apt-get install openssh-client
$
```

## Execute

```bash
$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
$
```

```bash
$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school
Your public key has been saved in school.pub
The key fingerprint is:
SHA256:7vxuWOhoZPFYW1h3DeIaF+MZqFtfYXx1IpX2fdOLqRk root@9d03faf1f602
The key's randomart image is:
+---[RSA 4096]----+
|           .*o+++|
|          oo.BB.+|
|         +..=+ +o|
|      . + o+  ..=|
|       =S*.. .o +|
|      +.= .E.o . |
|     o o.o  +    |
|      ooo .o     |
|     .  o+o      |
+----[SHA256]-----+
$
```

Add the SSH public key to the server

``sudo vim ~/.ssh/authorized_keys``

and add the key

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
