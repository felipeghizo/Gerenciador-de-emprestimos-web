import mysql.connector
from mysql.connector import Error

class EnvioDAO:
    def __init__(self):
        self.conexao = Conexao()  # Conecta ao banco de dados

    def _executar_query(self, sql, params):
        try:
            conn = self.conexao.get_conexao()
            if conn:
                cursor = conn.cursor(dictionary=True)
                cursor.execute(sql, params)
                resultado = cursor.fetchall()
                cursor.close()
                return resultado
        except Error as e:
            print(f"Erro ao executar a consulta: {e}")
        return []

    def get_envio_id(self, cliente_id, camera_id):
        sql = "SELECT COUNT(*) AS total FROM envios WHERE clienteid = %s AND cameraid = %s"
        resultado = self._executar_query(sql, (cliente_id, camera_id))
        
        if resultado and resultado[0]['total'] > 0:
            sql = "SELECT envioid FROM envios WHERE clienteid = %s AND cameraid = %s"
            resultado = self._executar_query(sql, (cliente_id, camera_id))
            if resultado:
                return resultado[0].get('envioid', -1)
        return -1

    def get_cliente_id(self, envio_id):
        sql = "SELECT clienteid FROM envios WHERE envioid = %s"
        resultado = self._executar_query(sql, (envio_id,))
        if resultado:
            return resultado[0].get('clienteid', 0)
        print(f"Nenhum clienteid encontrado com o id: {envio_id}")
        return 0

    def get_camera_id(self, envio_id):
        sql = "SELECT cameraid FROM envios WHERE envioid = %s"
        resultado = self._executar_query(sql, (envio_id,))
        if resultado:
            return resultado[0].get('cameraid', 0)
        print(f"Nenhum cameraid encontrado com o id: {envio_id}")
        return 0

    def get_acesso(self, envio_id):
        sql = "SELECT acesso FROM envios WHERE envioid = %s"
        resultado = self._executar_query(sql, (envio_id,))
        if resultado:
            return resultado[0].get('acesso', "")
        print(f"Nenhum acesso encontrado com o id: {envio_id}")
        return ""

    def get_data_entrega(self, envio_id):
        sql = "SELECT data_entrega FROM envios WHERE envioid = %s"
        resultado = self._executar_query(sql, (envio_id,))
        if resultado:
            return resultado[0].get('data_entrega', "")
        print(f"Nenhuma data_entrega encontrada com o id: {envio_id}")
        return ""

    def get_data_envio(self, envio_id):
        sql = "SELECT data_envio FROM envios WHERE envioid = %s"
        resultado = self._executar_query(sql, (envio_id,))
        if resultado:
            return resultado[0].get('data_envio', "")
        print(f"Nenhuma data_envio encontrada com o id: {envio_id}")
        return ""

    def get_data_instalacao(self, envio_id):
        sql = "SELECT data_instalacao FROM envios WHERE envioid = %s"
        resultado = self._executar_query(sql, (envio_id,))
        if resultado:
            return resultado[0].get('data_instalacao', "")
        print(f"Nenhuma data_instalacao encontrada com o id: {envio_id}")
        return ""

    def get_nota_fiscal(self, envio_id):
        sql = "SELECT nota_fiscal FROM envios WHERE envioid = %s"
        resultado = self._executar_query(sql, (envio_id,))
        if resultado:
            return resultado[0].get('nota_fiscal', 0)
        print(f"Nenhuma nota_fiscal encontrada com o id: {envio_id}")
        return 0

    def get_sequencia(self, envio_id):
        sql = "SELECT sequencia FROM envios WHERE envioid = %s"
        resultado = self._executar_query(sql, (envio_id,))
        if resultado:
            return resultado[0].get('sequencia', 0)
        print(f"Nenhuma sequencia encontrada com o id: {envio_id}")
        return 0

    def get_numero_pedido(self, envio_id):
        sql = "SELECT numero_pedido FROM envios WHERE envioid = %s"
        resultado = self._executar_query(sql, (envio_id,))
        if resultado:
            return resultado[0].get('numero_pedido', 0)
        print(f"Nenhum numero_pedido encontrado com o id: {envio_id}")
        return 0

class Conexao:
    def __init__(self):
        self.connection = self.conectar()

    def conectar(self):
        try:
            return mysql.connector.connect(
                host='10.100.68.253',
                database='envio',
                user='root',
                password='Camerasip135.'
            )
        except Error as e:
            print(f"Falha na conexão: {e}")
        return None

    def get_conexao(self):
        return self.connection
