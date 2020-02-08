#!/usr/bin/env  python

from Bio import SeqIO
import csv
import argparse
import pprint
import sys


def annotate_ref(seq_fobj, map_fobj,  informat, outfile_fobj, outformat):

    map_data = dict([ line.split("\t") for line in map_fobj.read().splitlines() if line ])
    seq_fobj = SeqIO.parse(seq_fobj, informat)
    annotated_seq = []
    for seq in seq_fobj:
        seq_id = seq.id
        seq.description = ''
        try:
            #genus, species = map_data[seq.id].split(" ",1)
            tag = map_data[seq.id].split(" ",1)
            #print(tag)
            #annotation = ''.join([genus[0]+'.',species,"[{}]".format(seq_id)])
            #annotation = "{}[{}]".format(map_data[align.id],seq_id)
            #annotation = "{}_{}".format(genus, species)
            #seq.id = annotation
            seq.id = ''.join(tag)
            print(seq.id)
        except KeyError:
            pass
        annotated_seq.append(seq)
    
    SeqIO.write(annotated_seq,
                  outfile_fobj,
                    outformat)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser("Generate ref file for Unipro fasta file")
    parser.add_argument('seq_file',help ="sequence file", type=argparse.FileType('r'))
    parser.add_argument('-m','--map', type=argparse.FileType('r'), required = True)
    parser.add_argument('-i','--informat', default="fasta")
    parser.add_argument('-o','--outfile', type=argparse.FileType('w'),  required=True)
    parser.add_argument('-v','--outformat', default="fasta")
    args = parser.parse_args()
    annotate_ref(args.seq_file, args.map, args.informat, args.outfile, args.outformat)





        
    

        
