'''
Created on 5 juil. 2012

@author: Antoine Lorence
'''

import os
import re

DEFAULT_PATERN = "%artist% - %title%"

class RenameEngine(object):

    def __init__(self, inputFileOrFolder, connector, recursive=False, pattern=None):
        '''
        Constructor
        '''
        self.input = inputFileOrFolder
        self.connector = connector
        self.recursive = recursive
        if self.recursive :
            self.fileList = self.getAllFiles()
        else :
            eltList = os.listdir(self.input)
            self.fileList = []
            for elt in eltList:
                elt = self.input + os.path.sep + elt
                if os.path.isfile(elt):
                    self.fileList.append(elt)
        if None == pattern:
            self.pattern = DEFAULT_PATERN
        else:
            self.pattern = pattern
    
    def getAllFiles(self):
        fileList = []
        for root, _, files in os.walk(self.input) :
            for f in files:
                fileList.append(os.path.join(root, f))
        return fileList
        
    def renameFiles(self):
        renameList = []
        idList = []
        for _file in self.fileList:
            try:
                infos = self.getIdFromFile(_file)
                if infos['id'] != "":
                    idList.append(infos['id'])
                    renameList.append(infos)
            except:
                pass
        
        if len(idList) > 0:
            print "Search informations to rename %i file(s)" % (len(idList), )
        else:
            print "No file to rename"
            pass
        
        tracksList = self.connector.getTracksFromIds(idList)
        
        for rename in renameList:
            
            oldFile = rename['dir'] + os.path.sep + rename['file']
            
            if tracksList.has_key(rename['id']):
                
                trackObj = tracksList[rename['id']]
                suffix = getSuffix(rename['file'])
                
                newFile = rename['dir'] + os.path.sep + trackObj.getArtists() + ' - ' + trackObj.title + '.' + suffix
                
                try :
                    os.rename(oldFile, newFile)
                    print "%s renamed into %s" % (oldFile, newFile)
                except Exception, e :
                    print "Unable to rename track %s in %s : " % (oldFile, newFile)
                    print e

            else:
                print "Unable to find informations for track %s" % (oldFile, )
            
        
    
    def getIdFromFile(self, filePath):
        info = {}
        separatorPos = filePath.rfind(os.path.sep)
        d = filePath[0:separatorPos]
        f = filePath[separatorPos + 1:]
        idT = re.match(r"([0-9]+).*\.(wav|flac|mp3|aiff|aif)", f).group(1)
        info['id'] = idT
        info['dir'] = d
        info['file'] = f
        return info
    
def getSuffix(fileName):
    return fileName[fileName.rfind(".")+1:]