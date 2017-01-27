# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:21:52 2017

Quick'n'Dirty way to write Arduino readings, originally sent 
to Serial Monitor, to a text file

@author: David G. Khachatrian
"""

import os
import serial
from datetime import datetime, timedelta
import re

# change according to microcontroller settings / settings in Arduino IDE
COMPORT = 'COM4'
BAUDRATE = 9600

import time

# Interfacing help: http://playground.arduino.cc/interfacing/python


def monitor_to_file(f, com_port, baud_rate):
    
    print("Connecting...")
    ser = serial.Serial(com_port, baud_rate, timeout = 0)
    print("Connected!")
    time.sleep(5) #give microcontroller time to get ready

    # SO resource: http://stackoverflow.com/questions/12210472/how-to-perform-a-function-for-a-certain-time-period-in-python    
    
    print("Starting to listen...")
    
    start = datetime.now()
    
    while (datetime.now() - start < timedelta(seconds=3)):
        line = ser.readline()
        s = str(line)[2]
#        s = re.sub(r"^b'", r'', s)
        
        if (line != ""): #we have something from microcontroller
            #copy it verbatim, cutting out b'' from the line
            f.write(str(line)[2:-1] + '\n') 
    
    print("Done!")

def main():
    time = datetime.now()
    #format the time so that it can be a filename...
    s = re.sub(r'\.\w+', r'', str(time)) #remove the last confusing part...
    
    # remembering my regex ~
    # lookbehind (?<= ...) and lookahead (?=...)
    # helpful SO page: http://stackoverflow.com/questions/6109882/regex-match-all-characters-between-two-strings
    # fun fact: look-behind requires fixed-width pattern
    
    #replace ':' with '_' so that filename is valid
    s = re.sub(r'(?<=\d)(\:)(?=\d)', r'_', s) 
    
    fname = "arduino_log {0}.log".format(s)
    with open(fname, mode = 'w+') as f:
        monitor_to_file(f, COMPORT, BAUDRATE)
    

main()
