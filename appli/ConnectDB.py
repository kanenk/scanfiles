# Filename : ConnectDB.py
# Author : kane
# Email : knguyen@ipno.in2p3.fr
# Date : 2014.07.31 14:32:08
# release : 1.0
# Python : v2.7.6
#

import sqlite3

class ConnectDB(object):
    def __init__(self, databasename, debug):
        self.DEBUG = debug
        self.__database = databasename
        self.__conn = sqlite3.connect(self.__database)
        if self.DEBUG == 1:
            print("ConnectDB.py : constructor...")
            print("ConnectDB.py : connected to database...")

    def __del__(self):
        if self.DEBUG == 1:
            print("ConnectDB.py : destructor...")

    def insertDB(self, filecreationdate, filename, filepath, filesize):
        # insertion d'une entree dans la base de donnees
        c = self.__conn.cursor()
        try:
            # id, __filecreationdate, filename, filepath, __filesize
            c.execute ('INSERT INTO scanfiles_files_db VALUES(?, ?, ?, ?, ?)',
                       (None, 
                        filecreationdate, 
                        filename, 
                        filepath, 
                        filesize))
            self.__conn.commit()
            c.close()
            if self.DEBUG == 1:
                print("ConnectDB.py : success in commiting database...")
            return True
        except sqlite3.Error as e:
            if self.DEBUG == 1:
                print("ConnectDB.py : error in commiting database (insert): ", e.args[0])
            c.close()
            return False

    def selectDB(self, filecreationdate, filename, filepath, filesize):
        c = self.__conn.cursor()
        try:
            c.execute('SELECT * FROM scanfiles_files_db WHERE name=? AND path=?', (filename,filepath))
            if (c.fetchall() == []):
                return False
            else:
                return True
            c.close
        except sqlite3.Error as e:
            if self.DEBUG == 1:
                print("ConnectDB.py : error in commiting database (select): ", e.args[0])
            c.close()

    def countFiles(self):
        c = self.__conn.cursor()
        try:
            c.execute('SELECT COUNT(*) FROM scanfiles_files_db;')
            numberOfFiles = c.fetchone()
            return numberOfFiles[0]
            c.close()
            if self.DEBUG == 1:
                print("scanfiles.py : number of files in database          : ", numberOfFiles)
                print("scanfiles.py : number of files in local directories : ", countFiles)

        except sqlite3.Error as e:
            if self.DEBUG == 1:
                print("ConnectDB.py : error in commiting database (count): ", e.args[0])
            c.close()

    def findDoubles(self, filename):
        c = self.__conn.cursor()
        try:
            c.execute('SELECT COUNT(*) FROM scanfiles_files_db WHERE name=?', (filename,))
            numberOfDoubles = c.fetchone()
            return numberOfDoubles[0]
            c.close()
        except sqlite3.Error as e:
            if self.DEBUG == 1:
                print("ConnectDB.py : error in commiting database (double): ", e.args[0])
            c.close()
