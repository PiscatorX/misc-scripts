#!/bin/bash

hmmalign \
    --informat fasta \
    /opt/DB_REF/Pfam/Peptidase_C14.hmm \
    $1  > C14_hmmalign.sto  &&  esl-reformat\
    --informat stockholm \
    -o C14_hmmalign.aln \
    clustal \
    C14_hmmalign.sto


hmmalign \
    --informat fasta \
    --trim \
    /opt/DB_REF/Pfam/Peptidase_C14.hmm \
    $1  > C14_hmmalign_trim.sto  &&  esl-reformat\
    --informat stockholm \
    -o C14_hmmalign_trim.aln \
    clustal \
    C14_hmmalign_trim.sto


esl-alimask \
    -p \
    --ppcons 0.7 \
    C14_hmmalign_trim.sto  >  C14_hmmalign_trim_7pp.sto &&   esl-reformat \
							      fasta C14_hmmalign_trim_7pp.sto   -o fasta C14_hmmalign_trim_7pp.fasta  

