#!/usr/bin/env python
from Bio.Align import MultipleSeqAlignment
from Bio.SeqRecord import SeqRecord
#from Bio.Alphabet import generic_dna
from Bio import AlignIO
from Bio.Seq import Seq
import argparse
import sys

import os

__author__ = "Andrew Ndhlovu"
__copyright__ = "Copyright 2020"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Andrew Ndhlovu"
__email__ = "drewxdvst@outlook.com"


def rm_dot(args):

    if not args.outfile:
         outfile = ''.join([args.infile.name.replace(args.infmt, ''), args.ofmt])

    msa  = AlignIO.read(args.infile, args.infmt)
    dd_msa =  []
    for i,alignment in enumerate(msa,1):
        seq = SeqRecord(Seq(str(alignment.seq).replace("-","")), id=alignment.id,  description="") 
        dd_msa.append(seq)
        
    AlignIO.write(MultipleSeqAlignment(dd_msa), open(args.outfile,'w'), args.ofmt)

    
if  __name__ == '__main__':
    parser = argparse.ArgumentParser(description="simple Biopython format convertor rm alingment")
    parser.add_argument('infile', action='store',  type=argparse.FileType('r'))
    parser.add_argument('-i','--in-format', dest='infmt', action='store', default='clustal', type=str)
    parser.add_argument('-f','--out-format', dest='ofmt', action='store', default='clustal', required=False, type=str)    
    parser.add_argument('-o','--outfile', dest='outfile', action='store', type=str, required = True)
    args = parser.parse_args()
    rm_dot(args)
