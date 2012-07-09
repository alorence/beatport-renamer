'''
Created on 4 juil. 2012

@author: Toine
'''

class Track(object):


    def __init__(self, contentDict):

        self.idTrack = contentDict["id"]
        self.title = contentDict["title"]
        self.artists = []
        for artist in contentDict["artists"] :
            self.artists.append(artist['name'])
        self.releaseDate = contentDict["releaseDate"]
        self.bpPublishDate = contentDict["publishDate"]
        self.mixName = contentDict["mixName"]
        self.length = contentDict["length"]
        # TODO :
        # self.release = contentDict["release"]
        # self.label = contentDict["label"]
    
    def getArtists(self):
        return ", ".join(self.artists)
        
    def getId(self):
        return str(self.idTrack)
        
    def __repr__(self):
        stringRes = []
        stringRes.append('*** Track ' + str(self.idTrack))
        stringRes.append('Artists : ' + self.getArtists())
        stringRes.append('Title : '+self.title)
        stringRes.append('Mix name : '+self.mixName)
        stringRes.append('Length : '+self.length)
        stringRes.append('Release date : '+self.releaseDate)
        
        return "\n".join(stringRes) + "\n\n"
    
    
    
    