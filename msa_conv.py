#!/usr/bin/env  python

from Bio import AlignIO
import csv
import argparse
import pprint
import sys


parser = argparse.ArgumentParser(description = "convert msa file")
parser.add_argument('msa_file',help ="multiple sequence alignment (MSA) file", type=argparse.FileType('r'))
parser.add_argument('-i','--informat', default="clustal", help ="MSA format")
parser.add_argument('-o','--outfile', type=argparse.FileType('w'), help ="MSA output file",  required=True)
parser.add_argument('-v','--outformat', default="clustal", help ="MSA output format")
args = parser.parse_args()

AlignIO.convert(args.msa, args.informat, args.outfile, args.outformat)







        
    

        
