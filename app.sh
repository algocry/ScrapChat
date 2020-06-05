#!/bin/bash
if [ $1 = "-v" ] 
then echo 'Scrap Chat v0.1' 
else 
	xterm -fa 'Monospace' -fs 14 -T "ScrapChat <recieve>" -bg black -fg green -e 'python3 listen.py'&
	xterm -fa 'Monospace' -fs 10 -T "ScrapChat <send>" -bg black -fg green -e 'python3 chat.py'
fi
