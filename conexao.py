import mysql.connector

class Conexao:

    def __init__(self):
        self.__conn = mysql.connector.connect(host = 'trolley.proxy.rlwy.net', user = 'root', password = 'esrBSowUtfVNujmqvrMTQtNdzlWPgHAa', database = 'railway', port = 34179)


    def get_conexao(self):
        return self.__conn
    

    def get_cursor(self):
        return  self.__conn.cursor()
    
    def fechar_conexao(self):
        self.__conn.close()
        self.__conn.cursor().close()
