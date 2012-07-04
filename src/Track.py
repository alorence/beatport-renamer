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
        artistList = []
        for artist in self.artists :
            artistList.append(str(artist))
        stringRes.append('Artists : '+", ".join(artistList))
        stringRes.append('Title : '+self.title)
        stringRes.append('Mix name : '+self.mixName)
        stringRes.append('Length : '+self.length)
        stringRes.append('Release date : '+self.releaseDate)
        
        return "\n".join(stringRes) + "\n\n"
    
    
    
    