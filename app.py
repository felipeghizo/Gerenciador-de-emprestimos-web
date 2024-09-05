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
        return render_template('Envios.html', envios=results)
    else:
        return "Erro na conexão com o banco de dados"

@app.route('/cameras')
def cameras():
    banco = "envio"
    ip = "10.100.68.253"
    senha = "Camerasip135."
    results = None
    if connect_to_db(banco, ip, senha):
        results = fetch_cameras_data(banco, ip, senha)
        return render_template('Cameras.html', cameras=results)
    else:
        return "Erro na conexão com o banco de dados"

@app.route('/clientes')
def clientes():
    banco = "envio"
    ip = "10.100.68.253"
    senha = "Camerasip135."
    results = None
    if connect_to_db(banco, ip, senha):
        results = fetch_clientes_data(banco, ip, senha)
        return render_template('Clientes.html', clientes=results)
    else:
        return "Erro na conexão com o banco de dados"

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
    
def fetch_clientes_data(banco, ip, senha):
    db_config = {
        'user': 'root',
        'password': senha,
        'host': ip,
        'database': banco
    }
    try: 
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT clienteid, nome, telefone, numero_cliente, endereco, email FROM clientes"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        return results
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return []

def fetch_cameras_data(banco, ip, senha):
    db_config = {
        'user': 'root',
        'password': senha,
        'host': ip,
        'database': banco
    }
    try: 
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT cameraid, modelo, MAC, Cloud FROM cameras"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        return results
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return []

# CRUD CLIENTE  
@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    nome = request.form.get('add_nome')
    numero_cliente = request.form.get('add_numero_cliente')
    telefone = request.form.get('add_telefone')
    
    banco = "envio"
    ip = "10.100.68.253"
    senha = "Camerasip135."

    if connect_to_db(banco, ip, senha):
        db_config = {
            'user': 'root',
            'password': senha,
            'host': ip,
            'database': banco
        }
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "INSERT INTO clientes (nome, telefone, numero_cliente) VALUES (%s, %s, %s)"
            cursor.execute(query, (nome, telefone, numero_cliente))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('clientes'))
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return "Erro ao adicionar cliente", 500
    else:
        return "Erro na conexão com o banco de dados", 500
    
@app.route('/edit_cliente', methods=['POST'])
def edit_cliente():
    nome = request.form.get('Nome')
    telefone = request.form.get('Numero_intelbras')
    numero_cliente = request.form.get('Telefone')
    clienteid = request.form.get('edit_id')
    print(clienteid)
    banco = "envio"
    ip = "10.100.68.253"
    senha = "Camerasip135."

    if connect_to_db(banco, ip, senha):
        db_config = {
            'user': 'root',
            'password': senha,
            'host': ip,
            'database': banco
        }
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = """
                UPDATE clientes
                SET nome = %s, telefone = %s, numero_cliente = %s
                WHERE clienteid = %s
            """
            cursor.execute(query, (nome, telefone, numero_cliente, clienteid))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('clientes'))
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return "Erro ao editar cliente", 500
    else:
        return "Erro na conexão com o banco de dados", 500

@app.route('/delete_cliente', methods=['POST'])
def delete_cliente():
    cliente_id = request.form.get('id')

    banco = "envio"
    ip = "10.100.68.253"
    senha = "Camerasip135."

    if connect_to_db(banco, ip, senha):
        db_config = {
            'user': 'root',
            'password': senha,
            'host': ip,
            'database': banco
        }
        try:
            if cliente_tem_envios(cliente_id):
                return "Não é possível excluir o cliente porque ele está associado a envios ativos.", 400

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            
            # Depois, excluir o cliente
            delete_cliente_query = "DELETE FROM clientes WHERE clienteid = %s"
            cursor.execute(delete_cliente_query, (cliente_id,))
            
            conn.commit()
            cursor.close()
            conn.close()
            return '', 204
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return "Erro ao excluir cliente", 500
    else:
        return "Erro na conexão com o banco de dados", 500

