import sqlite3
import mysql.connector

class ClienteDAO:
    def __init__(self, nome="", telefone="", email="", numero_cliente=0, endereco=""):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.numero_cliente = numero_cliente
        self.endereco = endereco
        self.connection = self.conectar()

    def conectar(self):
        banco = "envio.db"  # Ajuste o caminho do banco de dados conforme necessário
        try:
            connection = sqlite3.connect(banco)
            return connection
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    # Obtém o ID do cliente
    def get_cliente_id(self, nome, numero_cliente):
        sql = "SELECT COUNT(*) AS total FROM clientes WHERE nome = ? AND numero_cliente = ?"
        cliente_id = 0

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (nome, numero_cliente))
            total_clientes = cursor.fetchone()[0]

            if total_clientes > 0:
                sql = "SELECT clienteid FROM clientes WHERE nome = ? AND numero_cliente = ?"
                cursor.execute(sql, (nome, numero_cliente))
                cliente_id = cursor.fetchone()[0]
            else:
                return -1
        except sqlite3.Error as e:
            print(f"Erro ao procurar cliente: {e}")

        return cliente_id

    # Obtém o nome do cliente pelo ID
    def get_nome_dao(self, cliente_id):
        db_config = {
            'user': 'root',
            'password': "Camerasip135.",
            'host': "10.100.68.253",
            'database': "envio"
        }
        try: 
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT nome FROM clientes WHERE clienteid = %s"
            cursor.execute(sql, (cliente_id,))
            nome = cursor.fetchone()
            cursor.close()
            conn.close()
            
            if nome:
                return nome['nome']
            else:
                print(f"Nenhum nome encontrado com o id: {cliente_id}")
                return ""
        except mysql.connector.Error as e:
            print(f"Erro ao buscar o nome do cliente: {e}")
            return ""

    # Obtém o telefone do cliente pelo ID
    def get_telefone_dao(self, cliente_id):
        sql = "SELECT telefone FROM clientes WHERE clienteid = ?"
        telefone = ""

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (cliente_id,))
            telefone = cursor.fetchone()
            if telefone:
                telefone = telefone[0]
            else:
                print(f"Nenhum telefone encontrado com o id: {cliente_id}")
        except sqlite3.Error as e:
            print(f"Erro ao buscar o telefone do cliente: {e}")

        return telefone

    # Obtém o email do cliente pelo ID
    def get_email(self, cliente_id):
        sql = "SELECT email FROM clientes WHERE clienteid = ?"
        email = ""

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (cliente_id,))
            email = cursor.fetchone()
            if email:
                email = email[0]
            else:
                print(f"Nenhum email encontrado com o id: {cliente_id}")
        except sqlite3.Error as e:
            print(f"Erro ao buscar o email do cliente: {e}")

        return email

    # Obtém o endereço do cliente pelo ID
    def get_endereco(self, cliente_id):
        sql = "SELECT endereco FROM clientes WHERE clienteid = ?"
        endereco = ""

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (cliente_id,))
            endereco = cursor.fetchone()
            if endereco:
                endereco = endereco[0]
            else:
                print(f"Nenhum endereço encontrado com o id: {cliente_id}")
        except sqlite3.Error as e:
            print(f"Erro ao buscar o endereço do cliente: {e}")

        return endereco

    # Obtém o número do cliente pelo ID
    def get_numero_cliente(self, cliente_id):
        sql = "SELECT numero_cliente FROM clientes WHERE clienteid = ?"
        numero_cliente = 0

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (cliente_id,))
            numero_cliente = cursor.fetchone()
            if numero_cliente:
                numero_cliente = numero_cliente[0]
            else:
                print(f"Nenhum número de cliente encontrado com o id: {cliente_id}")
        except sqlite3.Error as e:
            print(f"Erro ao buscar o número de cliente: {e}")

        return numero_cliente

    # Atualiza o nome do cliente
    def set_nome(self, cliente_id, novo_nome):
        sql = "UPDATE clientes SET nome = ? WHERE clienteid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_nome, cliente_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    # Atualiza o telefone do cliente
    def set_telefone(self, cliente_id, novo_telefone):
        sql = "UPDATE clientes SET telefone = ? WHERE clienteid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_telefone, cliente_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    # Atualiza o email do cliente
    def set_email(self, cliente_id, novo_email):
        sql = "UPDATE clientes SET email = ? WHERE clienteid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_email, cliente_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    # Atualiza o endereço do cliente
    def set_endereco(self, cliente_id, novo_endereco):
        sql = "UPDATE clientes SET endereco = ? WHERE clienteid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_endereco, cliente_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    # Atualiza o número do cliente
    def set_numero_cliente(self, cliente_id, novo_numero_cliente):
        sql = "UPDATE clientes SET numero_cliente = ? WHERE clienteid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_numero_cliente, cliente_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    # Retorna a lista de clientes
    def get_clientes(self):
        minha_lista = []

        try:
            sql = "SELECT * FROM clientes"
            cursor = self.connection.cursor()
            cursor.execute(sql)

            rows = cursor.fetchall()
            for row in rows:
                nome = row[1]  # Assumindo que o nome está na segunda coluna
                telefone = row[2]  # Assumindo que o telefone está na terceira coluna
                email = row[3]  # Assumindo que o email está na quarta coluna
                numero_cliente = row[4]  # Assumindo que o número do cliente está na quinta coluna
                endereco = row[5]  # Assumindo que o endereço está na sexta coluna
                cliente = Cliente(nome, telefone, email, numero_cliente, endereco)  # Assumindo que a classe Cliente já existe
                minha_lista.append(cliente)
        except sqlite3.Error as e:
            print(f"Erro: {e}")

        return minha_lista

    # Adiciona um cliente
    def add_cliente(self, nome, telefone, email, numero_cliente, endereco):
        sql = "INSERT INTO clientes (nome, telefone, email, numero_cliente, endereco) VALUES (?, ?, ?, ?, ?)"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (nome, telefone, email, numero_cliente, endereco))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    # Exclui um cliente
    def del_cliente(self, cliente_id):
        sql = "DELETE FROM clientes WHERE clienteid = ?"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (cliente_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

# Exemplo de uso
def main():
    try:
        cliente_dao = ClienteDAO()
        
        # Exemplo: adicionar um cliente
        cliente_dao.add_cliente("João da Silva", "1234-5678", "joao@example.com", 123, "Rua das Flores, 123")

        # Exemplo: obter a lista de clientes
        clientes = cliente_dao.get_clientes()
        for cliente in clientes:
            print(f"Nome: {cliente.get_nome_dao()}, Telefone: {cliente.get_telefone()}, Email: {cliente.get_email()}, Número: {cliente.get_numero_cliente()}, Endereço: {cliente.get_endereco()}")

    except sqlite3.Error as e:
        print(f"Erro na conexão: {e}")

if __name__ == "__main__":
    main()
