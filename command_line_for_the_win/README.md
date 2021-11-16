# Command line for the win

```bash
 ██████  ██████  ███    ███ ███    ███  █████  ███    ██ ██████      ██      ██ ███    ██ ███████
██      ██    ██ ████  ████ ████  ████ ██   ██ ████   ██ ██   ██     ██      ██ ████   ██ ██
██      ██    ██ ██ ████ ██ ██ ████ ██ ███████ ██ ██  ██ ██   ██     ██      ██ ██ ██  ██ █████
██      ██    ██ ██  ██  ██ ██  ██  ██ ██   ██ ██  ██ ██ ██   ██     ██      ██ ██  ██ ██ ██
 ██████  ██████  ██      ██ ██      ██ ██   ██ ██   ████ ██████      ███████ ██ ██   ████ ███████
```

## Background Context

CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

## Environment

<div>
<!-- ubuntu -->
<a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Suite CRM"></a>
<!-- vim -->
<a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="Suite CRM"></a>
<!-- bash -->
  <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="terminal"></a>

</div>

<!-- cmd challente -->
* <a href="https://cmdchallenge.com/" target="_blank"> cmdchallenge.com</a>

* Language: BASH scripting (executable)
  * #!/usr/bin/env bash

* OS: Ubuntu 20.04 LTS

* Editor: VIM 8.1.2269

* [Shellcheck (version 0.7.0)](https://github.com/koalaman/shellcheck#installing)

* [Shellcheck issues](https://github.com/koalaman/shellcheck/wiki/SC2034)

## command for the challenge

> Use ```man``` and ```help``` pages of each of the following commands

* ```echo```
* ```pwd```
* ```ls```
* ```cat```
* ```tail```
* ```touch```
* ```mkdir```
  * *```-p``` to create parent directories*
* ```cp```
* ```mv```

***

* ```ln``` *see the -s flag to create symbolic links*
* ```find```
  * *```-delete``` to delete files*
  * *```-iname``` to search for files in the current directory*
  * *```-type``` to search for files by type*
  > *```find . -iname '*.txt'``` to search for files with the extension .txt recursively*
* ```grep```
  > *```grep "pattern" file``` to search for a pattern in a file*
* *```-h``` nodisplay of the file name*
  > *```grep -l "pattern" *``` seach files matching a pattern and print only the filename without path*
* ```xargs``` *Run command with arguments INITIAL-ARGS and more args read from input*
* ```cut``` print selected parts of each line of a file
  > *```cut -d " " -f 1``` to print the first column of each line with a single space delimiter*
* ```wc``` *print newline, word and byte count for each file*
  > *```wc -l``` to print the number of lines in a file*

***

* ```sort``` *sort lines of a file*
  * ```-c``` *print the number of selected lines*
  > *```sort -r``` to reverse the order of the lines*
* ```tr``` *translate characters in a file*
  > *```tr "old" "new"``` to replace all occurrences of old with new*
* ```echo``` *print a line of text*
  * *```{1..10}``` to print a range of numbers*
  > *```echo "Hello World"``` to print the text "Hello World"*
* ```sed``` *stream editor*
  > *```sed "s/old/new/g"``` to replace all occurrences of old with new*
  > *```sed -i "text to delete//g" **/*txt * to delete the text and save the file*
* ```awk``` *programming language for manipulation of data files, text retrieval and processing, prototyping and experimenting with algorithms*
  > *```awk '{print $1}'``` to print the first column of each line*
* ```printf``` *print formatted output to stdout*
  > *```printf "%s\n" "Hello World"``` to print the text "Hello World"*
  > *```find -type f -printf '%f\n'``` to print the file's filename without the leading path recursively*
* ```rename``` *rename files*
  > *```rename "s/old/new/g"``` to replace all occurrences of old with new*
* ```mv``` *move files*
  > *```mv "old" "new"``` to rename old to new*
  > *```for file in $(find . -type f); do mv "$file" "${file%.*}"; done``` to rename all the files and remove extensions*



## Autor

```bash
Ronald Rivero
```

### contact

<br>
<div>
<a href="https://twitter.com/ralex_uy" target="_blank">  <img align="left" alt="Ronald Rivero | Twitter" src="https://img.shields.io/twitter/follow/ralex_uy?style=social"/> </a>

<a href="https://www.linkedin.com/in/ronald-rivero/" target="_blank">  <img align="left" alt="Ronald Rivero | LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=social&logo=linkedin"/> </a>

<a href="https://github.com/ralexrivero/" target="_blank">  <img align="left" src="https://img.shields.io/github/followers/ralexrivero?style=social" alt="Ralex | Github"> </a>
</br>
</div>
