import re


class Curlrefs(object):

    def __init__(self, fname):

        self.fname  = fname
        
    def get_data(self):
        regex1 = re.compile("(\(\w+,* \d+\)|\(\w+ and \w+, \d+\)|\(\w+ .*;.*\d+\))")
        #(Lockshin and Williams, 1964)
        regex2 = re.compile("\(\w+ and \w+, \d+\)")
        data = open(self.fname).read()

        print re.findall(regex1, data)
        
            
                    
        
            
    


curlref = Curlrefs("CH1_LitRevPhDX.txt.bak")
#curlref = Curlrefs("test.txt")
curlref.get_data()

