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

    # Adiciona Envio
    def add_envio(self, clienteid, cameraid, nota_fiscal, sequencia, numero_pedido, status):
        self.envio_dao.add_envio_DAO(clienteid, cameraid, nota_fiscal, sequencia, numero_pedido, status)

    # Edita Envio 
    def edit_envio(self, envioid, editNumero_pedido, editSequencia, editStatus):
        self.envio_dao.edit_envio_DAO(envioid, editNumero_pedido, editSequencia, editStatus)

    # Remove Envio
    def delete_envio(self, envio_id):
        self.envio_dao.delete_envio_DAO(envio_id)
