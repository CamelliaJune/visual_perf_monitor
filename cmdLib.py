#!/usr/bin/env python2
#-*- coding: utf-8 -*-
import sys
import os
sys.path.append("%s/../"%os.path.dirname(os.path.realpath(__file__)))

import subprocess
import commands

def cmd_execute(cmd,mode="commands"):
    if(mode == "subprocess"):
        ps=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        ps.wait()
        stdout,stderror=ps.communicate()
        return stdout,stderror
    if(mode == "commands"):
        status,output=commands.getstatusoutput(cmd)
        return status,output


