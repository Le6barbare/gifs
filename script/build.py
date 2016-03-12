#!/usr/bin/python3.3

import os

Path="img/"

ListDirectory = os.listdir("../"+Path)

with open('../_includes/site-index.html', 'w') as OpenFile:
    with open('../_data/static_files.yml', 'w') as StaticFile:
        OpenFile.write('<ul>')
        StaticFile.write('---\n')
        for Dir in ListDirectory:
            OpenFile.write('<li>'+Dir+'<ul>')
            ListFile = os.listdir("../"+Path+Dir)
            for File in ListFile:
                Link=str(Path+Dir+'/'+File)
                OpenFile.write('<li><span href="'+Link+'" class="gif" data-clipboard-text="'+Link+'">'+File+'</span></li>')
                StaticFile.write('- path: '+Link+'\n')
                StaticFile.write('  modified_time: '+str(int(os.path.getmtime("../"+Link)))+'\n')
                StaticFile.write('  extname: "'+os.path.splitext(File)[1]+'"\n')
            OpenFile.write('</ul></li>')
        OpenFile.write('</ul>')
