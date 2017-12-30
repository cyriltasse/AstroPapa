#!/usr/bin/env python
import sys
import fnmatch
import os
from cr2fits import cr2fits


def GiveList(Patern="*.c"):
    matches = []
    for root, dirnames, filenames in os.walk('.'):
        for filename in fnmatch.filter(filenames, Patern):
            matches.append(os.path.join(root, filename))

    m=[os.path.abspath(f) for f in matches]
    return m

def Convert(Patern="*.c"):
    L=GiveList(Patern)
    for l in L:
        print "Converting Image %s"%l
        for s in range(3):
            print "  doing slice %i"%s
            a = cr2fits(l, s)
            a.convert()


            
if __name__=="__main__":
    Patern=sys.argv[1]
    Convert(Patern)
