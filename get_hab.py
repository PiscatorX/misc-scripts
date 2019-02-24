import sys
from Bio import SeqIO



def  parse_data(filename):
    
    seq_data  = SeqIO.parse(open(filename), "fasta")
    new_fobj = open('sel_'+filename,'w')
    select_seq_data =  []
    for rec in seq_data:
        taxa_data = rec.description.split(';')
        if is_hab_algae(taxa_data):
            print taxa_data
            select_seq_data.append(rec)
    SeqIO.write(select_seq_data, new_fobj,'fasta')
    new_fobj.close()

    
def is_hab_algae(taxa_data):

    for algae in hab_algae:
        if algae in taxa_data:
            return True
        
    return False

    
hab_algae = open('target_habs').read().splitlines()
parse_data(sys.argv[1])
