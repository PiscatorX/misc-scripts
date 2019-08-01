#!/usr/bin/env  python

from Bio import AlignIO
import csv
import argparse
import pprint
import sys


def annotate_ref(msa_fobj, msa_informat, outfile_fobj, split, outformat):

    msa_data = AlignIO.read(msa_fobj, msa_informat)
    align1 = []
    align2 = []
    outfile_fobj2 =   open(outfile_fobj.name+'.2','w')
    for i,align in enumerate(msa_data,1):
        if (i <= split):
           print(">{}".format(align.id), end =" ")
           align1.append(align)
        elif (i > split):
           print(">{}".format(align.id), end =" ")
           align2.append(align)
        if (i  == split):print("\n")

    print()
    AlignIO.write(AlignIO.MultipleSeqAlignment(align1),outfile_fobj, outformat)
    AlignIO.write(AlignIO.MultipleSeqAlignment(align2),outfile_fobj2, outformat)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser("split msa into two files")
    parser.add_argument('msa_file',help ="multiple sequence alignment (MSA) file", type=argparse.FileType('r'))
    parser.add_argument('-i','--informat', default="clustal", help ="MSA output informat")
    parser.add_argument('-s','--split', type = int,  required = True)
    parser.add_argument('-o','--outfile', type=argparse.FileType('w'), help ="MSA output file",  required=True)
    parser.add_argument('-v','--outformat', default="clustal", help ="MSA output format")
    # parser.add_argument('-t','--trimm', type=argparse.FileType('r'), required = False)
    # group.add_argument('-a','--acc-ids',dest='acc_ids', action='store',nargs='+', type=str, required=False,
    #                     help='space seperated list of  accession ids')
    args = parser.parse_args()
    trimm = []
    # if args.acc_ids:
    #     trimm = args.acc_ids
    # elif args.trimm:
    #     trimm = args.trimm.read.split()
    
    annotate_ref(args.msa_file, args.informat, args.outfile, args.split, args.outformat)





        
    

        
