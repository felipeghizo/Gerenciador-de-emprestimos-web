<?php

// Importa a classe de conexão
require_once 'Conexao.php';  // Certifique-se de que o caminho está correto

class EnvioDAO {

    private $conexao;

    public function __construct() {
        $this->conexao = new Conexao();  // Conecta ao banco de dados
    }

    // gets
    public function getEnvioId($clienteId, $cameraId) {
        $sql = "SELECT COUNT(*) AS total FROM envios WHERE clienteid = :clienteid AND cameraid = :cameraid";
        $envioId = 0;

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':clienteid', $clienteId, PDO::PARAM_INT);
            $stmt->bindParam(':cameraid', $cameraId, PDO::PARAM_INT);
            $stmt->execute();
            
            $totalFerramentas = $stmt->fetchColumn();
            if ($totalFerramentas > 0) {
                $sql = "SELECT envioid FROM envios WHERE clienteid = :clienteid AND cameraid = :cameraid";
                $stmt = $conn->prepare($sql);
                $stmt->bindParam(':clienteid', $clienteId, PDO::PARAM_INT);
                $stmt->bindParam(':cameraid', $cameraId, PDO::PARAM_INT);
                $stmt->execute();

                $row = $stmt->fetch(PDO::FETCH_ASSOC);
                if ($row) {
                    $envioId = $row['envioid'];
                }
            } else {
                return -1;
            }
        } catch (PDOException $e) {
            echo "Erro ao procurar envioid: " . $e->getMessage();
        }
        return $envioId;
    }

    public function getClienteId($envioId) {
        $sql = "SELECT clienteid FROM envios WHERE envioid = :envioid";
        $clienteId = 0;

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':envioid', $envioId, PDO::PARAM_INT);
            $stmt->execute();
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($row) {
                $clienteId = $row['clienteid'];
            } else {
                echo "Nenhum clienteid encontrado com o id: " . $envioId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o clienteid do envio: " . $e->getMessage();
        }
        return $clienteId;
    }

    public function getCameraId($envioId) {
        $sql = "SELECT cameraid FROM envios WHERE envioid = :envioid";
        $cameraId = 0;

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':envioid', $envioId, PDO::PARAM_INT);
            $stmt->execute();
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($row) {
                $cameraId = $row['cameraid'];
            } else {
                echo "Nenhum cameraid encontrado com o id: " . $envioId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o cameraid do envio: " . $e->getMessage();
        }
        return $cameraId;
    }

    public function getAcesso($envioId) {
        $sql = "SELECT acesso FROM envios WHERE envioid = :envioid";
        $acesso = "";

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':envioid', $envioId, PDO::PARAM_INT);
            $stmt->execute();
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($row) {
                $acesso = $row['acesso'];
            } else {
                echo "Nenhum acesso encontrado com o id: " . $envioId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o acesso do envio: " . $e->getMessage();
        }
        return $acesso;
    }

    public function getDataEntrega($envioId) {
        $sql = "SELECT data_entrega FROM envios WHERE envioid = :envioid";
        $dataEntrega = "";

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':envioid', $envioId, PDO::PARAM_INT);
            $stmt->execute();
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($row) {
                $dataEntrega = $row['data_entrega'];
            } else {
                echo "Nenhuma data_entrega encontrada com o id: " . $envioId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar a data_entrega do envio: " . $e->getMessage();
        }
        return $dataEntrega;
    }

    public function getDataEnvio($envioId) {
        $sql = "SELECT data_envio FROM envios WHERE envioid = :envioid";
        $dataEnvio = "";

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':envioid', $envioId, PDO::PARAM_INT);
            $stmt->execute();
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($row) {
                $dataEnvio = $row['data_envio'];
            } else {
                echo "Nenhuma data_envio encontrada com o id: " . $envioId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar a data_envio do envio: " . $e->getMessage();
        }
        return $dataEnvio;
    }

    public function getDataInstalacao($envioId) {
        $sql = "SELECT data_instalacao FROM envios WHERE envioid = :envioid";
        $dataInstalacao = "";

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':envioid', $envioId, PDO::PARAM_INT);
            $stmt->execute();
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($row) {
                $dataInstalacao = $row['data_instalacao'];
            } else {
                echo "Nenhuma data_instalacao encontrada com o id: " . $envioId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar a data_instalacao do envio: " . $e->getMessage();
        }
        return $dataInstalacao;
    }

    public function getNotaFiscal($envioId) {
        $sql = "SELECT nota_fiscal FROM envios WHERE envioid = :envioid";
        $notaFiscal = 0;

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':envioid', $envioId, PDO::PARAM_INT);
            $stmt->execute();
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($row) {
                $notaFiscal = $row['nota_fiscal'];
            } else {
                echo "Nenhuma nota_fiscal encontrada com o id: " . $envioId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar a nota_fiscal do envio: " . $e->getMessage();
        }
        return $notaFiscal;
    }

    public function getSequencia($envioId) {
        $sql = "SELECT sequencia FROM envios WHERE envioid = :envioid";
        $sequencia = 0;

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':envioid', $envioId, PDO::PARAM_INT);
            $stmt->execute();
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($row) {
                $sequencia = $row['sequencia'];
            } else {
                echo "Nenhuma sequencia encontrada com o id: " . $envioId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar a sequencia do envio: " . $e->getMessage();
        }
        return $sequencia;
    }

    public function getNumeroPedido($envioId) {
        $sql = "SELECT numero_pedido FROM envios WHERE envioid = :envioid";
        $numeroPedido = 0;

        try {
            $conn = $this->conexao->getConexao();
            $stmt = $conn->prepare($sql);
            $stmt->bindParam(':envioid', $envioId, PDO::PARAM_INT);
            $stmt->execute();
            
            $row = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($row) {
                $numeroPedido = $row['numero_pedido'];
            } else {
                echo "Nenhum numero_pedido encontrado com o id: " . $envioId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o numero_pedido do envio: " . $e->getMessage();
        }
        return $numeroPedido;
    }
}

?>