#!/usr/bin/env python
from Bio import SeqIO
import argparse
import glob
import os

def fname2seqid(glob_path, informat, outfile):

    filenames =  glob.glob(os.path.join(glob_path))

    
    sequence_list = []
    for seq_path in filenames:
        fname = os.path.basename(seq_path)
        seqrecord =  SeqIO.read(seq_path, informat)
        print("{}\t{}".format(fname, seqrecord.id))
        seqrecord.id = fname
        sequence_list.append(seqrecord)

    with open(outfile, 'w') as fp:
        SeqIO.write(sequence_list, fp, informat)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("")
    parser.add_argument('glob_path', help ="glob path for files with wildcards")
    parser.add_argument('-i','--informat', default="fasta")
    parser.add_argument('-o','--outfile', default="merged.seqs")
    args = parser.parse_args()
    fname2seqid(args.glob_path, args.informat, args.outfile)
