<?php
require_once 'Conexao.php';
class ClienteDAO {
    private $pdo;

    public function __construct($nome = "", $telefone = "", $email = "", $NumeroCliente = 0, $endereco = "") {
        $this->nome = $nome;
        $this->telefone = $telefone;
        $this->email = $email;
        $this->NumeroCliente = $NumeroCliente;
        $this->endereco = $endereco;
    }

    public function conectar(){
        $banco = "envio";
        $ip = "10.100.68.253";
        $senha = "Camerasip135.";

        // Cria a conexão
        $conexao = new Conexao($banco, $ip, $senha);
        return $pdo = $conexao->getConexao();
    }

    // Obtém o ID do cliente
    public function getClienteId($nome, $numeroCliente) {
        $sql = "SELECT COUNT(*) AS total FROM clientes WHERE nome = :nome AND numero_cliente = :numero_cliente";
        $clienteId = 0;

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['nome' => $nome, 'numero_cliente' => $numeroCliente]);

            $totalClientes = $stmt->fetchColumn();
            if ($totalClientes > 0) {
                $sql = "SELECT clienteid FROM clientes WHERE nome = :nome AND numero_cliente = :numero_cliente";
                $stmt2 = $this->pdo->prepare($sql);
                $stmt2->execute(['nome' => $nome, 'numero_cliente' => $numeroCliente]);
                $clienteId = $stmt2->fetchColumn();
            } else {
                return -1;
            }
        } catch (PDOException $e) {
            echo "Erro ao procurar cliente: " . $e->getMessage();
        }

        return $clienteId;
    }

    // Obtém o nome do cliente pelo ID
    public function getNomeDAO($clienteId) {
        $sql = "SELECT nome FROM clientes WHERE clienteid = :clienteid";
        $nome = "";

        try {

            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['clienteid' => $clienteId]);
            $nome = $stmt->fetchColumn();

            if ($nome === false) {
                echo "Nenhum nome encontrado com o id: " . $clienteId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o nome do cliente: " . $e->getMessage();
        }

        return $nome;
    }

    // Obtém o telefone do cliente pelo ID
    public function getTelefone($clienteId) {
        $sql = "SELECT telefone FROM clientes WHERE clienteid = :clienteid";
        $telefone = "";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['clienteid' => $clienteId]);
            $telefone = $stmt->fetchColumn();

            if ($telefone === false) {
                echo "Nenhum telefone encontrado com o id: " . $clienteId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o telefone do cliente: " . $e->getMessage();
        }

        return $telefone;
    }

    // Obtém o email do cliente pelo ID
    public function getEmail($clienteId) {
        $sql = "SELECT email FROM clientes WHERE clienteid = :clienteid";
        $email = "";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['clienteid' => $clienteId]);
            $email = $stmt->fetchColumn();

            if ($email === false) {
                echo "Nenhum email encontrado com o id: " . $clienteId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o email do cliente: " . $e->getMessage();
        }

        return $email;
    }

    // Obtém o endereço do cliente pelo ID
    public function getEndereco($clienteId) {
        $sql = "SELECT endereco FROM clientes WHERE clienteid = :clienteid";
        $endereco = "";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['clienteid' => $clienteId]);
            $endereco = $stmt->fetchColumn();

            if ($endereco === false) {
                echo "Nenhum endereço encontrado com o id: " . $clienteId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o endereço do cliente: " . $e->getMessage();
        }

        return $endereco;
    }

    // Obtém o número do cliente pelo ID
    public function getNumeroCliente($clienteId) {
        $sql = "SELECT numero_cliente FROM clientes WHERE clienteid = :clienteid";
        $numeroCliente = 0;

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['clienteid' => $clienteId]);
            $numeroCliente = $stmt->fetchColumn();

            if ($numeroCliente === false) {
                echo "Nenhum número de cliente encontrado com o id: " . $clienteId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o número de cliente: " . $e->getMessage();
        }

        return $numeroCliente;
    }

    // Atualiza o nome do cliente
    public function setNome($clienteId, $novoNome) {
        $sql = "UPDATE clientes SET nome = :nome WHERE clienteid = :clienteid";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['nome' => $novoNome, 'clienteid' => $clienteId]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    // Atualiza o telefone do cliente
    public function setTelefone($clienteId, $novoTelefone) {
        $sql = "UPDATE clientes SET telefone = :telefone WHERE clienteid = :clienteid";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['telefone' => $novoTelefone, 'clienteid' => $clienteId]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    // Atualiza o email do cliente
    public function setEmail($clienteId, $novoEmail) {
        $sql = "UPDATE clientes SET email = :email WHERE clienteid = :clienteid";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['email' => $novoEmail, 'clienteid' => $clienteId]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    // Atualiza o endereço do cliente
    public function setEndereco($clienteId, $novoEndereco) {
        $sql = "UPDATE clientes SET endereco = :endereco WHERE clienteid = :clienteid";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['endereco' => $novoEndereco, 'clienteid' => $clienteId]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    // Atualiza o número do cliente
    public function setNumeroCliente($clienteId, $novoNumeroCliente) {
        $sql = "UPDATE clientes SET numero_cliente = :numero_cliente WHERE clienteid = :clienteid";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['numero_cliente' => $novoNumeroCliente, 'clienteid' => $clienteId]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    // Retorna a lista de clientes
    public function getClientes() {
        $minhaLista = [];

        try {
            $sql = "SELECT * FROM clientes";
            $stmt = $this->pdo->query($sql);

            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                $nome = $row['nome'];
                $telefone = $row['telefone'];
                $email = $row['email'];
                $numeroCliente = $row['numero_cliente'];
                $endereco = $row['endereco'];
                $cliente = new Cliente($nome, $telefone, $email, $numeroCliente, $endereco); // Assumindo que a classe Cliente já existe
                $minhaLista[] = $cliente;
            }
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }

        return $minhaLista;
    }

    // Adiciona um cliente
    public function addCliente($nome, $telefone, $email, $numeroCliente, $endereco) {
        $sql = "INSERT INTO clientes (nome, telefone, email, numero_cliente, endereco) VALUES (:nome, :telefone, :email, :numero_cliente, :endereco)";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute([
                'nome' => $nome,
                'telefone' => $telefone,
                'email' => $email,
                'numero_cliente' => $numeroCliente,
                'endereco' => $endereco
            ]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    // Exclui um cliente
    public function delCliente($clienteId) {
        $sql = "DELETE FROM clientes WHERE clienteid = :clienteid";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['clienteid' => $clienteId]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }
}
?>