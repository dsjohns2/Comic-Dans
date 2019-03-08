#!/bin/bash

sudo cp comicdans.tfm /usr/share/texmf/fonts/tfm/ 
sudo cp comicdans.pfb /usr/share/texmf/fonts/type1/ 
echo "comicdans ComicDans <comicdans.pfb" > comicdans.map
sudo cp comicdans.map /usr/share/texmf/fonts/map/dvips/ 
