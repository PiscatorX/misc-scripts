#! /usr/bin/env python
import argparse
import csv




class Summary2Krona(object):

    def  __init__(self):

        parser = argparse.ArgumentParser("Save Qiime summary taxa(*.txt) file to Krona text for import")
        parser.add_argument('qiime_summary')
        parser.add_argument('-p','--prefix', default="D_L__",help = "prefix 'L' for digits (default 0-9)")
        args = parser.parse_args()
        self.summary = args.qiime_summary
        self.prefix = args.prefix.replace('L','{}')
        self.summary_data = open(self.summary).read()
        self.krona_file = '_'.join(['krona', self.summary_data])

        
    def parse2krona(self):
        
        for digit in range(0,11):
            self.summary_data = self.summary_data.replace(self.prefix.format(digit),'')
            
        self.summary_data =[ row for row in self.summary_data.replace(';','\t').splitlines()\
                             if not row[0].startswith('#') ]

        with open(self.krona_file, 'w') as fp:
            for row in csv.reader(self.summary_data, dialect='excel-tab'):
                line = [row[-1]]+row[:-2]
                fp.writeline(line)
            
        
if __name__ == '__main__':
    summary = Summary2Krona()
    summary.parse2krona()
