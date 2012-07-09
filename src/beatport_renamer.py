'''
Created on 3 juil. 2012

@author: Antoine Lorence
'''

import argparse
from RenameEngine import RenameEngine
from connectors.Beatport import Beatport

VERSION = 0.1

def setupCommandLine():
    # Help on arparse usage module : http://docs.python.org/library/argparse.html#module-argparse
    global parser
    
    parser = argparse.ArgumentParser(description='This program help you to rename tracks purchased from http:://www.beatport.com', version=VERSION)

    parser.add_argument('-i', '--input', action="store", dest="path", required=True,
                        help="Input file or folder to search in")
    
if __name__ == '__main__':
    setupCommandLine()
    arguments = parser.parse_args()
    bp = Beatport()
    engine = RenameEngine(arguments.path, bp)
    engine.renameFiles()