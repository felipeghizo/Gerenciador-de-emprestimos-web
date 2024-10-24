from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from Model.cliente import Cliente 
from Model.camera import Camera 

# Muda o diretório de templates para 'view'
app = Flask(__name__, template_folder='View', static_folder='View/Style')

cliente = Cliente()
camera = Camera()

def get_db_config():
    return {
        'user': "root",
        'password': "Camerasip135.",
        'host': "10.100.68.253",
        'database': "envio"
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    show_error = False
    if request.method == 'GET':
        if connect_to_db():  
            return redirect(url_for('cameras'))
        else:
            show_error = True
            return render_template('cameras.html', show_error=show_error)
    return render_template('cameras.html', show_error=show_error)

@app.route('/envios', methods=['GET', 'POST'])
def envios():
    results = None
    if connect_to_db():
        envios_data = fetch_envios_data()
        cameras_envioativo_data = fetch_cameras_enviosAtivos_data()
        clientes_envioativo_data = fetch_clientes_enviosAtivos_data()
            
        results = {
            'envios': envios_data,
            'cameras': cameras_envioativo_data,
            'clientes': clientes_envioativo_data
        }
        return render_template('envios.html', **results)
    else:
        return "Erro na conexão com o banco de dados"

@app.route('/cameras')
def cameras():
    results = None
    if connect_to_db():
        results = fetch_cameras_data()
        return render_template('Cameras.html', cameras=results)
    else:
        return "Erro na conexão com o banco de dados"

@app.route('/clientes')
def clientes():
    results = None
    if connect_to_db():
        results = fetch_clientes_data()
        return render_template('Clientes.html', clientes=results)
    else:
        return "Erro na conexão com o banco de dados"

@app.route('/historico')
def historico():
    return render_template('Historico.html')

def connect_to_db():
    db_config = get_db_config()
    try: 
        conn = mysql.connector.connect(**db_config)
        conn.close()
        return True
    except mysql.connector.Error as err:
        print(err)
        return False

def fetch_envios_data():
    db_config = get_db_config()
    try: 
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT clienteid, cameraid, status FROM envios"
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

def fetch_clientes_data():
    db_config = get_db_config()
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

def fetch_clientes_enviosAtivos_data():
    db_config = get_db_config()
    try: 
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT c.clienteid, c.nome, c.telefone, c.numero_cliente, c.endereco, c.email 
            FROM clientes c
            LEFT JOIN envios e ON c.clienteid = e.clienteid
            WHERE e.clienteid IS NULL
        """
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()

        return results
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return []

def fetch_cameras_data():
    db_config = get_db_config()
    try: 
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT cameraid, modelo, Cloud, MAC FROM cameras"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return []
        
def fetch_cameras_enviosAtivos_data():
    db_config = get_db_config()
    try: 
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT cam.cameraid, cam.modelo, cam.Cloud 
            FROM cameras cam
            LEFT JOIN envios e ON cam.cameraid = e.cameraid
            WHERE e.cameraid IS NULL
        """
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
    endereco = request.form.get('add_endereco')
    email = request.form.get('add_email')
    
    if connect_to_db():
        db_config = get_db_config()
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "INSERT INTO clientes (nome, telefone, numero_cliente, endereco, email) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (nome, telefone, numero_cliente, endereco, email))
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
    endereco = request.form.get('edit_endereco')
    email = request.form.get('edit_email')

    if connect_to_db():
        db_config = get_db_config()
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = """
                UPDATE clientes
                SET nome = %s, telefone = %s, numero_cliente = %s, endereco = %s, email = %s
                WHERE clienteid = %s
            """
            cursor.execute(query, (nome, telefone, numero_cliente, endereco, email, clienteid))
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

    if connect_to_db():
        db_config = get_db_config()
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
    db_config = get_db_config()
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

    if connect_to_db():
        db_config = get_db_config()
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

    if connect_to_db():
        db_config = get_db_config()
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

    if connect_to_db():
        db_config = get_db_config()
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

def camera_tem_envios(cameraid):
    db_config = get_db_config()
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Verifica se há envios associados à câmera
        query2 = "SELECT COUNT(*) FROM envios WHERE cameraid = %s"
        cursor.execute(query2, (cameraid,))
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return count > 0

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False

# CRUD Envios
@app.route('/add_InfoEnvio', methods=['POST'])
def add_InfoEnvio():
    cliente = request.form.get('addInfo_clienteid')
    camera = request.form.get('addInfo_camid')
    numero_pedido = request.form.get('numero_pedido')
    sequencia = request.form.get('sequencia')
    status = request.form.get('addInfo_status')
    
    if connect_to_db():
        db_config = get_db_config()
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
