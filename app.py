from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        banco = request.form.get('Banco_connect')
        ip = request.form.get('IP_connect')
        senha = request.form.get('Senha_connect')
        
        # Aqui você faria a lógica de conexão com o banco de dados
        if connect_to_db(banco, ip, senha):  # Supondo que essa função verifique a conexão
            return redirect(url_for('envios'))
        else:
            return "Falha na conexão."
    return render_template('index.html')

@app.route('/envios')
def envios():
    return render_template('Envios.html')  

@app.route('/cameras')
def envios():
    return render_template('Cameras.html')  

@app.route('/clientes')
def envios():
    return render_template('Clientes.html')  

@app.route('/historico')
def envios():
    return render_template('Historico.html')  

def connect_to_db(banco, ip, senha):

    return True

if __name__ == '__main__':
    app.run(debug=True)
