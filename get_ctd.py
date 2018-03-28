#!/usr/bin/env python
import  csv
import  glob
import  sys
import  pprint 



class GetCTD(object):

    def __init__(self):
        
        self.csv_files  = glob.glob('*.csv')
        self.ctd_data = {}
        self.strip_comma = lambda x: x.replace(',','')

    def get_data(self):

        for csv_fname  in self.csv_files:    
            self.parse_csv(csv_fname)
        pprint.pprint(self.ctd_data)
        
    def parse_csv(self, csv_fname):
        
        with open(csv_fname) as fp:
            ctd_file = csv.reader(fp)
            header = False
            xdata = {}
            for i,row in enumerate(ctd_file):
                if any(row) and (i != 0) and (i != 2):
                    if i == 1:
                       header = map(self.strip_comma, row)
                       data = dict((param,[]) for param in  header)
                       continue
                    if header:
                       for param, reading in zip(header, row):
                           data[param].append(reading)
                           
            self.ctd_data[csv_fname] = data
                    
            
        
    

            
ctd = GetCTD()
ctd.get_data()
