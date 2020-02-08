import sys
import csv
import glob
import itertools
import collections
import numpy as np

def get_data(glob_search, col, out_fname):
    
    station_data = {}
    ocean_data = ''
    
    for file_name in  glob.iglob(glob_search):
         st_name, mean = process_data(file_name, station_data, col)
         ocean_data = ''.join([ocean_data, st_name ,'\t',str(mean), '\n'])
         print '\rStation %s Mean=> %s '%(st_name, mean)

    print '\t**DATA**'
    print ocean_data
    with open(out_fname,'w') as fp:
       fp.write(ocean_data)
       
    print '\nData writen to %s'%out_fname     

def process_data(file_name, station_data, col, colx='DEPTH'):
    
    st_name = file_name.rsplit('_')[-1].split('.')[0]
    station_data[st_name]= collections.OrderedDict()
    init  = False
    parse_header =  lambda header: dict((j,i) for i,j in  enumerate(header))
    with open(file_name) as fp:
        csv_reader = csv.reader(fp)
        print'\n{}\n'.format(file_name)
        for row in csv_reader:
            if not init:
                header = parse_header(csv_reader.next())
                csv_reader.next()
                init = True
                continue
            station_data[st_name][float(row[header[colx]])] = row[header[col]]
            
    f_name = '_'.join(['station', st_name])+'.dat'
    data = []
    for line in [ [x, float(y)] for x,y in  station_data[st_name].items()  if x <= 1 ]:
        data.append(line[1])
        print line
    print data
    mean = np.mean(np.array(data))

    return st_name, mean

col, out_fname = sys.argv[1:]
files =  get_data("St Hel Bay 11Feb15*csv", col, out_fname)

