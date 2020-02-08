#!/usr/bin/env python
import csv
import pprint
import argparse
import collections
from Bio import SeqIO

def dedup(seq_fobj, informat, seq_out, outformat, ascending, prefix, mapping):
    
    fasta_records = SeqIO.parse(seq_fobj, informat)
    id_counts =  collections.defaultdict(int)
    seq_ref = {}
    seq_map = {}
    
    for i,seq  in enumerate(fasta_records):       
        seq_ref[i] = seq.id
        seq_map[i] = seq
        
    sorted_data  = sorted(seq_ref, key=seq_ref.get, reverse=ascending)
    ref_counter = 0
    map_writer = csv.writer(mapping, delimiter='\t')
    for ref  in sorted_data:
        seq = seq_map[ref]
        seq.description = ''
        old_seqid = seq.id
        seq.id = seq.id.split("/", 1)[0]
        id_counts[seq.id] += 1
        tmp_id =  id_counts[seq.id]
        if prefix:
            if (tmp_id != 1):
                seq.id = "_".join(map(str, [prefix, ref_counter, tmp_id]))
                map_writer.writerow([old_seqid, seq.id])
            else:
                ref_counter += 1
                seq.id = "_".join(map(str, [prefix, ref_counter]))
                map_writer.writerow([old_seqid, seq.id])
        else:
            if (tmp_id != 1):
                seq.id = "_".join(map(str, [seq.id, tmp_id]))        
                map_writer.writerow([old_seqid, seq.id])
        print(seq.id)
        SeqIO.write(seq, seq_out, outformat)
        seq_out.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""Dedupe fasta""")
    parser.add_argument('sequences', type=argparse.FileType('r') )
    parser.add_argument('-i','--informat', default="fasta")
    parser.add_argument('-o','--outfile', type=argparse.FileType('w'), default="deduped.out")
    parser.add_argument('-f','--format', default="fasta")
    parser.add_argument('-a','--ascending', action="store_true", default=False)
    parser.add_argument('-','--mapping', default="dedupe.map", type=argparse.FileType('w'))
    parser.add_argument('-p','--prefix')
    
    args, unknown = parser.parse_known_args()
    dedup(args.sequences, args.informat, args.outfile, args.format, args.ascending, args.prefix, args.mapping)
    
