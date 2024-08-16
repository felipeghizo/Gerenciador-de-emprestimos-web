from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from modelo.Cliente import Cliente 
from modelo.Camera import Camera 

cliente = Cliente()
camera = Camera()

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

@app.route('/envios', methods=['GET', 'POST'])
def envios():
    banco = "envio"
    ip = "10.100.68.253"
    senha = "Camerasip135."
    results = None
    if connect_to_db(banco, ip, senha):
        results = fetch_envios_data(banco, ip, senha)
        print(results)
        return render_template('Envios.html', envios=results)
    else:
        return "Erro na conexão com o banco de dadossss"

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
    db_config = {
        'user': 'root',
        'password': senha,
        'host': ip,
        'database': banco
    }
    if banco == "envio" and ip == "10.100.68.253" and senha == "Camerasip135.":
        try: 
            print("helo")
            conn = mysql.connector.connect(**db_config)
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(err)
            return False
    else:
        return False

def fetch_envios_data(banco, ip, senha):
    db_config = {
        'user': 'root',
        'password': senha,
        'host': ip,
        'database': banco
    }
    try: 
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT clienteid, cameraid, acesso FROM envios"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        # Atualizando o dicionário com o nome correspondente ao ID do cliente
        for obj in results:
            if 'clienteid' in obj:
                obj['clienteid'] = cliente.get_nome_id(obj['clienteid'])
            if 'cameraid' in obj:
                obj['cameraid'] = camera.get_modelo_id(obj['cameraid'])

        return results
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return []

if __name__ == '__main__':
    app.run(debug=True)
