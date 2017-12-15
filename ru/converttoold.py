#!/usr/bin/env python
import codecs
import sys

vof = codecs.open('verb-obj.ei','w',encoding='utf-8')
svf = codecs.open('subj-verb.ei','w',encoding='utf-8')

with codecs.open('seeds.ei','r',encoding='utf-8') as inf:
    for line in inf:
        (s, v, o) = line.strip().split(None,2)
        if s=='-':
            print >> vof, u'{0}, {1}'.format(v, o)
        elif o=='-':
            print >> svf, u'{0}, {1}'.format(v, s)
