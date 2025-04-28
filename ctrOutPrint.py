from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
import _mysql_connector

class Toner:
    def __int__(self, codigo, descricao, nota, dataRecebimento, tipo):
        self.codigo= codigo
        self.descricao = descricao
        self.nota = nota
        self.dataRecebimento = dataRecebimento
        self.tipo = tipo

app = Flask(__name__)

#Configurando a conexão
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(

        SGBD="mysql+mysqlconnector",#Verifivar o motivo de não funcionar quando atribuído da variável .env
        usuario=os.getenv('USU_DB'),
        senha=os.getenv('PSW_DB'),
        servidor=os.getenv('SERVER'),
        database=os.getenv('DATABASE')

    )

#Atribuindo a aplicação so Sqlalchemy
db = SQLAlchemy(app)

#Atribuindo a chave do Gemini
CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")

#Rota pata HOME
@app.route('/')
def tst():
    return os.getenv('SYS_NAME') # implementar

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
    return render_template('lista.html', titulo='Controle do Outsoursing de Impressão')

if __name__ == '__main__':
    app.run(debug=True) # é possível fazer configurando host e porta da seguinte forma: app.run(host='0.0.0.0', port=8080)