from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import sqlite3
from mysql.connector import Error
from Controller.conexaoDAO import ConexaoDAO


conexao = ConexaoDAO()

class EnvioDAO:

    ''' GETS '''
    def getClienteidDAO(self, envioid):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try: 
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor(dictionary=True)
                sql = "SELECT clienteid FROM envios WHERE envioid = %s"
                cursor.execute(sql, (envioid,))
                cliente_id = cursor.fetchone()
                cursor.close()
                conn.close()
                return cliente_id
            except mysql.connector.Error as e:
                print(f"Erro ao buscar o id do cliente do envio: {e}")
                return ""
            
    def getCameraidDAO(self, envioid):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try: 
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor(dictionary=True)
                sql = "SELECT cameraid FROM envios WHERE envioid = %s"
                cursor.execute(sql, (envioid,))
                camera_id = cursor.fetchone()
                cursor.close()
                conn.close()
                return camera_id
            except mysql.connector.Error as e:
                print(f"Erro ao buscar o id da camera do envio: {e}")
                return ""
            
    def getAcessoDAO(self, envioid):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try: 
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor(dictionary=True)
                sql = "SELECT acesso FROM envios WHERE envioid = %s"
                cursor.execute(sql, (envioid,))
                acesso = cursor.fetchone()
                cursor.close()
                conn.close()
                return acesso
            except mysql.connector.Error as e:
                print(f"Erro ao buscar o acesso da camera do envio: {e}")
                return ""
                
    def getNotaFiscalDAO(self, envioid):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try: 
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor(dictionary=True)
                sql = "SELECT nota_fiscal FROM envios WHERE envioid = %s"
                cursor.execute(sql, (envioid,))
                nota_fiscal = cursor.fetchone()
                cursor.close()
                conn.close()
                return nota_fiscal
            except mysql.connector.Error as e:
                print(f"Erro ao buscar a nota fiscal do envio: {e}")

    def getSequenciaDAO(self, envioid):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try: 
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor(dictionary=True)
                sql = "SELECT sequencia FROM envios WHERE envioid = %s"
                cursor.execute(sql, (envioid,))
                sequencia = cursor.fetchone()
                cursor.close()
                conn.close()
                return sequencia
            except mysql.connector.Error as e:
                print(f"Erro ao buscar a sequencia do envio: {e}")

    def getNumeroPedidoDAO(self, envioid):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try: 
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor(dictionary=True)
                sql = "SELECT numero_pedido FROM envios WHERE envioid = %s"
                cursor.execute(sql, (envioid,))
                numero_pedido = cursor.fetchone()
                cursor.close()
                conn.close()
                return numero_pedido
            except mysql.connector.Error as e:
                print(f"Erro ao buscar o numero do pedido do envio: {e}")

    def getStatusDAO(self, envioid):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try: 
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor(dictionary=True)
                sql = "SELECT status FROM envios WHERE envioid = %s"
                cursor.execute(sql, (envioid,))
                status = cursor.fetchone()
                cursor.close()
                conn.close()
                return status
            except mysql.connector.Error as e:
                print(f"Erro ao buscar o status do pedido do envio: {e}")

    ''' SETS '''
    def setClienteidDAO(self, novo_cliente, envioid):
        sql = "UPDATE envios SET clienteid = ? WHERE envioid = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_cliente, envioid))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def setCameraidDAO(self, nova_camera, envioid):
        sql = "UPDATE envios SET cameraid = ? WHERE envioid = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (nova_camera, envioid))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def setAcessoDAO(self, novo_acesso, envioid):
        sql = "UPDATE envios SET acesso = ? WHERE envioid = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_acesso, envioid))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def setNotaFiscalDAO(self, nova_notaFiscal, envioid):
        sql = "UPDATE envios SET nota_fiscal = ? WHERE envioid = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (nova_notaFiscal, envioid))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def setSequenciaDAO(self, nova_sequencia, envioid):
        sql = "UPDATE envios SET seuqencia = ? WHERE envioid = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (nova_sequencia, envioid))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def setNumeroPedidoDAO(self, novo_numeroPedido, envioid):
        sql = "UPDATE envios SET numero_pedido = ? WHERE envioid = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_numeroPedido, envioid))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    def setStatusDAO(self, novo_status, envioid):
        sql = "UPDATE envios SET status = ? WHERE envioid = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, (novo_status, envioid))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro: {e}")

    ''' CRUD '''
    def addEnvioDAO(self, clienteid, cameraid, nota_fiscal, sequencia, numero_pedido):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                query = "INSERT INTO envios (clienteid, cameraid, nota_fiscal, numero_pedido, sequencia, status) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (clienteid, cameraid, nota_fiscal, sequencia, numero_pedido, "Ativo"))
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for('envios'))
            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                return "Erro ao adicionar envio", 500
        else:
            return "Erro na conexão com o banco de dados", 500
        
    def visualizarDadosDAO(self):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                sql = "SELCET * FROM envios"
                cursor.execute(sql)
                sequencia = cursor.fetchone()
                cursor.close()
                conn.close()
                return sequencia
            except mysql.connector.Error as e:
                print(f"Erro ao buscar dados de envios: {e}")
        else:
            return "Erro na conexão com o banco de dados", 500
        
    ''' def editEnvioDAO(envioid, clienteid, cameraid, acesso, nota_fiscal, sequencia, numero_pedido, status):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                query = """
                    UPDATE envios
                    SET  clienteid = ?,
                         cameraid = ?,
                         acesso = ?,
                         nota_fiscal = ?, 
                         sequencia = ?, 
                         numero_pedido = ?,
                         status = ? 
                    WHERE envioid = ?
                """
                cursor.execute(query, (clienteid, cameraid, acesso, nota_fiscal, sequencia, numero_pedido, status, envioid))
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for('envios'))
            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                return "Erro ao editar envio", 500
        else:
            return "Erro na conexão com o banco de dados", 500'''

    