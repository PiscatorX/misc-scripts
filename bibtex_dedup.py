#!/usr/bin/python
import argparse



def  bibtex_dedup():
    
    parser = argparse.ArgumentParser("Match in text citation ref to refs from Bibtex file")
    parser.add_argument('bibtex', help = 'bitex file')
    args = parser.parse_args()
    bib_fname = args.bibtex
    
    fp2  = open("_".join([bib_fname,"deduped"]),"w") 
    with open(bib_fname) as fp:
        start  = False
        ref_list  = []
        for line in  fp:
            if line.startswith('@'):
                key = line.split('{')[-1]
                if key not in ref_list:
                    print key
                    print >>fp2,line,
                    ref_list.append(key)
                    start = True
                else:
                    print key,"Exists"
            if start:
                print >>fp2,line,
                if line.startswith('}'):
                    fp2.flush()
                    start = False

                    

        
bibtex_dedup()
