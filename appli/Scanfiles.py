#!/usr/bin/python3

# Filename : scanfile.py
# Author : kane
# Email : knguyen@ipno.in2p3.fr
# Date : 2014.08.01 15:49:00
# release : 1.0
# Python : v2.7.6

import os
from datetime import *
from ConnectDB import ConnectDB
from ReadHeader import ReadHeader
from os.path import join

class ScanFiles(object):
    def __init__(self, debug):
        self.DEBUG = debug
        if self.DEBUG == 1:
            print("scanfiles.py : constructor...")
        self.__rh = ReadHeader(self.DEBUG)

    def __del__(self):
        if self.DEBUG == 1:
            print("scanfiles.py : destructor...")

    def getDatabaseName(self):
        return self.__databasename

    def setDatabaseName(self, database):
        self.__databasename = database

    def processFile(self, path):
        countFiles = 0
        numberOfDoubles = 0
        self.__connectDB = ConnectDB(self.__databasename, 0)
        # traitement des fichiers se trouvant dans le dossier
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith((".dat")):
                    # creation du chemin complet vers le fichier dat
                    fullPath = join(root,name)
                    # determination de la date de creation du fichier
                    t = os.path.getmtime(fullPath)
                    ctime = datetime.fromtimestamp(t)
                    # calcul du nombre de jours depuis la date de creation du fichier
                    time_to_today = abs(date.today() - ctime.date())
                    if self.DEBUG == 1 or self.DEBUG == 2:
                        print("Scanfiles.py : Time from file creation date to today in days = %s" % time_to_today.days)
                        self.__rh.setFilename(fullPath)
                        self.__rh.openFile()
                        filecreationdate = self.__rh.getFileCreationDate()
                        filepath         = self.__rh.getFilePath()
                        filename         = self.__rh.getFileName()
                        filesize         = self.__rh.getFileSize()
                        # Teste si le fichier existe deja dans la base de donnee
                        # Si le fichier n'existe pas, l'inserer dans la base de donnees
                        if self.__connectDB.selectDB(filecreationdate, name, root, filesize) == False:
                            self.__connectDB.insertDB(filecreationdate, name, root, filesize)
                        else:
                            numberOfDoubles = self.__connectDB.findDoubles(name)
                            print("Scanfiles.py : fichier existe deja dans la base de donnee...")
                            print("Scanfiles.py : number of files", name,"present in database = ", numberOfDoubles)

if __name__ == '__main__':
    databasename  = "scanfiles.db"
    path = './sourcedir2/'

    debug = 2;

    # instanciation des classes ScanFiles, ReadHeader et ConnectDB
    scanfiles = ScanFiles(debug)
    readHeader = ReadHeader(debug)
    connectDB = ConnectDB(databasename, debug)

    scanfiles.setDatabaseName(databasename)
    scanfiles.processFile(path)
    numberOfFiles = connectDB.countFiles()
