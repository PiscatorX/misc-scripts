#!/usr/bin/env python
import pandas as pd
import argparse
import sys
import os


def group_medium(fname, group, check_headers, sep, *variables):

    data_df = pd.read_csv(fname, sep = sep)
    
    if check_headers:
        print("Columns:\t{}".format(data_df.columns))
        sys.exit(0)
        
    for var in variables:
        new_var = '_'.join(['median', var])
        data_df.loc[:,new_var] = pd.NA
        data_df[new_var] = data_df.groupby(group)[var].transform('median')
        
    outfname = os.path.basename(fname.name)
    #print(outfname)
    data_df.to_csv('modified_' + outfname, sep = "\t")
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser("Annotate an msa file using a map file")
    parser.add_argument('data_fname', type=argparse.FileType('r'))
    parser.add_argument('-g','--group', help = "grouping column", default = "shapeid", required=False)
    parser.add_argument('-s','--sep',  default=',')
    parser.add_argument('-c','--check_headers', action='store_true')
    parser.add_argument('-v','--variables', nargs='+', help = "variable columns", required=False, default = ['x','y'])
    args = parser.parse_args()
    group_medium(args.data_fname, args.group, args.check_headers,  args.sep, *args.variables)

