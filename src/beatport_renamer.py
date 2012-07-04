'''
Created on 3 juil. 2012

@author: Antoine Lorence
'''
from beatport.Beatport import Beatport

if __name__ == '__main__':
    bp = Beatport()
    result = bp.getTrackFromId("1574171")
    for t in result :
        print t.__repr__()