#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':      # this way the module can be
    genseed = "python simpleradar.py '%s' radar4all/r4-%s-%d.png"
    seedsh = '''#!/bin/sh
    %s
    '''
    #  python simpleradar.py [5,3,5,5] r4doubanFM-5355-90.png
    pli = []    # [[分数列],分数名列,分合值,总评]
    i = range(1,6)
    j = range(1,6)
    k = range(1,6)
    l = range(1,6)
    count = 0
    for m in range(0,5):
        for n in range(0,5):
            for o in range(0,5):
                for p in range(0,5):
                    #print i[m],j[n],k[o],l[p],(m+n+o+p)*100/20.0
                    pli.append([[i[m],j[n],k[o],l[p]]
                        ,"%s%s%s%s"% (i[m], j[n], k[o], l[p])
                        ,(m+n+o+p+4)
                        ,((m+n+o+p+4)*100/20.0)])
                    count += 1
    print count
    exp = ""
    for c in pli:
        exp += "\n"+genseed%(c[0],c[1],c[-1])
    #print exp
    open("gen4allrader.sh","w").write(seedsh%exp)
