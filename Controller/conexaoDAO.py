import mysql.connector

class ConexaoDAO:

    def get_db_config(self):
        return {
            'user': "root",
            'password': "Camerasip135.",
            'host': "10.100.68.253",
            'database': "envio"
        }

    def connect_to_db(self):
        db_config = self.get_db_config()
        try: 
            conn = mysql.connector.connect(**db_config)
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(err)
            return False
    