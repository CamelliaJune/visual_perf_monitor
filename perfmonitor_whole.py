#!/usr/bin/env python2
#-*- coding: utf-8 -*-
import sys
import datetime
import time
import psutil
from cmdLib import *

class perfmonitor_whole(object):
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
                memusage = psutil.virtual_memory().percent
                cpuusage = psutil.cpu_percent()
                memusagestr = current + "\t" + str(memusage) + "\n"
                cpuusagestr = current + "\t" + str(cpuusage) + "\n"

                memusagestr_filepath = self.perflog + "mem" + "-whole" + ".log"
                cpuusagestr_filepath = self.perflog + "cpu" + "-whole" + ".log"

                fp=open(memusagestr_filepath,"a")
                fp.write(memusagestr)
                fp.close()
                fp=open(cpuusagestr_filepath,"a")
                fp.write(cpuusagestr)
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
        print("""|  usage              : python perfmonitor_whole.py MonitorTime""")
        print("""|  example            : python perfmonitor_whole.py 1""")
        print("""======================================================================================""")
        sys.exit()
    monitor_time = int(sys.argv[1])
    perfm = perfmonitor_whole(monitor_time)
    perfm.perfrunner()

