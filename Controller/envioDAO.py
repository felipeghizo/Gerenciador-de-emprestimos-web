from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
from conexaoDAO import ConexaoDAO


conexao = ConexaoDAO()

class EnvioDAO:

    def add_envio_DAO(cliente, camera, numero_pedido, sequencia, status):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                query = "INSERT INTO envios (clienteid, cameraid, numero_pedido, sequencia, status) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (cliente, camera, numero_pedido, sequencia, status))
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for('envios'))
            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                return "Erro ao adicionar cliente", 500
        else:
            return "Erro na conexão com o banco de dados", 500
        
    def edit_envio_DAO(envioid, editNumero_pedido, editSequencia, editStatus):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                query = """
                    UPDATE envios
                    SET  numero_pedido = %s, sequencia = %s, status = %s 
                    WHERE envioid = %s
                """
                cursor.execute(query, (editNumero_pedido, editSequencia, editStatus, envioid))
                conn.commit()
                cursor.close()
                conn.close()
                return redirect(url_for('envios'))
            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                return "Erro ao editar envio", 500
        else:
            return "Erro na conexão com o banco de dados", 500

    def delete_envio_DAO(envio_id):
        if conexao.connect_to_db():
            db_config = conexao.get_db_config()
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                
                # Excluir a câmera
                delete_cliente_query = "DELETE FROM envios WHERE envioid = %s"
                cursor.execute(delete_cliente_query, (envio_id,))
                
                conn.commit()
                cursor.close()
                conn.close()
                return '', 204
            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                return "Erro ao excluir envio", 500
        else:
            return "Erro na conexão com o banco de dados", 500