'''
Created on 4 juil. 2012

@author: Toine
'''
from Artist import Artist

class Track(object):
    '''
    classdocs
    '''


    def __init__(self, contentDict):
        '''
        Constructor
        '''
        self.idTrack = contentDict["id"]
        self.title = contentDict["title"]
        self.artists = []
        for artistDict in contentDict["artists"] :
            self.artists.append(Artist(artistDict))
        self.releaseDate = contentDict["releaseDate"]
        self.bpPublishDate = contentDict["publishDate"]
        self.mixName = contentDict["mixName"]
        self.length = contentDict["length"]
        # TODO :
        # self.release = contentDict["release"]
        # self.label = contentDict["label"]
        
        
    def __repr__(self):
        stringRes = []
        stringRes.append('*** Track '+str(self.idTrack))
        stringRes.append('Title : '+self.title)
        artistList = []
        for artist in self.artists :
            artistList.append(str(artist))
        stringRes.append('Artists : '+", ".join(artistList))
        
        return "\n".join(stringRes) + "\n\n"
    
    
    
    