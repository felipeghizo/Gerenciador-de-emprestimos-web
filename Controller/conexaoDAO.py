import mysql.connector

class ConexaoDAO:

    def get_db_config():
        return {
            'user': "root",
            'password': "Camerasip135.",
            'host': "10.100.68.253",
            'database': "envio"
        }

    def connect_to_db():
        db_config = {
            'user': "root",
            'password': "Camerasip135.",
            'host': "10.100.68.253",
            'database': "envio"
        }
        try: 
            conn = mysql.connector.connect(**db_config)
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(err)
            return False
    