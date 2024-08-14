from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    # Configurações do banco de dados
    db_config = {
        'user': 'seu_usuario',
        'password': 'sua_senha',
        'host': '10.100.68.253',
        'database': 'envio'
    }

    try:
        # Conectar ao banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Consulta SQL
        query = "SELECT clienteid, cameraid, acesso FROM envios"
        cursor.execute(query)

        # Buscar todos os resultados
        results = cursor.fetchall()

        # Fechar a conexão
        cursor.close()
        conn.close()

        # Renderizar a página HTML com os dados
        return render_template('envios.html', envios=results)

    except mysql.connector.Error as err:
        return f"Erro: {err}"

if __name__ == "__main__":
    app.run(debug=True)
