import mysql.connector
from mysql.connector import Error

class Conexao:
    def __init__(self, banco, ip, senha, usuario="root"):
        self.banco = banco
        self.ip = ip
        self.senha = senha
        self.usuario = usuario
        self.connection = self.conectar()

    def conectar(self):
        try:
            connection = mysql.connector.connect(
                host=self.ip,
                database=self.banco,
                user=self.usuario,
                password=self.senha,
                use_pure=True
            )
            return connection
        except Error as e:
            print(f"Falha na conexão: {e}")
            return None

    def get_conexao(self):
        return self.connection

# Exemplo de uso
if __name__ == "__main__":
    try:
        conexao = Conexao("envio", "10.100.68.253", "Camerasip135.")
        db_connection = conexao.get_conexao()
        if db_connection:
            print("Conexão bem-sucedida!")
        else:
            print("Falha na conexão.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
