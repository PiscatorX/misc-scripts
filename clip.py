#!/usr/bin/env python
import argparse
import sys


class ClipText(object):
    
    def __init__(self, filename, top, bottom):
        
        self.file_obj =  open(filename)
        self.top = top
        self.bottom = bottom  
        
    def clip_text(self):

        start = False
        for line in self.file_obj:
            if self.bottom:
                    if line.startswith(self.bottom):
                        break
            if start:
                print(line,end='')
            if line.startswith(self.top):
                start = True
             

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="clip text inbetween two lines")
    parser.add_argument('infile', action='store')
    parser.add_argument('-t','--top', action='store', required=True)
    parser.add_argument('-b','--bottom', action='store', required=False)    
    args = parser.parse_args()
    clip = ClipText(args.infile, args.top, args.bottom)
    clip.clip_text()
