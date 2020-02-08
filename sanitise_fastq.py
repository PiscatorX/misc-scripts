#!/usr/bin/env python

from Bio import SeqIO
import argparse



def fastq_gen(fastq_handle):
    
    for i,line in enumerate(fastq_handle,1):
        try:
        #assert line[0] == '@', "FastQ line does must start with `@`" 
            if line[0] == '@':
                defline=line[1:]
                seq_data = next(fastq_handle).rstrip()
                seq_defline = next(fastq_handle).rstrip()
                if seq_defline.startswith('+'):
                    if seq_defline[1:]:
                        assert seq_defline[1:] == defline,"sequence defline and quality deflines differ"
                seq_qual = next(fastq_handle).rstrip()
        except StopIteration:
            pass
    
            
    
    

    


if __name__ == '__main__':
    parser = argparse.ArgumentParser("read and write fastq properly")
    parser.add_argument('fastq', help = 'fastaq file', type=argparse.FileType('r'))
    args = parser.parse_args()
    fastq_gen(args.fastq)
