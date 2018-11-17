import bibtexparser
import argparse
from  difflib import SequenceMatcher


class BibRefs(object):

    def __init__(self):

        parser = argparse.ArgumentParser("Match in text citation ref to refs from Bibtex file")
        parser.add_argument('-b','--bibtex', help = 'bitex file', required=True )
        parser.add_argument('-c','--cites', help = 'citation file with citation on each line', required=True )
        parser.add_argument('-t','--tex', help = 'tex file where bib refs are to be entered')
        args = parser.parse_args()
        self.bibtex = args.bibtex
        self.cites  = args.cites
        self.tex    = args.tex
        self.replace_dict = {}
        
    def getcites(self):

        with open(self.cites) as cite_fp:
            self.cite_data =  cite_fp.read().splitlines()
                                   

    def getbib(self):
        
        with open(self.bibtex) as bibtex_file:
            bib_database = bibtexparser.bparser.BibTexParser(common_strings=True).parse_file(bibtex_file)

        for bib in bib_database.entries:
            self.bib_data = dict((bib['ID'], ' '.join([bib['author'], bib.get('year','')]))\
                                 for bib in bib_database.entries)
            #(' '.join([bib['author'], bib.get('year','')]), bib['ID']

        
    def matchdata(self):
        trans_table = ")(."
        mktrans = str.maketrans(trans_table, " "*len(trans_table))
        for cite in self.cite_data:
            trans_cite = cite.translate(mktrans).replace('et al', '')
            author, year = trans_cite.strip().split(',')[:2]
            for key, ref in self.bib_data.items():
                if year in ref and ref.startswith(author.split(' ')[0]):
                    if all( word  in ref  for word in author.split(' ')):
                        self.replace_dict[cite] = "\\cite{{{}}}".format(key)
                    

    def save_tex(self):

        save_fp  = open(''.join([self.tex,'.ref']), 'w')
        with open(self.tex) as source_tex:
            r_data =  source_tex.read()
            for k,v in self.replace_dict.items():
                print(k,v)
                r_data = r_data.replace(k, v)
        save_fp.write(r_data)
        save_fp.close()
            
                        
bibref = BibRefs()
bibref.getcites()
bibref.getbib()
bibref.matchdata()
if bibref.tex:
    bibref.save_tex()
    

