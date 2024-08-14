import mysql.connector
from mysql.connector import Error

class CameraDAO:
    # Aqui você deve implementar todos os métodos de acesso ao banco de dados como no PHP.
    # Para o exemplo, vamos supor que esses métodos já estão implementados.

    def get_camera_id_dao(self, modelo, mac):
        # Implemente a lógica para obter o ID da câmera
        pass

    def get_modelo_dao(self, camera_id):
        # Implemente a lógica para obter o modelo da câmera
        pass

    def get_mac_dao(self, camera_id):
        # Implemente a lógica para obter o MAC da câmera
        pass

    def get_cameras_dao(self):
        # Implemente a lógica para obter a lista de câmeras
        pass

    def set_mac_dao(self, camera_id, mac):
        # Implemente a lógica para atualizar o MAC da câmera
        pass

    def set_modelo_dao(self, camera_id, modelo):
        # Implemente a lógica para atualizar o modelo da câmera
        pass

    def add_camera_dao(self, modelo, mac):
        # Implemente a lógica para adicionar uma nova câmera
        pass

    def del_camera_dao(self, camera_id):
        # Implemente a lógica para deletar uma câmera
        pass

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

    def add_camera(self):
        self.camera_dao.add_camera_dao(self.modelo, self.mac)

    def del_camera(self, modelo, mac):
        camera_id = self.get_camera_id(modelo, mac)
        self.camera_dao.del_camera_dao(camera_id)

    def del_camera_id(self, camera_id):
        self.camera_dao.del_camera_dao(camera_id)
