#!/usr/bin/env  python

from Bio import AlignIO
import csv
import argparse
import pprint
import sys


def annotate_ref(msa_fobj, msa_informat, outfile_fobj, start, end, outformat):

    assert end >  start, "sequence end must greater than start"
    msa_data = AlignIO.read(msa_fobj, msa_informat)
    align1 = []
    for align in msa_data:
        align1.append(align[start:end])
    AlignIO.write(AlignIO.MultipleSeqAlignment(align1),outfile_fobj, outformat)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser("split msa into two files")
    parser.add_argument('msa_file',help ="multiple sequence alignment (MSA) file", type=argparse.FileType('r'))
    parser.add_argument('-i','--informat', default="clustal", help ="MSA output informat")
    parser.add_argument('-s','--start', type = int, default = 0,  required = False)
    parser.add_argument('-e','--end', type = int,  required = True)
    parser.add_argument('-o','--outfile', type=argparse.FileType('w'), help ="MSA output file",  required=True)
    parser.add_argument('-v','--outformat', default="clustal", help ="MSA output format")
    args = parser.parse_args()
    annotate_ref(args.msa_file, args.informat, args.outfile, args.start, args.end, args.outformat)





        
    

        
