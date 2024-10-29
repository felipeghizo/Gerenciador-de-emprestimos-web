from Controller.envioDAO import EnvioDAO

class Envio:

    def __init__(self, clienteid=0, cameraid=0, acesso="", nota_fiscal=0, sequencia=0, numero_pedido=0, status=""):
        self.clienteid = clienteid
        self.cameraid = cameraid
        self.acesso = acesso
        self.nota_fiscal = nota_fiscal
        self.sequencia = sequencia
        self.numero_pedido = numero_pedido
        self.status = status
        self.envio_dao = EnvioDAO()

    ''' GETS '''
    def getClienteid(self, envioid):
        return self.envio_dao.getClienteidDAO(envioid)
    
    def getCameraid(self, envioid):
        return self.envio_dao.getCameraidDAO(envioid)
    
    def getAcesso(self, envioid):
        return self.envio_dao.getAcessoDAO(envioid)
    
    def getNotaFiscal(self, envioid):
        return self.envio_dao.getNotaFiscalDAO(envioid)
    
    def getSequencia(self, envioid):
        return self.envio_dao.getSequenciaDAO(envioid)
    
    def getNumeroPedido(self, envioid):
        return self.envio_dao.getNumeroPedidoDAO(envioid)
    
    def getStatus(self, envioid):
        return self.envio_dao.getStatusDAO(envioid)

    ''' SETS '''
    def setClienteid(self, novo_clienteid, envioid):
        self.clienteid = novo_clienteid
        self.envio_dao.setClienteidDAO(novo_clienteid, envioid)
    
    def setCameraid(self, nova_cameraid, envioid):
        self.cameraid = nova_cameraid
        self.envio_dao.setCameraidDAO(nova_cameraid, envioid)
    
    def setAcesso(self,  novo_acesso, envioid):
        self.acesso =  novo_acesso
        self.envio_dao.setAcessoDAO(novo_acesso, envioid)
    
    def setNotaFiscal(self, nova_notaFiscal, envioid):
        self.nota_fiscal = nova_notaFiscal
        self.envio_dao.setNotaFiscalDAO(nova_notaFiscal, envioid)
    
    def setSequencia(self, nova_sequencia, envioid):
        self.sequencia = nova_sequencia
        self.envio_dao.setSequenciaDAO(nova_sequencia, envioid)
    
    def setNumeroPedido(self, novo_numeropedido, envioid):
        self.numero_pedido = novo_numeropedido
        self.envio_dao.setNumeroPedidoDAO(novo_numeropedido, envioid)
    
    def setStatus(self, novo_status, envioid):
        self.status = novo_status
        self.envio_dao.setStatusDAO(novo_status, envioid)

    # Adiciona Envio
    def add_envio(self, clienteid, cameraid, nota_fiscal, sequencia, numero_pedido):
        return self.envio_dao.addEnvioDAO(clienteid, cameraid, nota_fiscal, sequencia, numero_pedido)

    def visualizar_dados(self):
        return self.envio_dao.visualizarDadosDAO()

    # Edita Envio 
    def edit_envio(self, envioid, clienteid, cameraid, acesso, nota_fiscal, sequencia, numero_pedido, status):
        self.setClienteid(clienteid, envioid)
        self.setCameraid(cameraid, envioid)
        self.setAcesso(acesso, envioid)
        self.setNotaFiscal(nota_fiscal, envioid)
        self.setSequencia(sequencia, envioid)
        self.setNumeroPedido(numero_pedido, envioid)
        self.setStatus(status, envioid)

    # Remove Envio
    def delete_envio(self, envio_id):
        self.envio_dao.setStatusDAO("Finalizado", envio_id)