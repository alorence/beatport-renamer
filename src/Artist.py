'''
Created on 4 juil. 2012

@author: Antoine Lorence
'''

class Artist(object):
    '''
    classdocs
    '''


    def __init__(self, contentDict):
        '''
        Constructor
        '''
        self.id = contentDict["id"]
        self.name = contentDict["name"]
    
    def __repr__(self):
        return self.name