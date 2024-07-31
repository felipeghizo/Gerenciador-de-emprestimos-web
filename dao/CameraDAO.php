<?php

class CameraDAO {
    private $pdo;
    
    public function __construct($pdo) {
        $this->pdo = $pdo;
    }
    
    // Obtém o ID da câmera
    public function getCameraId($modeloEditar, $MACEditar) {
        $sql = "SELECT COUNT(*) AS total FROM cameras WHERE modelo = :modelo AND MAC = :MAC";
        $cameraId = 0;

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['modelo' => $modeloEditar, 'MAC' => $MACEditar]);

            $totalFerramentas = $stmt->fetchColumn();
            if ($totalFerramentas > 0) {
                $sql = "SELECT cameraid FROM cameras WHERE modelo = :modelo AND MAC = :MAC";
                $stmt2 = $this->pdo->prepare($sql);
                $stmt2->execute(['modelo' => $modeloEditar, 'MAC' => $MACEditar]);
                $cameraId = $stmt2->fetchColumn();
            } else {
                return -1;
            }
        } catch (PDOException $e) {
            echo "Erro ao procurar câmera: " . $e->getMessage();
        }

        return $cameraId;
    }

    // Obtém o modelo da câmera pelo ID
    public function getModelo($cameraId) {
        $sql = "SELECT modelo FROM cameras WHERE cameraid = :cameraid";
        $modelo = "";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['cameraid' => $cameraId]);
            $modelo = $stmt->fetchColumn();

            if ($modelo === false) {
                echo "Nenhum modelo encontrado com o id: " . $cameraId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o modelo da câmera: " . $e->getMessage();
        }

        return $modelo;
    }

    // Obtém o MAC da câmera pelo ID
    public function getMAC($cameraId) {
        $sql = "SELECT MAC FROM cameras WHERE cameraid = :cameraid";
        $MAC = "";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['cameraid' => $cameraId]);
            $MAC = $stmt->fetchColumn();

            if ($MAC === false) {
                echo "Nenhum MAC encontrado com o id: " . $cameraId;
            }
        } catch (PDOException $e) {
            echo "Erro ao buscar o MAC da câmera: " . $e->getMessage();
        }

        return $MAC;
    }

    // Atualiza o modelo da câmera
    public function setModelo($cameraId, $novoModelo) {
        $sql = "UPDATE cameras SET modelo = :modelo WHERE cameraid = :cameraid";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['modelo' => $novoModelo, 'cameraid' => $cameraId]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    // Atualiza o MAC da câmera
    public function setMAC($cameraId, $novoMAC) {
        $sql = "UPDATE cameras SET MAC = :MAC WHERE cameraid = :cameraid";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['MAC' => $novoMAC, 'cameraid' => $cameraId]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    // Retorna a lista de câmeras
    public function getCameras() {
        $minhaLista = [];

        try {
            $sql = "SELECT * FROM cameras";
            $stmt = $this->pdo->query($sql);

            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                $nome = $row['modelo'];
                $MAC = $row['MAC'];
                $camera = new Camera($nome, $MAC); // Assumindo que a classe Camera já existe
                $minhaLista[] = $camera;
            }
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }

        return $minhaLista;
    }

    // Adiciona uma nova câmera
    public function addCamera($modelo, $MAC) {
        $sql = "INSERT INTO cameras (modelo, MAC) VALUES (:modelo, :MAC)";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['modelo' => $modelo, 'MAC' => $MAC]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }

    // Exclui uma câmera
    public function delCamera($cameraId) {
        $sql = "DELETE FROM cameras WHERE cameraid = :cameraid";

        try {
            $stmt = $this->pdo->prepare($sql);
            $stmt->execute(['cameraid' => $cameraId]);
        } catch (PDOException $e) {
            echo "Erro: " . $e->getMessage();
        }
    }
}

// Exemplo de uso
try {
    $pdo = new PDO("mysql:host=10.100.68.85;dbname=envio;charset=utf8", "root", "Camerasip135.");
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $cameraDAO = new CameraDAO($pdo);
    
    // Exemplo: adicionar uma nova câmera
    $cameraDAO->addCamera("Modelo X", "00:14:22:01:23:45");

    // Exemplo: obter a lista de câmeras
    $cameras = $cameraDAO->getCameras();
    foreach ($cameras as $camera) {
        echo "Modelo: " . $camera->getModelo() . ", MAC: " . $camera->getMAC() . "<br>";
    }
} catch (PDOException $e) {
    echo "Erro na conexão: " . $e->getMessage();
}

?>