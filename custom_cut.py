#!/usr/bin/env  python
import csv
import argparse
import pprint
import sys



def cut(fileinput, delim, field, out_delimiter):
    
    csv_reader = csv.reader(fileinput, delimiter = delim)
    for row in csv_reader:
        row = out_delimiter.join([row[i] for i in field])
        print(row)
        
            
if __name__ == '__main__':
      parser = argparse.ArgumentParser("custome cut")
      parser.add_argument('fileinput',help ="File to be cut.",  nargs='*', type=argparse.FileType('r'))
      parser.add_argument('-d','--delimiter', default="\t", type = str, help ="Delimit input/file on.")
      parser.add_argument('-f','--field', nargs='+', type = int, required = True, help = "Zero indexed. Space separated field/columns to print out.")
      parser.add_argument('-o','--out_delimiter', default="\t", type = str, help = "Delimit output on.")
      args = parser.parse_args()
      if args.fileinput:
          #TO DO
          #ignore other files 
          fileinput = args.fileinput[0]
          cut(fileinput, args.delimiter, args.field, args.out_delimiter)
      else:
          fileinput = sys.stdin
      cut(fileinput, args.delimiter, args.field, args.out_delimiter)
