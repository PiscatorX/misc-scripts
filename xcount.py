#!/usr/bin/env python
from Bio import SeqIO
import argparse

def count(infile, infmt):
    
    seqx = SeqIO.parse(infile, infmt)
    print("{} sequnces found!\n".format(len(list(seqx))))

if  __name__ == '__main__':
    parser = argparse.ArgumentParser(description="show number of sequences")
    parser.add_argument('infile', type=str)
    parser.add_argument('-i','--in-format', dest='infmt', action='store', default='fasta', type=str)
    args = parser.parse_args()
    count(args.infile, args.infmt)

