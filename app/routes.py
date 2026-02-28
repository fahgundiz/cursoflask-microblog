from app import app
from flask import render_template

#Definindo endereço no navegador
@app.route('/')
@app.route('/index')

def index():
    nome = "Gabriel"
    dados = {"profissao":"Programador", "canal":"Fahgundiz Dev"}
    return render_template('index.html', nome = nome, dados = dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')