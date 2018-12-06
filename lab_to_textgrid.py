#!/usr/bin/python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "errrolyan"
# Date: 18-10-16
# Describe = "lab_to_lab的输出结果.lab 输入到 praat 修正lab的元音和辅音的分界值”
import sys
import re

usage = 'Usage: ./lab_to_textgrid.py input.lab output.TextGrid'

if len(sys.argv) != 3:
    print usage
    exit()

ifname = sys.argv[1]
ofname = sys.argv[2]

inf = open(ifname, 'r')
outf = open(ofname, 'w')

# get info from .lab
labs = []
for line in inf:
    if not re.search('^\s*\d+\s*\d+\s*\S+', line): #regular expresion for "space number space number space word"
        continue
    tokens = line.split()
    time = tokens[1].strip()
    label = tokens[2].strip()
    labs.append((str(int(time)/10000000.0), label))

maxtime = str(labs[-1][0])

# boilerplate
outf.write('File type = "ooTextFile"\n')
outf.write('Object class = "TextGrid"\n')
outf.write('\n')
outf.write('xmin = 0\n')
outf.write('xmax = ' + maxtime + '\n')
outf.write('tiers? <exists>\n')
outf.write('size = 1\n')
outf.write('item []:\n')
outf.write('    item [1]:\n')
outf.write('        class = "IntervalTier"\n')
outf.write('        name = "labels"\n')
outf.write('        xmin = 0\n')
outf.write('        xmax = ' + maxtime + '\n')
outf.write('        intervals: size = ' + str(len(labs)) + '\n')

# intervals
count = 0
prevtime = '0'
for elt in labs:
    count += 1
    outf.write('        intervals [' + str(count) + ']:\n')
    outf.write('            xmin = ' + prevtime + '\n')
    outf.write('            xmax = ' + elt[0] + '\n')
    outf.write('            text = "' + elt[1] + '"\n')
    prevtime = elt[0]

inf.close()
outf.close()
