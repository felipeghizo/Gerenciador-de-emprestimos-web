from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    show_error = False
    if request.method == 'POST':
        banco = request.form.get('Banco_connect')
        ip = request.form.get('IP_connect')
        senha = request.form.get('Senha_connect')
        print(banco, ip, senha)
        if connect_to_db(banco, ip, senha):  
            return redirect(url_for('envios'))
        else:
            show_error = True
            return render_template('index.html', show_error=show_error)
    return render_template('index.html', show_error=show_error)

@app.route('/envios')
def envios():
    return render_template('Envios.html')  

@app.route('/cameras')
def cameras():
    return render_template('Cameras.html')  

@app.route('/clientes')
def clientes():
    return render_template('Clientes.html')  

@app.route('/historico')
def historico():
    return render_template('Historico.html')  

def connect_to_db(banco, ip, senha):
        # Configurações do banco de dados
    db_config = {
        'user': 'seu_usuario',
        'password': senha,
        'host': ip,
        'database': banco
    }
    if banco == "envios" and ip == "10.100.68.253" and senha=="Camerasip135.":
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
            return True

        except mysql.connector.Error as err:
            return f"Erro: {err}"
    else:
        return False
    
if __name__ == '__main__':
    app.run(debug=True)
