#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "errrolyan"
# Date: 18-10-16
# Describe = "读取sinsy官网的log文件，用于制作mono.label 和full.label”
import os,re

def fileread_log(pathlog):
    pathDir = os.listdir(pathlog)
    print(pathDir)
    pathmono = "./labels/mono/"
    pathfull = "./labels/full/"
    for i in pathDir:
        name = i[0:26]
        monolab = pathmono + name +".lab"
        fulllab = pathfull + name + ".lab"
        mono = open(monolab,"w+")
        full = open(fulllab,"w+")
        inf = open(pathlog+i, 'r')  # ifname
        str2 = ""
        for line in inf:
            if "Duration" not in line and "State" not in line and "PDF" not in line and "MSD" not in line and "HMM" not in line :
                if "Stream" not in line and "Interpolation" not in line and "Tree" not in line and "Re-alignment" not in line and "                                       ->" not in line :
                    if "F0 shift" not in line and "[Global parameter]" not in line and "Sampring frequency " not in line and "Frame period " not in line:
                        if "5.00000(msec)" not in line and "All-pass constant"not in line and "Gamma" not in line and "Postfiltering coefficient" not in line:
                            if "Audio buffer size" not in line and "Number of states" not in line and "Length of this speech" not in line:
                                if "GV" not in line and "Dynamic window size  " not in line and "Generated sequence" not in line and "Number of stats" not in line :
                                    if "Name" in line:
                                        str2 += "?"
                                    if line != "\n":
                                        line = re.sub(" ", "", line.strip())
                                        if line != "\n":
                                            str2 += line +"\n"

        v = str2.split('?')
        time_list = []
        yinsu_list = []
        full_list = []
        for elem in v:
            if elem != "":
                v = elem.split('\n')
                length = 0
                yinsu =""
                fulllabs=""
                for i in v:
                    if "Length->" in i:
                        a =int(re.sub("\D", "", i))
                        length += a
                    if "Name" in i:
                        yinsu =re.search(r'\-(\w+?)\+', i).group(1)
                        fulllabs= i[6:]
                time = length*5000
                time_list.append(time)
                yinsu_list.append(yinsu)
                full_list.append(fulllabs)
        time_list1 =[]
        time_list1.append(0)
        i = 1
        while i < len(time_list)*2:
            time_list1.append(time_list1[i-1]+time_list[int((i+1)/2)-1])
            if len(time_list1) != len(time_list)*2:
                time_list1.append(time_list1[i])
            i +=2
        print(len(time_list1),time_list1)
        i =0
        while i < len(yinsu_list):
            full.write(str(time_list1[2*i])+" "+str(time_list1[2*i+1])+" "+full_list[i]+"\n")
            mono.write(str(time_list1[2*i])+" "+str(time_list1[2*i+1])+" "+yinsu_list[i]+"\n")
            i +=1
        full.close()
        mono.close()
        inf.close()

if __name__=="__main__":
    usage = 'Usage: ./log_to_labs.py [Sinsy_log_dir]'
    if len(sys.argv) != 2:
        print(usage)
        exit()
    ifname = sys.argv[1]
    fileread_log(ifname)