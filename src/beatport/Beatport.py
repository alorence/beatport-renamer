'''
Created on 4 juil. 2012

@author: Antoine Lorence
'''
from network.ApiConnection import ApiConnection
from Track import Track

BEATPORT_API = "api.beatport.com"

class Beatport(object):
    '''
    classdocs
    '''

    

    '''
    Constructor
    '''
    def __init__(self):
        self.api = ApiConnection(BEATPORT_API)
    
    def getTrackFromId(self, trackId):
        params = {"id":trackId}
        results = self.api.query("/catalog/3/tracks", params)
        
        nbResults = len(results["results"])
        print "Serach for tracks with id " + trackId + " : " + str(nbResults) + " results"
        
        tracksResult = []
        for trackJsonContent in results["results"] :
            tracksResult.append(Track(trackJsonContent))
        return tracksResult
        
    
    def getTrackFromInfos(self, artist, track, release):
        pass