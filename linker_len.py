#!/usr/bin/env  python

from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import AlignIO
from Bio import SeqIO
import csv
import argparse
import pprint
import sys


parser = argparse.ArgumentParser(description = "convert msa file")
parser.add_argument('msa_file',help ="multiple sequence alignment (MSA) file", type=argparse.FileType('r'))
parser.add_argument('-i','--informat', default="clustal", help ="MSA format")
parser.add_argument('-s','--start', default=0, type=int)
parser.add_argument('-e','--end', required= True, type=int)
parser.add_argument('-o','--outfile', type=argparse.FileType('w'), help ="unalign output file",  required=True)
parser.add_argument('-v','--outformat', default="fasta", help ="unaligned output format")
a = parser.parse_args()

assert  a.end  >  a.start, "start must be greater than end"
a.start = a.start if a.start == 0 else a.start - 1

align = AlignIO.read(a.msa_file, a.informat)
ungapped_seq = [ SeqRecord(Seq(str(seq.seq[a.start : a.end]).translate(str.maketrans('','', '-.')), IUPAC.protein), id=seq.id, description="")  for seq in align ]
SeqIO.write(ungapped_seq, a.outfile, a.outformat)

        



