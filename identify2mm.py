#!/usr/bin/env python

import sys


class  Identify2mm(object):

    def __init__(self):

        self.INCH2MM = 25.4

        
    def get_data(self):
        
        inch2mm = lambda inch: float(inch)*self.INCH2MM
        
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                sys.exit()
            if line.startswith("Format:"):
                print(line)
            if line.startswith("Resolution"):
                print(line)
            if line.startswith("Print size"):
                x, y = map(inch2mm,  line.split(":")[-1].strip().split("x"))
                print("Print size: {:.2f} x {:.2f} mm\n".format(x, y))
                sys.exit(0)
                
                
i2mm  =  Identify2mm()
i2mm.get_data()
