import mysql.connector
from mysql.connector import Error
from Controller.clienteDAO import ClienteDAO


class Cliente:
    def __init__(self, nome="", telefone="", email="", numero_cliente=0, endereco=""):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.numero_cliente = numero_cliente
        self.endereco = endereco
        self.cliente_dao = ClienteDAO()

    def get_cliente_id(self, nome, numero_cliente):
        return self.cliente_dao.get_cliente_id_dao(nome, numero_cliente)

    def get_nome(self):
        cliente_id = self.get_cliente_id(self.nome, self.numero_cliente)
        return self.cliente_dao.get_nome_dao(cliente_id)

    def get_nome_id(self, cliente_id):
        return self.cliente_dao.get_nome_dao(cliente_id)

    def get_telefone(self):
        cliente_id = self.get_cliente_id(self.nome, self.numero_cliente)
        return self.cliente_dao.get_telefone_dao(cliente_id)
    
    def get_telefone_id(self, cliente_id):
        return self.cliente_dao.get_telefone_dao(cliente_id)
    
    def get_email(self):
        cliente_id = self.get_cliente_id(self.nome, self.numero_cliente)
        return self.cliente_dao.get_email_dao(cliente_id)

    def get_endereco(self):
        cliente_id = self.get_cliente_id(self.nome, self.numero_cliente)
        return self.cliente_dao.get_endereco_dao(cliente_id)

    def get_numero_cliente(self):
        cliente_id = self.get_cliente_id(self.nome, self.numero_cliente)
        return self.cliente_dao.get_numero_cliente_dao(cliente_id)

    def get_numero_cliente_id(self, cliente_id):
        return self.cliente_dao.get_numero_cliente_dao(cliente_id)

    def get_clientes(self):
        return self.cliente_dao.get_clientes_dao()

    def set_nome(self, nome):
        aux_nome = self.nome
        self.nome = nome
        cliente_id = self.get_cliente_id(aux_nome, self.numero_cliente)
        self.cliente_dao.set_nome_dao(cliente_id, nome)

    def set_nome_id(self, cliente_id, nome):
        self.cliente_dao.set_nome_dao(cliente_id, nome)

    def set_telefone(self, telefone):
        self.telefone = telefone
        cliente_id = self.get_cliente_id(self.nome, self.numero_cliente)
        self.cliente_dao.set_telefone_dao(cliente_id, telefone)

    def set_telefone_id(self, cliente_id, telefone):
        self.cliente_dao.set_telefone_dao(cliente_id, telefone)

    def set_email(self, email):
        self.email = email
        cliente_id = self.get_cliente_id(self.nome, self.numero_cliente)
        self.cliente_dao.set_email_dao(cliente_id, email)

    def set_email_id(self, cliente_id, email):
        self.cliente_dao.set_email_dao(cliente_id, email)

    def set_endereco(self, endereco):
        self.endereco = endereco
        cliente_id = self.get_cliente_id(self.nome, self.numero_cliente)
        self.cliente_dao.set_endereco_dao(cliente_id, endereco)

    def set_endereco_id(self, cliente_id, endereco):
        self.cliente_dao.set_endereco_dao(cliente_id, endereco)

    def set_numero_cliente(self, numero_cliente):
        aux_numero_cliente = self.numero_cliente
        self.numero_cliente = numero_cliente
        cliente_id = self.get_cliente_id(self.nome, aux_numero_cliente)
        self.cliente_dao.set_numero_cliente_dao(cliente_id, numero_cliente)

    def set_numero_cliente_id(self, cliente_id, numero_cliente):
        self.cliente_dao.set_numero_cliente_dao(cliente_id, numero_cliente)

    def add_cliente(self):
        self.cliente_dao.add_cliente_dao(self.nome, self.telefone, self.email, self.numero_cliente, self.endereco)

    def del_cliente(self, nome, numero_cliente):
        cliente_id = self.get_cliente_id(nome, numero_cliente)
        self.cliente_dao.del_cliente_dao(cliente_id)

    def del_cliente_id(self, cliente_id):
        self.cliente_dao.del_cliente_dao(cliente_id)
