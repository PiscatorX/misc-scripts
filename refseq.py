#!/usr/bin/env python



class me(object):

    def __ini__(self):
        pass
       #self.description = "tRNA-(ms[2]io[6]A)-hydroxylase [Marinomonas mediterranea]"

    
seq  = me()
#seq.description = "tRNA-(ms[2]io[6]A)-hydroxylase [Marinomonas mediterranea]"
seq.description = "3-oxoacyl-[acyl-carrier protein] reductase [Thalassiosira pseudonana CCMP1335]"
print(seq.description)


#desc, organism  =  seq.description.rsplit("[", 2)
#desc, organism  =  seq.description.split(" ",1)[-1].split("[", 1)
print(seq.description.rsplit("[", 1))
# except ValueError:
# desc  =  seq.description.split(" ",1)[-1]
# organism =  ''

