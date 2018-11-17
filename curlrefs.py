from collections import *
import argparse
import re


class Curlrefs(object):

    def __init__(self):

        parser = argparse.ArgumentParser("Extract refs from text file e.g  (Drewx et al., 2018)")
        parser.add_argument('textfile', help="file where refs must be extracted from")
        args = parser.parse_args()
        self.data = open(args.textfile).read()
        self.regexps = [re.compile("(\(\w+ \&{0,1}(et|and|) \w+[.,],{0,1} \d{4}\w{0,1}(;.*\)|\)))")]
        #Allows for additional regular expressions
        
        
    def get_data(self):

        for regex  in self.regexps:
            #allow
            references = re.finditer(regex, self.data)
            for ref in Counter(([ ref.group() for ref in references ])):
                print(ref)
                            
    
curlref = Curlrefs()
curlref.get_data()

