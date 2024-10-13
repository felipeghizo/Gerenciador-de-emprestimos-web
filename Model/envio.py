# Certifique-se de que o caminho para EnvioDAO está correto
from Controller.envioDAO import EnvioDAO

class Envio:

    def __init__(self, clienteid=0, cameraid=0, acesso="", data_entrega="", data_envio="", data_instalacao="", nota_fiscal=0, sequencia=0, numero_pedido=0, status=""):
        self.clienteid = clienteid
        self.cameraid = cameraid
        self.acesso = acesso
        self.data_entrega = data_entrega
        self.data_envio = data_envio
        self.data_instalacao = data_instalacao
        self.nota_fiscal = nota_fiscal
        self.sequencia = sequencia
        self.numero_pedido = numero_pedido
        self.status = status
        self.envio_dao = EnvioDAO()

    # Gets
    def get_envio_id(self, clienteid, cameraid):
        return self.envio_dao.get_envio_id_dao(clienteid, cameraid)

    def get_cliente_id(self):
        return self.envio_dao.get_cliente_id_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_cliente_id_by(self, envio_id):
        return self.envio_dao.get_cliente_id_dao(envio_id)

    def get_camera_id(self):
        return self.envio_dao.get_camera_id_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_camera_id_by(self, envio_id):
        return self.envio_dao.get_camera_id_dao(envio_id)

    def get_acesso(self):
        return self.envio_dao.get_acesso_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_acesso_by(self, envio_id):
        return self.envio_dao.get_acesso_dao(envio_id)

    def get_data_entrega(self):
        return self.envio_dao.get_data_entrega_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_data_entrega_by(self, envio_id):
        return self.envio_dao.get_data_entrega_dao(envio_id)

    def get_data_envio(self):
        return self.envio_dao.get_data_envio_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_data_envio_by(self, envio_id):
        return self.envio_dao.get_data_envio_dao(envio_id)

    def get_data_instalacao(self):
        return self.envio_dao.get_data_instalacao_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_data_instalacao_by(self, envio_id):
        return self.envio_dao.get_data_instalacao_dao(envio_id)

    def get_nota_fiscal(self):
        return self.envio_dao.get_nota_fiscal_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_nota_fiscal_by(self, envio_id):
        return self.envio_dao.get_nota_fiscal_dao(envio_id)

    def get_sequencia(self):
        return self.envio_dao.get_sequencia_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_sequencia_by(self, envio_id):
        return self.envio_dao.get_sequencia_dao(envio_id)

    def get_numero_pedido(self):
        return self.envio_dao.get_numero_pedido_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_numero_pedido_by(self, envio_id):
        return self.envio_dao.get_numero_pedido_dao(envio_id)

    def get_status(self):
        return self.envio_dao.get_status_dao(self.get_envio_id(self.clienteid, self.cameraid))

    def get_status_by(self, envio_id):
        return self.envio_dao.get_status_dao(envio_id)

    def get_envios(self):
        return self.envio_dao.get_envios_dao()

    # Sets
    def set_cliente_id(self, clienteid):
        envio_id = self.get_envio_id(self.clienteid, self.cameraid)
        self.envio_dao.set_cliente_id_dao(envio_id, clienteid)
        self.clienteid = clienteid

    def set_camera_id(self, cameraid):
        envio_id = self.get_envio_id(self.clienteid, self.cameraid)
        self.envio_dao.set_camera_id_dao(envio_id, cameraid)
        self.cameraid = cameraid

    def set_acesso(self, acesso):
        envio_id = self.get_envio_id(self.clienteid, self.cameraid)
        self.envio_dao.set_acesso_dao(envio_id, acesso)
        self.acesso = acesso

    def set_acesso_by(self, envio_id, acesso):
        self.envio_dao.set_acesso_dao(envio_id, acesso)

    def set_data_entrega(self, data_entrega):
        envio_id = self.get_envio_id(self.clienteid, self.cameraid)
        self.envio_dao.set_data_entrega_dao(envio_id, data_entrega)
        self.data_entrega = data_entrega

    def set_data_entrega_by(self, envio_id, data_entrega):
        self.envio_dao.set_data_entrega_dao(envio_id, data_entrega)

    def set_data_envio(self, data_envio):
        envio_id = self.get_envio_id(self.clienteid, self.cameraid)
        self.envio_dao.set_data_envio_dao(envio_id, data_envio)
        self.data_envio = data_envio

    def set_data_envio_by(self, envio_id, data_envio):
        self.envio_dao.set_data_envio_dao(envio_id, data_envio)

    def set_data_instalacao(self, data_instalacao):
        envio_id = self.get_envio_id(self.clienteid, self.cameraid)
        self.envio_dao.set_data_instalacao_dao(envio_id, data_instalacao)
        self.data_instalacao = data_instalacao

    def set_data_instalacao_by(self, envio_id, data_instalacao):
        self.envio_dao.set_data_instalacao_dao(envio_id, data_instalacao)

    def set_nota_fiscal(self, nota_fiscal):
        envio_id = self.get_envio_id(self.clienteid, self.cameraid)
        self.envio_dao.set_nota_fiscal_dao(envio_id, nota_fiscal)
        self.nota_fiscal = nota_fiscal

    def set_sequencia(self, sequencia):
        envio_id = self.get_envio_id(self.clienteid, self.cameraid)
        self.envio_dao.set_sequencia_dao(envio_id, sequencia)
        self.sequencia = sequencia

    def set_numero_pedido(self, numero_pedido):
        envio_id = self.get_envio_id(self.clienteid, self.cameraid)
        self.envio_dao.set_numero_pedido_dao(envio_id, numero_pedido)
        self.numero_pedido = numero_pedido

    def set_status(self, envio_id, status):
        self.envio_dao.set_status_dao(envio_id, status)
        self.status = status

    # Adiciona Envio ao banco de dados
    def add_envio(self, clienteid, cameraid, nota_fiscal, sequencia, numero_pedido, status):
        self.envio_dao.add_envio_dao(clienteid, cameraid, nota_fiscal, sequencia, numero_pedido, status)

    # Remove Envio do banco de dados
    def remove_envio(self, envio_id):
        self.envio_dao.remove_envio_dao(envio_id)
