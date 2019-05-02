#!/usr/bin/env python
import itertools
import argparse
import glob
import csv
import sys
import os


def gen_manifest(read_dir, manifest, pattern):
    leading, trailing  = pattern.split('{', 1)
    read_chars, trailing  = trailing.split('}')
    pattern = ''.join([read_dir,leading,'[',read_chars, ']',trailing ])
    direction = itertools.cycle(['forward','reverse'])
    manifest_writer = csv.writer(manifest)
    manifest_writer.writerow(['sample-id', 'absolute-filepath', 'direction'])
    for read_file in glob.iglob(pattern):
        base_fname = os.path.basename(read_file)
        sample_name = base_fname 
        for char in read_chars.split(','):
           pattern_string = ''.join([leading.replace('*',''), char, trailing.replace('*','')])
           if base_fname.endswith(pattern_string):
               sample_name = base_fname.replace(pattern_string,'',1)
        manifest_writer.writerow([sample_name, os.path.abspath(read_file), next(direction)])
    manifest.close()

if __name__ == '__main__':
     parser = argparse.ArgumentParser("generate manifest file")
     parser.add_argument('read_dir')
     parser.add_argument('-m', '--manifest', required = True, help = "manifest file", type=argparse.FileType('w'))
     parser.add_argument('-p','--pattern', help="wildcard read paring pattern with braces e.g `*_{1,2}.fq.gz` ", default="*_{1,2}.fq.gz")
     args = parser.parse_args()
     if (not '{' in args.pattern) or (not '}' in args.pattern):
         print("\n\nIncorrect read pairing pattern provided", file=sys.stderr)
         parser.print_help(sys.stderr)
     for char in "?[":
         if char in args.pattern:
             print("\n\nInvaling read pairing char founnd `{}` ".format(char), file=sys.stderr)
             parser.print_help(sys.stderr)
 
     gen_manifest(args.read_dir, args.manifest,  args.pattern)
     
