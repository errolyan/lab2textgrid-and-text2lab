#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "errrolyan"
# Date: 18-10-16
# Describe = "修正mono label有-1的问题”

import sys
import re
import os

def fileread_mono(filepath,filechange):
    pathDir = os.listdir(filepath)
    for s in pathDir:
        newDir = os.path.join(filepath, s)
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".lab":
                print(newDir)
                name = newDir[7:33]
                lab_in = filepath + name + ".lab"
                lab_out = filechange + name +".lab"
                inf = open(lab_in, 'r')  #ifname
                outf = open(lab_out, 'w')  #ofname
                labs = []
                for line in inf:
                   # print( line)
                    tokens = line.split()
                    print(tokens)
                    labs.append(tokens)
                print(len(labs))
                i = 0
                while len(labs) > i:
                    time = int(labs[i][1])
                    print(time)
                    if time < 0:
                        time1 = int(labs[i+1][1])-int(labs[i][0])
                        value1 = int(labs[i][0]) + int(time1 * 0.4)
                        labs[i][1] = str(value1)
                        labs[i+1][0] = str(value1)
                    i = i + 1
                print(labs)
                for iter in labs:
                    for i in iter:
                        outf.write(i+" ")
                    outf.write("\n")

def fileread_full(filepath,filechange):
    pathDir = os.listdir(filepath)
    for s in pathDir:
        newDir = os.path.join(filepath, s)
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".lab":
                print(newDir)
                name = newDir[7:33]
                lab_in = filepath + name + ".lab"
                lab_out = filechange + name +".lab"
                inf = open(lab_in, 'r')  #ifname
                outf = open(lab_out, 'w')  #ofname
                labs = []
                for line in inf:
                   # print( line)
                    tokens = line.split()
                    print(tokens)
                    labs.append(tokens)
                print(len(labs))
                i = 0
                while len(labs) > i:
                    time = int(labs[i][1])
                    print(time)
                    if time < 0:
                        time1 = int(labs[i+1][1])-int(labs[i][0])
                        value1 = int(labs[i][0]) + int(time1 * 0.4)
                        labs[i][1] = str(value1)
                        labs[i+1][0] = str(value1)
                    i = i + 1
                print(labs)
                for iter in labs:
                    for i in iter:
                        outf.write(i+" ")
                    outf.write("\n")

if __name__=="__main__":
    usage = 'Usage: ./lab_to_labs.py [labs_in_dir] [labs_out_dir]'

    if len(sys.argv) != 3:
        print (usage)
        exit()

    inpath = sys.argv[1]
    outpath = sys.argv[2]
fileread_mono(inpath,outpath)
fileread_full(inpath,outpath)
