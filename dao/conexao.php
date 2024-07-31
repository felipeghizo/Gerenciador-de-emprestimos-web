<?php

class Conexao {
    private $dsn;
    private $user;
    private $password;
    private $options;

    public function __construct() {
        // Configurar os detalhes da conexão
        $server = "10.100.68.253"; // Endereço IP do servidor MySQL na rede local
        $database = "envio";     // Nome do banco de dados que você deseja acessar
        $this->dsn = "mysql:host=$server;dbname=$database;charset=utf8";
        $this->user = "root";    // Nome de usuário do MySQL
        $this->password = "Camerasip135."; // Senha do usuário do MySQL
        
        // Configurar opções do PDO
        $this->options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Lançar exceções em caso de erro
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch mode padrão
            PDO::ATTR_EMULATE_PREPARES => false, // Desativar emulação de prepared statements
        ];
    }

    public function getConexao() {
        try {
            // Conectando...
            $pdo = new PDO($this->dsn, $this->user, $this->password, $this->options);
            return $pdo;
        } catch (PDOException $e) { // Captura erros de conexão
            echo "Não foi possível conectar: " . $e->getMessage();
            return null;
        }
    }
}

// Exemplo de uso
$conexao = new Conexao();
$db = $conexao->getConexao();
if ($db) {
    echo "Conexão bem-sucedida!";
} else {
    echo "Falha na conexão.";
}

?>
