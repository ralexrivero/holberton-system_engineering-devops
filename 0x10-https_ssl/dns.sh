#!/usr/bin/env bash
# dns info

awk 'NR==2{SUB=$1; REC=$4; DEST=$5; print "The subdomain " SUB, "is a " REC, "record and points to " DEST}' dns
