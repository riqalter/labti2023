import mysql.connector

global cnx

cnx = mysql.connector.connect(user='root', password='', host='localhost', database='ap2b')

class conndb:
    def queryResult(self,strsql):
        conn = cnx.cursor()
        conn.execute(strsql)
        return conn.fetchall()

    def queryExecute(self, strsql):
        conn = cnx.cursor()
        conn.execute(strsql)
        cnx.commit()
