#!/usr/bin/env python

from Bio  import SeqIO
import sys


fname = sys.argv[1]
print(fname)
records = SeqIO.parse(fname, "fasta")
new_records =  []



data = [ line.split(" ",1) for line in open("MMETSP.id").read().splitlines() ]

for x in range(10):
    data.extend(data)

for i,seq  in enumerate(records,1):
    seq_id, desc = data.pop()    
    seq.id = seq_id
    seq.description = desc
    new_records.append(seq)

    
SeqIO.write(new_records, open("new_file","w"), "fasta")



