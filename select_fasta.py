#!/usr/bin/env python

from Bio import SeqIO
import argparse
import sys

def  parse_data(filename):
    
    seq_data  = SeqIO.parse(open(filename), "fasta")
    new_fobj = open('sel_'+filename,'w')
    select_seq_data =  []
    for rec in seq_data:
        taxa_data = rec.description.split(';')
        if in_list(taxa_data):
            print taxa_data
            select_seq_data.append(rec)
    SeqIO.write(select_seq_data, new_fobj,'fasta')
    new_fobj.close()

    
def in_list(taxa_data):

    for word in select_list:
        if algae in taxa_data:
            return True
        
    return False



if __name__ == '__main__':
    parser = argparse.ArgumentParser("get sequences with id similar to provided file")
    parser.add_argument('reference', required=True, help = 'fasta reference file')
    parser.add_argument('-s','--select', help = 'list of words to look for in fasta id info', required=True )
    args = parser.parse_args()
    select_list = open(arg.select).read().splitlines()
    parse_data(args.reference)
