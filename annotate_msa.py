#!/usr/bin/env  python

from Bio import AlignIO
import csv
import argparse
import pprint
import sys


def annotate_ref(msa_fobj, map_fobj,  msa_informat, outfile_fobj, msa_outformat):

    map_data = dict([ line.split("\t") for line in map_fobj.read().splitlines() if line ])
    msa_data = AlignIO.read(msa_fobj, msa_informat)
    annotated_align = []
    for align in msa_data:
        seq_id = align.id
        try:
            genus, species = map_data[align.id].split(" ",1)
            #annotation = ''.join([genus[0]+'.',species,"[{}]".format(seq_id)])
            #annotation = "{}[{}]".format(map_data[align.id],seq_id)
            annotation = "{} {}".format(genus, species)
            align.id = annotation
        except KeyError:
            pass
        annotated_align.append(align)
    
    AlignIO.write(AlignIO.MultipleSeqAlignment(annotated_align),
                  outfile_fobj,
                  msa_outformat)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Annotate an msa file using a map file")
    parser.add_argument('msa_file',help ="multiple sequence alignment (MSA) file", type=argparse.FileType('r'))
    parser.add_argument('-m','--map', type=argparse.FileType('r'), required = True)
    parser.add_argument('-i','--informat', default="clustal", help ="MSA format")
    parser.add_argument('-o','--outfile', type=argparse.FileType('w'), help ="MSA output file",  required=True)
    parser.add_argument('-v','--outformat', default="clustal", help ="MSA output format")
    args = parser.parse_args()
    annotate_ref(args.msa_file, args.map, args.informat, args.outfile, args.outformat)





        
    

        
