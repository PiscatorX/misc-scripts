#!/usr/bin/env  python
from Bio import SeqIO
import csv
import argparse




def uniprot_ref(uniprot_fobj, outfile_fobj):

    seq_data  = SeqIO.parse(uniprot_fobj, "fasta")
    get_species = lambda seq_desc: ' '.join(seq_desc.strip("].").split(" ",1)[-1].split("[",1)[-1].split()[:2])
    seq_map = [ [seq.id, get_species(seq.description)] for seq  in seq_data ]
    tsv_writer = csv.writer(outfile_fobj, delimiter='\t')
    for entry in seq_map:
        tsv_writer.writerow(entry)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Generate ref file for Unipro fasta file")
    parser.add_argument('uniprot_fasta', type=argparse.FileType('r'))
    parser.add_argument('-o','--output',default="species_map.tsv", type=argparse.FileType('w'))
    args = parser.parse_args()
    
    uniprot_ref(args.uniprot_fasta, args.output)





        
    

        
