#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy
import math
#import pytz
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
import datetime
import time

import sys
import datetime
import time
import os
from cmdLib import *

def get_mem_stat_data(filepath):
    fp=open(filepath)
    mem_stat_data=[]
    for line in fp:
        line=line.strip()
        line_list=line.split("\t")
        mem_stat_data.append(line_list)
    fp.close()
    return mem_stat_data

def get_query_period_distribution_plot(stat_type, mem_stat_data, savefile):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xaxis = ax.xaxis
    yaxis = ax.yaxis
    yList=[]
    dateList=[]
    for item in mem_stat_data:
        dateList.append(item[0])
        try:
            assert(type(eval(item[1])) == float or type(eval(item[1])) == int)
            yList.append(item[1])
        except:
            yList.append(0)
    #print dateList
    #print len(dateList)
    #print yList

    dates=[datetime.datetime.strptime(item, "%Y-%m-%d %H:%M:%S") for item in dateList]
    ax.plot_date(dates,  yList,  'm-',  marker='.',  linewidth=1)

    ax.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d %H:%M:%S') )
    ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')

    name=savefile.split("/")[2].split(".")[0]
    plt.title(name)
    plt.xlabel(u'Time')
    if(stat_type == "mem"):
        plt.ylabel(u'memUsage-%')
    elif(stat_type == "cpu"):
        plt.ylabel(u'cpuUsage-%')
    plt.grid(True)


    fig.autofmt_xdate()
    plt.savefig(savefile)

if __name__ == '__main__':
    if(len(sys.argv) != 1):

        print("""|  usage              : python drawPng.py""")
        print("""|  example            : python drawPng.py""")
        print("""======================================================================================""")
        sys.exit()
    file_dir = "./perflog/"
    img_file_dir = "./perfimg/"

    status, output = cmd_execute("rm " + img_file_dir + "*")
    file_list = os.listdir(file_dir)
    #print file_list
    for item in file_list:

        if(item.split("-")[0] == "cpu"):
            stat_type = "cpu"
        elif(item.split("-")[0] == "mem"):
            stat_type = "mem"
        elif(item.split("-")[0] == "gpu"):
            stat_type = "gpu"
        elif(item.split("-")[0] == "gpu-mem"):
            stat_type = "gpu-mem"
        if(os.path.isfile(file_dir+item)):
            mem_stat_data=get_mem_stat_data(file_dir+item)
            get_query_period_distribution_plot(stat_type, mem_stat_data, img_file_dir + item + ".perf.png")
