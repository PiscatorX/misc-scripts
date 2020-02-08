#!/usr/bin/env python

import numpy as np
import os
import csv
import glob
import sys
import pprint
import argparse
import pandas as pd
import collections
import datetime 


class GetCTD(object):
    """
    
      gets a list of files and generates on long ctd file with time

    """
    
    def __init__(self):
        
        parser = argparse.ArgumentParser("generate ODV file")
        parser.add_argument('-m', '--metavars', default="ctd.metavars", required= True, help = """config file (yaml format) with default values on each line  example:

cruise: St Helena Bay   
station: St06  
lat : -32.75323 
long : 18.10633

 """)
        parser.add_argument('-g', '--glob_pattern', default="*St6.csv", help = "file pattern with wild cards matching files to be processed")
        parser.add_argument('-o', '--csv_save', default="ctd_all.csv", help = "output file to save data")
        parser.add_argument('-t', '--time', help = "output file to save date and times ")
        parser.add_argument('-f', '--force', help = "force file overwrite", action='store_true')
        args = parser.parse_args()
        self.metavars = collections.OrderedDict([ line.strip().split('=')
                               for line in open(args.metavars).read().splitlines()
                               if any(line) ])
        self.csv_files  = glob.glob(args.glob_pattern)
        assert any(self.csv_files), "No files matching glob {} ".format(args.glob_pattern)
        self.strip_comma = lambda x: x.replace(',','')
        self.ctd_dataframes = []
        self.calibrate_flour = 'Chl-a'
        self.calibrate_flour_unit = 'mg/m3'
        self.file_units = False
        self.csv_save = args.csv_save
        if os.path.exists(self.csv_save):
            if not args.force:
                sys.stderr.write("\noutput file `{}` exists, use -f/--force to overwrite.\n\n".format(self.csv_save))
                sys.exit(1)
        self.time = args.time
        if self.time:
            self.time_fobj = open(self.time, "w")
            print("Date,time",file=self.time_fobj)
        #YEAR,MONTH,DAY,HOUR,MINUTE,SEC

        
    def get_data(self):
        
        for csv_fname  in self.csv_files:
            #print(csv_fname)
            self.parse_csv(csv_fname)    
        self.ctd_all = pd.concat(self.ctd_dataframes, ignore_index=True)
        
        self.ctd_all['Fluorescence'] = self.ctd_all['Fluorescence'].astype(float)
        self.ctd_all['Pressure'] = self.ctd_all['Pressure'].astype(float)
        n = self.ctd_all.columns.get_loc('Fluorescence') 
        self.ctd_all.insert(n+1, self.calibrate_flour, (-0.351*np.log(self.ctd_all['Pressure']) + 2.1485)*(self.ctd_all['Fluorescence']))
        j = self.col_header.index('Fluorescence')
        self.col_header.insert(j+1, self.calibrate_flour)
        self.file_units.insert(j+1, self.calibrate_flour_unit)
        
       
        
    def parse_csv(self, csv_fname):

    
        with open(csv_fname) as fp:
            ctd_file = csv.reader(fp)
            self.col_header = False
            for i,row in enumerate(ctd_file):
                if any(row):
                    if i == 0:
                        date, time = filter(any, row)
                        d, t, time_ISO8601  = self.get_time(date, time)
                        self.metavars.update({**d, **t, **time_ISO8601})
                        
                        
                    elif i == 1:
                        self.col_header = self.dedup(map(self.strip_comma, row))
                        data = dict((param,[]) for param in  self.col_header)
                         
                    elif i == 2:
                        if not self.file_units:
                            self.file_units = row
                    elif self.col_header:
                       for param, reading in zip(self.col_header, row):
                           data[param].append(reading)
                       df = pd.DataFrame(data)
                       
            for i,(col, value)  in enumerate(self.metavars.items()):
                df.insert(i, col, value)
                #print(df)
            
            self.ctd_dataframes.append(df)

       
    def get_time(self, date, time):

        
        dt_obj = datetime.datetime.strptime(date,'%d-%b-%y')
        time_str = str(datetime.timedelta(seconds=float(time)))
        time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S')

        date_time_str = ' '.join([date, time_str])
        date_time_obj = datetime.datetime.strptime(date_time_str,'%d-%b-%y %H:%M:%S')
        time_ISO8601 = {'time_ISO8601': date_time_obj.isoformat() }
        
        d = collections.OrderedDict(map(lambda v: (v, getattr(dt_obj, v)), ['year','month','day']))
        t =  collections.OrderedDict(map(lambda v: (v, getattr(time_obj, v)), ['hour','minute','second']))
        if self.time:
            print("{},{}".format(dt_obj.strftime("%d/%m/%y"),time_str,file=self.time_fobj))
        return d, t, time_ISO8601 
        
    def dedup(self, dup_list):
        
        """
           Fix duplicate headers by apppending numbers to headers

        """
        dup_counter = collections.defaultdict(int)
        deduped_list = []
        for var in dup_list:
            dup_counter[var] += 1
            count = dup_counter[var]
            if count != 1:
                deduped_list.append('.'.join(map(str, [var, count])))
                continue
            deduped_list.append(var)

        return deduped_list

    
    
    def save_ctd(self):

        
        with open(self.csv_save, 'w') as fp:
            csv_writer = csv.writer(fp)
            csv_writer.writerow(list(self.metavars.keys()) + self.col_header )
            csv_writer.writerow([ '' for _ in self.metavars.keys() ] +  self.file_units)    
        self.ctd_all.to_csv(self.csv_save, header=False, mode='a', index=False)
        if self.time:
            self.time_fobj.close()
        print(self.ctd_all)
        print("\nCTD data sucessefully saved to ", self.csv_save)
        

if __name__ == '__main__':       
    ctd = GetCTD()
    ctd.get_data()
    ctd.save_ctd()
    
