import mysql.connector
from mysql.connector import Error
from Controller.cameraDAO import CameraDAO

class Camera:
    def __init__(self, modelo="", mac=""):
        self.modelo = modelo
        self.mac = mac
        self.camera_dao = CameraDAO()

    def get_camera_id(self, modelo, mac):
        return self.camera_dao.get_camera_id_dao(modelo, mac)

    def get_modelo(self):
        camera_id = self.get_camera_id(self.modelo, self.mac)
        return self.camera_dao.get_modelo_dao(camera_id)

    def get_modelo_id(self, camera_id):
        return self.camera_dao.get_modelo_dao(camera_id)

    def get_mac(self):
        camera_id = self.get_camera_id(self.modelo, self.mac)
        return self.camera_dao.get_mac_dao(camera_id)

    def get_mac_id(self, camera_id):
        return self.camera_dao.get_mac_dao(camera_id)

    def get_cameras(self):
        return self.camera_dao.get_cameras_dao()

    def set_mac(self, mac):
        aux_mac = self.mac
        self.mac = mac
        camera_id = self.get_camera_id(self.modelo, aux_mac)
        self.camera_dao.set_mac_dao(camera_id, self.mac)

    def set_mac_id(self, camera_id, mac):
        self.mac = mac
        self.camera_dao.set_mac_dao(camera_id, self.mac)

    def set_modelo(self, modelo):
        aux_modelo = self.modelo
        self.modelo = modelo
        camera_id = self.get_camera_id(aux_modelo, self.mac)
        self.camera_dao.set_modelo_dao(camera_id, self.modelo)

    def set_modelo_id(self, camera_id, modelo):
        self.modelo = modelo
        self.camera_dao.set_modelo_dao(camera_id, self.modelo)

    # Adiciona câmera
    def add_camera(self, modelo, cloud, mac):
        self.camera_dao.add_camera_DAP(self.modelo, self.mac)

    def del_camera(self, modelo, mac):
        camera_id = self.get_camera_id(modelo, mac)
        self.camera_dao.del_camera_dao(camera_id)

    def del_camera_id(self, camera_id):
        self.camera_dao.del_camera_dao(camera_id)
