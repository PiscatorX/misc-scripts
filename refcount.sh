#!/usr/bin/bash
    
grep  "year = {"  $1 | sed  's/year = {//g' | tr -d '},'  | sort.exe


