<?php

require_once 'CameraDAO.php'; // Certifique-se de que o caminho está correto

class Camera {

    private $modelo;
    private $MAC;
    private $cameraDAO;

    // Construtor Default
    public function __construct($modelo = "", $MAC = "") {
        $this->modelo = $modelo;
        $this->MAC = $MAC;
        $this->cameraDAO = new CameraDAO();
    }
    
    // Gets
    public function getCameraid($modelo, $MAC) {
        return $this->cameraDAO->getCameraidDAO($modelo, $MAC);
    }
    
    public function getModelo() {
        return $this->cameraDAO->getModeloDAO($this->getCameraid($this->modelo, $this->MAC));
    }
    
    public function getModeloID($ID) {
        return $this->cameraDAO->getModeloDAO($ID);
    }
    
    public function getMAC() {
        return $this->cameraDAO->getMACDAO($this->getCameraid($this->modelo, $this->MAC));
    }
    
    public function getMACID($ID) {
        return $this->cameraDAO->getMACDAO($ID);
    }
    
    // Get lista de câmeras
    public function getCameras() {
        return $this->cameraDAO->getCamerasDAO();
    }

    // Sets
    public function setMAC($MAC) {
        $auxMAC = $this->MAC;
        $this->MAC = $MAC;
        $this->cameraDAO->setMACDAO($this->getCameraid($this->modelo, $auxMAC), $this->MAC);
    }
    
    public function setMACID($ID, $MAC) {
        $this->MAC = $MAC;
        $this->cameraDAO->setMACDAO($ID, $this->MAC);
    }
    
    public function setModelo($modelo) {
        $auxModelo = $this->modelo;
        $this->modelo = $modelo;
        $this->cameraDAO->setModeloDAO($this->getCameraid($auxModelo, $this->MAC), $this->modelo);
    }
    
    public function setModeloID($ID, $modelo) {
        $this->modelo = $modelo;
        $this->cameraDAO->setModeloDAO($ID, $this->modelo);
    }
    
    // Adiciona camera ao banco de dados
    public function addCamera() {
        $this->cameraDAO->addCameraDAO($this->modelo, $this->MAC);
    }
    
    // Deleta camera do banco de dados
    public function delCamera($modelo, $MAC) {
        $this->cameraDAO->delCameraDAO($this->getCameraid($modelo, $MAC));
    }
    
    public function delCameraID($ID) {
        $this->cameraDAO->delCameraDAO($ID);
    }
}
?>