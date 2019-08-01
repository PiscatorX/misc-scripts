#!/usr/bin/env python
import argparse
import pprint

parser = argparse.ArgumentParser(description = "find words in file1 and not in file2")
parser.add_argument('file1', type=argparse.FileType('r'))
parser.add_argument('file2', type=argparse.FileType('r'))
parser.add_argument('-o','--out', type=argparse.FileType('w'),  required = True)
args = parser.parse_args()

file1 = set([  record for record in args.file1.read().split()  if not record.startswith("sample") ])
file2 = set([  record for record in args.file2.read().split()  if not record.startswith("sample") ])
difference = file1 - file2
pprint.pprint(difference)

with open("PEP_missing","w") as fp:
    fp.writelines([ record+"\n" for record in difference])
