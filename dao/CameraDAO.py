import sqlite3
import mysql.connector

class CameraDAO:
    def __init__(self, modelo="", mac=""):
        self.modelo = modelo
        self.mac = mac
        self.connection = self.conectar()

    def conectar(self):
        banco = "envio.db"  # Ajuste o caminho do banco de dados conforme necessário
        try:
            connection = sqlite3.connect(banco)
            return connection
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
        
    # Obtém o ID da câmera
    def get_camera_id(self, modelo_editar, mac_editar):
        sql = "SELECT COUNT(*) AS total FROM cameras WHERE modelo = ? AND MAC = ?"
        camera_id = 0
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (modelo_editar, mac_editar))
            total_ferramentas = cursor.fetchone()[0]

            if total_ferramentas > 0:
                sql = "SELECT cameraid FROM cameras WHERE modelo = ? AND MAC = ?"
                cursor.execute(sql, (modelo_editar, mac_editar))
                camera_id = cursor.fetchone()[0]
            else:
                return -1
        except sqlite3.Error as e:
            print(f"Erro ao procurar câmera: {e}")
        
        return camera_id

    # Obtém o modelo da câmera pelo ID
    def get_modelo_dao(self, camera_id):
        db_config = {
            'user': 'root',
            'password': "Camerasip135.",
            'host': "10.100.68.253",
            'database': "envio"
        }
        try: 
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT modelo FROM cameras WHERE cameraid = %s"
            cursor.execute(sql, (camera_id,))
            modelo = cursor.fetchone()
            cursor.close()
            conn.close()
            
            if modelo:
                return modelo['modelo']
            else:
                print(f"Nenhum modelo encontrado com o id: {camera_id}")
                return ""
        except mysql.connector.Error as e:
            print(f"Erro ao buscar o modelo da câmera: {e}")
            return ""

    # Obtém o MAC da câmera pelo ID
    def get_mac_dao(self, camera_id):
        sql = "SELECT MAC FROM cameras WHERE cameraid = ?"
        mac = ""

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (camera_id,))
            mac = cursor.fetchone()
            if mac:
                mac = mac[0]
            else:
                print(f"Nenhum MAC encontrado com o id: {camera_id}")
        except sqlite3.Error as e:
            print(f"Erro ao buscar o MAC da câmera: {e}")

        return mac

    # Atualiza o modelo da câmera
    def set_modelo(self, camera_id, novo_modelo):
        sql = "UPDATE cameras SET modelo = ? WHERE cameraid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_modelo, camera_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    # Atualiza o MAC da câmera
    def set_mac(self, camera_id, novo_mac):
        sql = "UPDATE cameras SET MAC = ? WHERE cameraid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_mac, camera_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    # Retorna a lista de câmeras
    def get_cameras(self):
        minha_lista = []

        try:
            sql = "SELECT * FROM cameras"
            cursor = self.connection.cursor()
            cursor.execute(sql)

            rows = cursor.fetchall()
            for row in rows:
                nome = row[1]  # Considerando que o modelo está na segunda coluna
                mac = row[2]   # Considerando que o MAC está na terceira coluna
                camera = Camera(nome, mac)  # Assumindo que a classe Camera já existe
                minha_lista.append(camera)
        except sqlite3.Error as e:
            print(f"Erro: {e}")

        return minha_lista

    # Adiciona uma nova câmera
    def add_camera(self, modelo, mac):
        sql = "INSERT INTO cameras (modelo, MAC) VALUES (?, ?)"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (modelo, mac))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    # Exclui uma câmera
    def del_camera(self, camera_id):
        sql = "DELETE FROM cameras WHERE cameraid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (camera_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

# Exemplo de uso
def main():
    try:
        connection = sqlite3.connect("envio.db")  # Ajuste o caminho do banco de dados conforme necessário
        camera_dao = CameraDAO(connection)
        
        # Exemplo: adicionar uma nova câmera
        camera_dao.add_camera("Modelo X", "00:14:22:01:23:45")

        # Exemplo: obter a lista de câmeras
        cameras = camera_dao.get_cameras()
        for camera in cameras:
            print(f"Modelo: {camera.get_modelo()}, MAC: {camera.get_mac()}")

    except sqlite3.Error as e:
        print(f"Erro na conexão: {e}")

if __name__ == "__main__":
    main()
