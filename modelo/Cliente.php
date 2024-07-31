<?php

require_once 'ClienteDAO.php'; // Certifique-se de que o caminho está correto

class Cliente {

    private $nome;
    private $telefone;
    private $email;
    private $NumeroCliente;
    private $endereco;
    private $clienteDAO;

    // Construtor Default
    public function __construct($nome = "", $telefone = "", $email = "", $NumeroCliente = 0, $endereco = "") {
        $this->nome = $nome;
        $this->telefone = $telefone;
        $this->email = $email;
        $this->NumeroCliente = $NumeroCliente;
        $this->endereco = $endereco;
        $this->clienteDAO = new ClienteDAO();
    }

    // Gets
    public function getClienteid($nome, $NumeroCliente) {
        return $this->clienteDAO->getClienteidDAO($nome, $NumeroCliente);
    }

    public function getNome() {
        return $this->clienteDAO->getNomeDAO($this->getClienteid($this->nome, $this->NumeroCliente));
    }

    public function getNomeID($ID) {
        return $this->clienteDAO->getNomeDAO($ID);
    }

    public function getTelefone() {
        return $this->clienteDAO->getTelefoneDAO($this->getClienteid($this->nome, $this->NumeroCliente));
    }

    public function getEmail() {
        return $this->clienteDAO->getEmailDAO($this->getClienteid($this->nome, $this->NumeroCliente));
    }

    public function getEndereco() {
        return $this->clienteDAO->getEnderecoDAO($this->getClienteid($this->nome, $this->NumeroCliente));
    }

    public function getNumeroCliente() {
        return $this->clienteDAO->getNumeroClienteDAO($this->getClienteid($this->nome, $this->NumeroCliente));
    }

    public function getNumeroClienteID($ID) {
        return $this->clienteDAO->getNumeroClienteDAO($ID);
    }

    // Get lista de clientes
    public function getClientes() {
        return $this->clienteDAO->getClientesDAO();
    }

    // Sets
    public function setNome($nome) {
        $auxNome = $this->nome;
        $this->nome = $nome;
        $this->clienteDAO->setNomeDAO($this->getClienteid($auxNome, $this->NumeroCliente), $nome);
    }

    public function setNomeID($ID, $nome) {
        $this->clienteDAO->setNomeDAO($ID, $nome);
    }

    public function setTelefone($telefone) {
        $this->telefone = $telefone;
        $this->clienteDAO->setTelefoneDAO($this->getClienteid($this->nome, $this->NumeroCliente), $telefone);
    }

    public function setTelefoneID($ID, $telefone) {
        $this->clienteDAO->setTelefoneDAO($ID, $telefone);
    }

    public function setEmail($email) {
        $this->email = $email;
        $this->clienteDAO->setEmailDAO($this->getClienteid($this->nome, $this->NumeroCliente), $email);
    }

    public function setEmailID($ID, $email) {
        $this->clienteDAO->setEmailDAO($ID, $email);
    }

    public function setEndereco($endereco) {
        $this->endereco = $endereco;
        $this->clienteDAO->setEnderecoDAO($this->getClienteid($this->nome, $this->NumeroCliente), $endereco);
    }

    public function setEnderecoID($ID, $endereco) {
        $this->clienteDAO->setEnderecoDAO($ID, $endereco);
    }

    public function setNumeroCliente($NumeroCliente) {
        $auxNumeroCliente = $this->NumeroCliente;
        $this->NumeroCliente = $NumeroCliente;
        $this->clienteDAO->setNumeroClienteDAO($this->getClienteid($this->nome, $auxNumeroCliente), $NumeroCliente);
    }

    public function setNumeroClienteID($ID, $NumeroCliente) {
        $this->clienteDAO->setNumeroClienteDAO($ID, $NumeroCliente);
    }

    // Adiciona cliente ao banco de dados
    public function addCliente() {
        $this->clienteDAO->addClienteDAO($this->nome, $this->telefone, $this->email, $this->NumeroCliente, $this->endereco);
    }

    // Deleta cliente do banco de dados
    public function delCliente($nome, $numeroCliente) {
        $this->clienteDAO->delClienteDAO($this->getClienteid($nome, $numeroCliente));
    }

    public function delClienteID($ID) {
        $this->clienteDAO->delClienteDAO($ID);
    }
}

?>