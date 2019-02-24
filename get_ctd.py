#!/usr/bin/env python
import  csv
import  glob
import  sys
import  pprint
import  argparse
import  pandas as pd
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
        args = parser.parse_args()
        self.metavars = collections.OrderedDict([ line.strip().split('=')
                               for line in open(args.metavars).read().splitlines()
                               if any(line) ])
        self.csv_files  = glob.glob(args.glob_pattern)
        assert any(self.csv_files), "No files matching glob {} ".format(args.glob_pattern)
        self.strip_comma = lambda x: x.replace(',','')
        self.ctd_dataframes = []
        self.file_header = False
        self.file_units = False
        self.csv_save = args.csv_save
        self.time = args.time
        print args
        if self.time:
            self.time_fobj = open(self.time, "w")
            print >> self.time_fobj,"Date,time"
        #YEAR,MONTH,DAY,HOUR,MINUTE,SEC

        
    def get_data(self):
        
        for csv_fname  in self.csv_files:
            print csv_fname
            self.parse_csv(csv_fname)    
        self.ctd_all = pd.concat(self.ctd_dataframes)
        
            
        
    def parse_csv(self, csv_fname):
        
        with open(csv_fname) as fp:
            ctd_file = csv.reader(fp)
            col_header = False
            for i,row in enumerate(ctd_file):
                if any(row):
                    if i == 0:
                        date, time = filter(any, row)
                        d, t  = self.get_time(date, time)
                        map(self.metavars.update, [d, t])
                        
                    elif i == 1:
                        col_header = self.dedup(map(self.strip_comma, row))
                        data = dict((param,[]) for param in  col_header)
                        if not self.file_header:
                            self.file_header = self.metavars.keys() + col_header
                            
                            
                    elif i == 2:
                        if not self.file_units:
                            self.file_units = row
                    elif col_header:
                       for param, reading in zip(col_header, row):
                           data[param].append(reading)
            df = pd.DataFrame(data)
            for idx, (col, value)  in enumerate(self.metavars.items()):
                df.insert(idx, col, value)
            self.ctd_dataframes.append(df)

       
    def get_time(self, date, time):

        dt_obj = datetime.datetime.strptime(date,'%d-%b-%y')
        time_str = str(datetime.timedelta(seconds=float(time)))
        time_obj = datetime.datetime.strptime(time_str, '%H:%M:%S')
        
        d = collections.OrderedDict(map(lambda v: (v, getattr(dt_obj, v)), ['year','month','day']))
        t =  collections.OrderedDict(map(lambda v: (v, getattr(time_obj, v)), ['hour','minute','second']))
        print >> self.time_fobj,"{},{}".format(dt_obj.strftime("%d/%m/%y"),time_str)
        return d, t
        
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
            csv_writer.writerow(self.file_header)
            #csv_writer.writerow([ '' for _ in self.metavars.keys() ] +  self.file_units)    
        self.ctd_all.to_csv(self.csv_save, header=False, mode='a')
        if self.time:
            self.time_fobj.close() 
        print "\nCTD data sucessefully saved to ", self.csv_save
        

        
ctd = GetCTD()
ctd.get_data()
ctd.save_ctd()
