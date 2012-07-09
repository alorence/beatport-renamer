'''
Created on 4 juil. 2012

@author: Antoine Lorence
'''

from models.Track import Track
from connectors.ApiConnector import ApiConnector

BEATPORT_API = "api.beatport.com"

class Beatport(ApiConnector):

    def __init__(self):
        ApiConnector.__init__(self, BEATPORT_API)
    
    '''
    Return a list of dict with 'id' and 'obj' attibutes
    '''
    def getTracksFromIds(self, idList):
        strIdList = ','.join(idList)
        params = {"ids":strIdList}
        results = self.query("/catalog/3/tracks", params)
        
        tracksResult = {}
        for trackJsonContent in results["results"] :
            trackObject = Track(trackJsonContent)
            tracksResult[str(trackObject.getId())] = trackObject
        return tracksResult
        
    
    def getTrackFromInfos(self, artist, track, release):
        pass