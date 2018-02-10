#! /usr/bin/env Rscript

require(argparse)
cwd = getwd()
parser <- ArgumentParser()
parser <- ArgumentParser(description="Process sanger ab1 reads and generate fasta files")
parser$add_argument("biom", help="input folder where abi files are located.")
parser$add_argument("-o","--output-folder", dest="outDir", default=cwd,
                    help="directory to write output files")

library(phyloseq)
library(ggplot2)
library(gridExtra)
library(dunn.test)
source("/home/drewx/Documents/Paribus/microbiome_custom_functions.R")

biom <- args$biom
inDir  <- args$inDir

phy <- import_biom(BIOMfilename = biom, verbose = TRUE)
ntaxa(phy)#(number of OTUs)

