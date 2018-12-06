#！/usr/bin/env python
#coding:utf8
#__Author__="Errol Yan"
#__Date__="2018-12-04"
#__Describe__="读写labels”

import os
import json

class labelsRW():

    """定义一个读写类"""
    def __init__(self,pathDir):

        self.pathDir = pathDir
        self.Wdata = ""
        self.Rdata = {}
        self.conunt={}

    def labWrite(self):
        print(self.Wdata)

    def labRead(self):
        pathfile = os.listdir(self.pathDir)
        for lab in pathfile:
            lab_name = lab[0:26]
            print(lab_name)
            lab_path = os.path.join(self.pathDir,lab)
            with open(lab_path,"r") as lab_text:
                for line in lab_text:
                    list = line.split()
                    print(list)
                    time =int(list[1])-int(list[0])

                    if list[2] in self.conunt.keys():
                        self.Rdata[list[2]] = self.Rdata[list[2]]+time/10000
                        self.conunt[list[2]] = self.conunt[list[2]]+1
                    else:
                        self.Rdata[list[2]]=time/10000
                        self.conunt[list[2]]=1
        json_time = json.dumps(self.Rdata,indent=4)
        json_count =json.dumps(self.conunt,indent=4)
        with open("Result.json","w") as wjson:
            wjson.write(json_time)
            wjson.write(json_count)
        return self.conunt,self.Rdata

if __name__ =="__main__":
    lab = labelsRW("./labels/mono/")
    print(lab.labRead())