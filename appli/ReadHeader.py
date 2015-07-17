# Filename : ReadHeader.py
# Author : kane
# Email : knguyen@ipno.in2p3.fr
# Date : 2014.08.01 14:41:10
# release : 1.0
# Python : v2.7.6
#

from os.path import *

class ReadHeader(object):
    def __init__(self, debug):
        self.DEBUG = debug
        if self.DEBUG == 1:
            print("ReadHeader.py : constructor...")

    def __del__(self):
        if self.DEBUG == 1:
            print("ReadHeader.py : destructor...")

    def getFilename(self):
        return self.__currentfile

    def setFilename(self, filename):
        self.__currentfile = filename

    def openFile(self):
        try:
            self.__inputfile = open(self.__currentfile,"r")
            if self.DEBUG == 1:
                print("ReadHeader.py : file opened successfully...")
            return True
        except OSError as e:
            if self.DEBUG == 1:
                print("ReadHeader.py : failed to open file: ", e.args[0])
            return False

    def getFileCreationDate(self):
        # Date a partir de l'octet 105
        self.__inputfile.seek(105,0)
        self.__filecreationdate = self.__inputfile.read(18)
        return self.__filecreationdate
        
    def getFilePath(self):
        # Chemin du fichier a partir de l'octet 172
        self.__inputfile.seek(172,0)
        self.__filepath = self.__inputfile.read(128)
        self.__fpath = dirname(self.__filepath)
        return self.__fpath
        
    def getFileName(self):
        # Nom du fichier
        self.filename = basename(self.__filepath)
        self.filename.strip();
        return self.filename
        
    def getFileSize(self):
        # Taille du fichier
        # A decommenter lorsque l'appli sera implementee
        # self.__filesize = getsize(self.filepath)
        # A commenter lorsque l'appli sera implementee
        self.__filesize = getsize(self.__currentfile)
        return self.__filesize
