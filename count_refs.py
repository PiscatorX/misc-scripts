#!/usr/bin/python

from collections import Counter
import datetime
import  sys



def countyears(years):
    
    year = datetime.date.today().year
    
    counts = Counter(map(lambda x: int(x.strip()), years.splitlines()))
    total = sum(counts.values()) 
    
    year10 = sum([ counts[year] for year in range(year,year-10,-1)])
    year5 = sum([ counts[year] for year in range(year,year-5,-1)])
    
    
    print "Total references :",total
    print "\nYear\tCount\tPercent"
    for year in sorted(counts.keys()):
        count   =  counts[year]
        percent = float(count)/total
        
        print "{}\t{}\t{:.1%}".format(year, count, percent)
    print year5
    print year10
    print "Total references in last 5 years: {0}({1:.2%}) ".format(year5,float(year5)/total)
    print "Total references in last 10 years: {0}({1:.2%})".format(year10,float(year10)/total)
    

if __name__ ==  '__main__':
    years = sys.stdin.read()
    countyears(years)



