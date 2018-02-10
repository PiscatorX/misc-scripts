#! /usr/bin/env python
import seaborn as  sns
import pandas as pd
import argparse



class PlotDiversity(object):

    def __init__(self):
        parser  = argparse.ArgumentParser()
        parser.add_argument('data_file')
        args = parser.parse_args()
        self.data_file = args.data_file
        self.x_vars =  [""]
        self.y_vars =  [""]
        
                                
    def plot(self):

        data = pd.readtable(self.data_file)
        
    




if __name__ == '__main__':
    plot = PlotDiversity()
    plot.plot()
