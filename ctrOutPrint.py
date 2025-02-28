from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

#Rota pata testes
@app.route('/teste')
def tst():
    return 'testando'

#Rota para UPLOAD de notas de cartuchos
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']  # Obtém o objeto FileStorage

    return jsonify('Passou')# 200  # Retorna um dicionário serializável

#Rota para listar notas de cartuchos
@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Controle do Outsoursing')



app.run() # é possível fazer configurando host e porta da seguinte forma: app.run(host='0.0.0.0', port=8080)