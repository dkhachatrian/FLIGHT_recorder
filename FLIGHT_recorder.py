# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 17:21:52 2017

Quick'n'Dirty way to write Arduino readings, originally sent 
to Serial Monitor, to a text file

@author: David G. Khachatrian
"""

import os
import serial
import datetime

# change according to microcontroller settings / settings in Arduino IDE
COMPORT = 4
BAUDRATE = 115200



def monitor_to_file(f, com_port, baud_rate):
    
    ser = serial.Serial(com_port, baud_rate, timeout = 0)
    
    while(True):
        line = ser.readline()
        if (line != ""): #we have something from microcontroller
            f.write(line) #copy it verbatim
    


def main():
    time = datetime.datetime.now();
    fname = "arduino_log {0}.log".format(time)
    with open(fname, mode = 'w+') as f:
        monitor_to_file(f, COMPORT, BAUDRATE)
    

main()