def cliente_tem_envios(numero_cliente):
    db_config = {
        'user': 'root',
        'password': 'Camerasip135.',
        'host': '10.100.68.253',
        'database': 'envio'
    }
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Verifica se o cliente existe e obtém o clienteid
        query1 = "SELECT clienteid FROM clientes WHERE numero_cliente = %s"
        cursor.execute(query1, (numero_cliente,))
        result = cursor.fetchone()
        
        if result:
            clienteid = result[0]
        else:
            # Se o cliente não for encontrado, retorna False
            cursor.close()
            conn.close()
            return False
        
        # Verifica se há envios associados ao cliente
        query2 = "SELECT COUNT(*) FROM envios WHERE clienteid = %s"
        cursor.execute(query2, (clienteid,))
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return count > 0

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False

# CRUD CAMERA
@app.route('/add_camera', methods=['POST'])
def add_camera():
    modelo = request.form.get('modelo')
    cloud = request.form.get('Cloud')
    mac = request.form.get('MAC')
    cam_id = request.form.get('cameraid')

    banco = "envio"
    ip = "10.100.68.253"
    senha = "Camerasip135."

    if connect_to_db(banco, ip, senha):
        db_config = {
            'user': 'root',
            'password': senha,
            'host': ip,
            'database': banco
        }
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "INSERT INTO cameras (modelo, Cloud, MAC) VALUES (%s, %s, %s)"
            cursor.execute(query, (modelo, cloud, mac))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('cameras'))
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return "Erro ao adicionar câmera", 500
    else:
        return "Erro na conexão com o banco de dados", 500

@app.route('/edit_camera', methods=['POST'])
def edit_camera():
    Modelo = request.form.get('Modelo')
    Cloud = request.form.get('Cloud')
    MAC = request.form.get('MAC')
    camid = request.form.get('edit_id')

    banco = "envio"
    ip = "10.100.68.253"
    senha = "Camerasip135."

    if connect_to_db(banco, ip, senha):
        db_config = {
            'user': 'root',
            'password': senha,
            'host': ip,
            'database': banco
        }
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = """
                UPDATE cameras
                SET Modelo = %s, Cloud = %s, MAC = %s 
                WHERE cameraid = %s
            """
            cursor.execute(query, (Modelo, Cloud, MAC, camid))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('cameras'))
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return "Erro ao editar cliente", 500
    else:
        return "Erro na conexão com o banco de dados", 500

@app.route('/delete_camera', methods=['POST'])
def delete_camera():
    camera_id = request.form.get('id')

    banco = "envio"
    ip = "10.100.68.253"
    senha = "Camerasip135."

    if connect_to_db(banco, ip, senha):
        db_config = {
            'user': 'root',
            'password': senha,
            'host': ip,
            'database': banco
        }
        try:
            if camera_tem_envios(camera_id):
                return "Não é possível excluir a câmera porque ela está associada a envios ativos.", 400

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            
            # Excluir a câmera
            delete_cliente_query = "DELETE FROM cameras WHERE cameraid = %s"
            cursor.execute(delete_cliente_query, (camera_id,))
            
            conn.commit()
            cursor.close()
            conn.close()
            return '', 204
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return "Erro ao excluir cliente", 500
    else:
        return "Erro na conexão com o banco de dados", 500

def cliente_tem_envios(numero_cliente):
    db_config = {
        'user': 'root',
        'password': 'Camerasip135.',
        'host': '10.100.68.253',
        'database': 'envio'
    }
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Verifica se o cliente existe e obtém o clienteid
        query1 = "SELECT clienteid FROM clientes WHERE numero_cliente = %s"
        cursor.execute(query1, (numero_cliente,))
        result = cursor.fetchone()
        
        if result:
            clienteid = result[0]
        else:
            # Se o cliente não for encontrado, retorna False
            cursor.close()
            conn.close()
            return False
        
        # Verifica se há envios associados ao cliente
        query2 = "SELECT COUNT(*) FROM envios WHERE clienteid = %s"
        cursor.execute(query2, (clienteid,))
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return count > 0

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False

def camera_tem_envios(cameraid):
    db_config = {
        'user': 'root',
        'password': 'Camerasip135.',
        'host': '10.100.68.253',
        'database': 'envio'
    }
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Verifica se há envios associados ao cliente
        query2 = "SELECT COUNT(*) FROM envios WHERE cameraid = %s"
        cursor.execute(query2, (cameraid,))
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return count > 0

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
