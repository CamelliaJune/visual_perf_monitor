#!/usr/bin/env python2
#-*- coding: utf-8 -*-
import re
import os
import sys
import datetime
import time
from cmdLib import *

class perfmonitor_gpu(object):
    def __init__(self, monitor_time):
        self.monitor_time = monitor_time
        self.perflog = "./perflog/"
        self.perfimg = "./perfimg/"
        status,output=cmd_execute("rm " + self.perflog + "*")
    def perfrunner(self):
        try:
            monitorsecond = self.monitor_time * 60
            begintime = (int)(time.time())
            while(((int)(time.time()) - begintime) <= monitorsecond):
                current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cmd = "nvidia-smi | grep 'MiB' | grep 'W' | awk '{print $13}'"
                gpuusage0 = os.popen(cmd).read().strip("\n").replace("%", "").split('\n')[0]
                gpuusage1 = os.popen(cmd).read().strip("\n").replace("%", "").split('\n')[1]
                cmd = "nvidia-smi | grep 'MiB' | grep 'W' | awk '{print $9}'"
                mem0 = os.popen(cmd).read().strip("\n").replace("MiB", "").split('\n')[0]
                mem1 = os.popen(cmd).read().strip("\n").replace("MiB", "").split('\n')[1]
                print mem0
                print mem1
                cmd = "nvidia-smi | grep 'MiB' | grep 'W' | awk '{print $11}'"
                total_mem0 = os.popen(cmd).read().strip("\n").replace("MiB", "").split('\n')[0]
                total_mem1 = os.popen(cmd).read().strip("\n").replace("MiB", "").split('\n')[1]
                print total_mem0
                print total_mem1
                memusage0 = round(float(mem0) / float(total_mem0), 4) * 100
                memusage1 = round(float(mem1) / float(total_mem1), 4) * 100
                print memusage0
                print memusage1

                memusagestr0 = current + "\t" + str(memusage0) + "\n"
                memusagestr1 = current + "\t" + str(memusage1) + "\n"
                gpuusagestr0 = current + "\t" + str(gpuusage0) + "\n"
                gpuusagestr1 = current + "\t" + str(gpuusage1) + "\n"

                memusagestr_filepath0 = self.perflog + "gpu-mem-whole-0.log"
                memusagestr_filepath1 = self.perflog + "gpu-mem-whole-1.log"
                gpuusagestr_filepath0 = self.perflog + "gpu-whole-0.log"
                gpuusagestr_filepath1 = self.perflog + "gpu-whole-0.log"

                fp=open(memusagestr_filepath0,"a")
                fp.write(memusagestr0)
                fp.close()
                fp=open(memusagestr_filepath1,"a")
                fp.write(memusagestr1)
                fp.close()
                fp=open(gpuusagestr_filepath0,"a")
                fp.write(gpuusagestr0)
                fp.close()
                fp=open(gpuusagestr_filepath1, "a")
                fp.write(gpuusagestr1)
                fp.close()

                time.sleep(1)

            #now = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
            #cmdstr = "tar -czf perflog." + now + ".tar.gz " + self.perflog
            #status,output = cmd_execute(cmdstr)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("""======================================================================================
|                              Usage Instructions                                    |
======================================================================================""")
        print("""|  usage              : python perfmonitor_gpu.py MonitorTime""")
        print("""|  example            : python perfmonitor_gpu.py 1""")
        print("""======================================================================================""")
        sys.exit()
    monitor_time = int(sys.argv[1])
    perfm = perfmonitor_gpu(monitor_time)
    perfm.perfrunner()