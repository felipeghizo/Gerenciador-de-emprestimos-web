<?php

require_once 'EnvioDAO.php'; // Certifique-se de que o caminho está correto

class Envio {

    private $clienteid;
    private $cameraid;
    private $acesso;
    private $data_entrega;
    private $data_envio;
    private $data_instalacao;
    private $nota_fiscal;
    private $sequencia;
    private $numero_pedido;
    private $status;
    private $envioDAO;

    // Construtor Default
    public function __construct($clienteid = 0, $cameraid = 0, $acesso = "", $data_entrega = "", $data_envio = "", $data_instalacao = "", $nota_fiscal = 0, $sequencia = 0, $numero_pedido = 0, $status = "") {
        $this->clienteid = $clienteid;
        $this->cameraid = $cameraid;
        $this->acesso = $acesso;
        $this->data_entrega = $data_entrega;
        $this->data_envio = $data_envio;
        $this->data_instalacao = $data_instalacao;
        $this->nota_fiscal = $nota_fiscal;
        $this->sequencia = $sequencia;
        $this->numero_pedido = $numero_pedido;
        $this->status = $status;
        $this->envioDAO = new EnvioDAO();
    }

    // Gets
    public function getEnvioid($clienteid, $cameraid) {
        return $this->envioDAO->getEnvioidDAO($clienteid, $cameraid);
    }

    public function getClienteid() {
        return $this->envioDAO->getClienteidDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getClienteID($ID) {
        return $this->envioDAO->getClienteidDAO($ID);
    }

    public function getCameraid() {
        return $this->envioDAO->getCameraidDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getCameraID($ID) {
        return $this->envioDAO->getCameraidDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getAcesso() {
        return $this->envioDAO->getAcessoDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getAcessoID($ID) {
        return $this->envioDAO->getAcessoDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getData_Entrega() {
        return $this->envioDAO->getData_EntregaDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getData_EntregaID($ID) {
        return $this->envioDAO->getData_EntregaDAO($ID);
    }

    public function getData_Envio() {
        return $this->envioDAO->getData_EnvioDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getData_EnvioID($ID) {
        return $this->envioDAO->getData_EnvioDAO($ID);
    }

    public function getData_Instalacao() {
        return $this->envioDAO->getData_InstalacaoDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getData_InstalacaoID($ID) {
        return $this->envioDAO->getData_InstalacaoDAO($ID);
    }

    public function getNotaFiscal() {
        return $this->envioDAO->getNotaFiscalDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getNotaFiscalID($ID) {
        return $this->envioDAO->getNotaFiscalDAO($ID);
    }

    public function getSequencia() {
        return $this->envioDAO->getSequenciaDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getSequenciaID($ID) {
        return $this->envioDAO->getSequenciaDAO($ID);
    }

    public function getNumero_Pedido() {
        return $this->envioDAO->getNumero_PedidoDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getNumero_PedidoID($ID) {
        return $this->envioDAO->getNumero_PedidoDAO($ID);
    }

    public function getStatus() {
        return $this->envioDAO->getStatusDAO($this->getEnvioid($this->clienteid, $this->cameraid));
    }

    public function getStatusID($ID) {
        return $this->envioDAO->getStatusDAO($ID);
    }

    // Get lista de envios
    public function getEnvios() {
        return $this->envioDAO->getEnviosDAO();
    }

    // Sets
    public function setClienteid($clienteid) {
        $this->envioDAO->setClienteidDAO($this->getEnvioid($this->clienteid, $this->cameraid), $clienteid);
        $this->clienteid = $clienteid;
    }

    public function setCameraid($cameraid) {
        $this->envioDAO->setCameraidDAO($this->getEnvioid($this->clienteid, $this->cameraid), $cameraid);
        $this->cameraid = $cameraid;
    }

    public function setAcesso($acesso) {
        $this->envioDAO->setAcessoDAO($this->getEnvioid($this->clienteid, $this->cameraid), $acesso);
        $this->acesso = $acesso;
    }

    public function setAcessoID($ID, $acesso) {
        $this->envioDAO->setAcessoDAO($ID, $acesso);
    }

    public function setData_Entrega($data_entrega) {
        $this->envioDAO->setData_EntregaDAO($this->getEnvioid($this->clienteid, $this->cameraid), $data_entrega);
        $this->data_entrega = $data_entrega;
    }

    public function setData_EntregaID($ID, $data_entrega) {
        $this->envioDAO->setData_EntregaDAO($ID, $data_entrega);
    }

    public function setData_Envio($data_envio) {
        $this->envioDAO->setData_EnvioDAO($this->getEnvioid($this->clienteid, $this->cameraid), $data_envio);
        $this->data_envio = $data_envio;
    }

    public function setData_EnvioID($ID, $data_envio) {
        $this->envioDAO->setData_EnvioDAO($ID, $data_envio);
    }

    public function setData_Instalacao($data_instalacao) {
        $this->envioDAO->setData_InstalacaoDAO($this->getEnvioid($this->clienteid, $this->cameraid), $data_instalacao);
        $this->data_instalacao = $data_instalacao;
    }

    public function setData_InstalacaoID($ID, $data_instalacao) {
        $this->envioDAO->setData_InstalacaoDAO($ID, $data_instalacao);
    }

    public function setNota_Fiscal($nota_fiscal) {
        $this->envioDAO->setNota_FiscalDAO($this->getEnvioid($this->clienteid, $this->cameraid), $nota_fiscal);
        $this->nota_fiscal = $nota_fiscal;
    }

    public function setSequencia($sequencia) {
        $this->envioDAO->setSequenciaDAO($this->getEnvioid($this->clienteid, $this->cameraid), $sequencia);
        $this->sequencia = $sequencia;
    }

    public function setNumero_Pedido($numero_pedido) {
        $this->envioDAO->setNumero_PedidoDAO($this->getEnvioid($this->clienteid, $this->cameraid), $numero_pedido);
        $this->numero_pedido = $numero_pedido;
    }

    public function setStatus($ID, $status) {
        $this->envioDAO->setStatusDAO($ID, $status);
        $this->status = $status;
    }

    // Adiciona Envio ao banco de dados
    public function addEnvio($clienteid, $cameraid, $nota_fiscal, $sequencia, $numero_pedido, $status) {
        $this->envioDAO->addEnvioDAO($clienteid, $cameraid, $nota_fiscal, $sequencia, $numero_pedido, $status);
    }

    // Remove Envio do banco de dados
    public function removeEnvio($envioid) {
        $this->envioDAO->removeEnvioDAO($envioid);
    }
}

?>