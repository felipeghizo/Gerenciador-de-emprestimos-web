<?php

class Conexao {
    private $pdo;

    public function __construct($banco, $ip, $senha) {
        $dsn = "mysql:host=$ip;dbname=$banco;charset=utf8";
        $user = "root"; // Nome de usuário do MySQL

        // Configurar opções do PDO
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Lançar exceções em caso de erro
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch mode padrão
            PDO::ATTR_EMULATE_PREPARES => false, // Desativar emulação de prepared statements
        ];

        // Criar uma instância do PDO
        try {
            $this->pdo = new PDO($dsn, $user, $senha, $options);
        } catch (PDOException $e) {
            // Exibir mensagem de erro ou registrar em log
            echo "Falha na conexão: " . $e->getMessage();
            $this->pdo = null;
        }
    }

    public function getConexao() {
        return $this->pdo;
    }
}

?>