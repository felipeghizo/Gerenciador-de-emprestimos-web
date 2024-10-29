import sqlite3
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from Controller.conexaoDAO import ConexaoDAO


conexao = ConexaoDAO()

class CameraDAO:
    def __init__(self, modelo="", cloud="", mac=""):
        self.modelo = modelo
        self.mac = mac
        self.cloud = cloud
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

    # Obtém o Cloud da câmera pelo ID
    def get_cloud_dao(self, camera_id):
        sql = "SELECT Cloud FROM cameras WHERE cameraid = ?"
        mac = ""

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (camera_id,))
            mac = cursor.fetchone()
            if mac:
                mac = mac[0]
            else:
                print(f"Nenhum Cloud encontrado com o id: {camera_id}")
        except sqlite3.Error as e:
            print(f"Erro ao buscar o Cliud da câmera: {e}")

        return mac

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

    # Atualiza o cloud da câmera
    def set_modelo(self, camera_id, novo_cloud):
        sql = "UPDATE cameras SET Cloud = ? WHERE cameraid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_cloud, camera_id))
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
                nome = row[1]  
                Model = row[2]
                MAC = row[3]   
                minha_lista.append(nome, Model, MAC)
        except sqlite3.Error as e:
            print(f"Erro: {e}")

        return minha_lista

    # Adiciona uma nova câmera
    def add_camera_DAO(self, modelo, cloud, mac):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                query = "INSERT INTO cameras (modelo, Cloud, MAC) VALUES (%s, %s, %s)"
                cursor.execute(query, (modelo, cloud, mac))
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for('cameras'))
            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                return "Erro ao adicionar câmera", 500
        else:
            return "Erro na conexão com o banco de dados", 500
        
    def edit_camera_DAO(Modelo, Cloud, MAC, camid):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                query = """
                    UPDATE cameras
                    SET Modelo = %s, Cloud = %s, MAC = %s 
                    WHERE cameraid = %s
                """
                cursor.execute(query, (Modelo, Cloud, MAC, camid))
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for('cameras'))
            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                return "Erro ao editar cliente", 500
        else:
            return "Erro na conexão com o banco de dados", 500

    # Exclui uma câmera
    def del_camera_DAO(self, camera_id):
        sql = "DELETE FROM cameras WHERE cameraid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (camera_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")
