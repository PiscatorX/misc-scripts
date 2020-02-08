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
parser.add_argument('-l','--list', type=argparse.FileType('r'),  required = True)
args = parser.parse_args()

sel_seqs = args.list.read().split()
msa_data = AlignIO.read(args.msa_file, args.informat)

sel_align = []
found_align = []
for align in msa_data:
    if align.id in sel_seqs:
        sel_align.append(align)
        found_align.append(align.id)

AlignIO.write(AlignIO.MultipleSeqAlignment(sel_align), args.outfile, args.outformat)
[ sys.write("Not found:\t{}".format(align.id)) for seq_id in found_align if seq_id not in found_align  ]     
    

    






        
    

        
