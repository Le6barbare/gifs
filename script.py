#!/usr/bin/python3.3

import os

Path="img/"

ListDirectory = os.listdir(Path)

with open('__includes/site-index.html', 'w') as OpenFile:
    with open('__data/static_files.yml', 'w') as StaticFile:
        OpenFile.write('<ul>')
        StaticFile.write('---\n')
        for Dir in ListDirectory:
            OpenFile.write('<li>'+Dir+'<ul>')
            ListFile = os.listdir(Path+Dir)
            for File in ListFile:
                OpenFile.write('<li><a href="./'+Path+Dir+'/'+File+'" class="gif">'+File+'</a></li>')
                StaticFile.write('- path: '+Path+Dir+'/'+File+'\n')
                StaticFile.write('  modified_time: 1430463202\n')
                StaticFile.write('  extname: "'+os.path.splitext(File)[1]+'"\n')
            OpenFile.write('</ul></li>')
        OpenFile.write('</ul>')