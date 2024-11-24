#!/usr/bin/bash

LGREEN='\033[1;32m'
NC='\033[0m'

read -p "$(echo -e $LGREEN"Introduce la jerarquía y su grupo de notícias (ejemplo: es.charla) "${NC})" hierarchy

cat ~/.jnewsrc.original | grep ${hierarchy} > ~/.tmp.jnewsrc
sed -i 's/!/:/g' ~/.tmp.jnewsrc
mv ~/.tmp.jnewsrc ~/.jnewsrc
