#!/usr/bin/python
#coding=utf-8
import sys
import os, os.path
import dircache
import commands
def add(x,y):
    return x*y
 
def trans(dirname):
    lis = dircache.opendir(dirname)
    for a in lis:
        af=dirname+os.sep+a
##        print af
        if os.path.isdir(af):
##            print af
            trans(af)
        else:
    ##        print af+"encoding="+fi.name
            ft = commands.getoutput('file -i '+af)
##            print ft
            if a.find('.htm')==-1 and a.find('.xml')==-1 and ft.find('text/')!=-1 and ft.find('iso-8859')!=-1:
                print 'gbk'+ft+"   >"+af
                commands.getoutput('iconv -ficonv -f gbk -t utf-8 -c -o'+" "+af+" "+af)
 
trans(os.getcwd())
