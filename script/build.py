#!/usr/bin/python3.3

import os

Path="img/"

ListDirectory = os.listdir(Path)

with open('__includes/site-index.html', 'w') as OpenFile:
    OpenFile.write('<ul>')
    for Dir in ListDirectory:
        OpenFile.write('<li>'+Dir+'<ul>')
        ListFile = os.listdir(Path+Dir)
        for File in ListFile:
            OpenFile.write('<li><a href="./'+Path+Dir+'/'+File+'" class="gif">'+File+'</a></li>')
        OpenFile.write('</ul></li>')
    OpenFile.write('</ul>')