from flask import Flask, render_template
from database import banco, connection_tables, aluno, turma, escola, gestor
import database.professor as prof
import database.coordenador as coor

app = Flask(__name__)

banco.create_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_aluno')
def cadastro_aluno():
    esc = escola.Escola(6999, 'IFCE Campus Crato', 'Crato', 'CE')
    al = aluno.Aluno(0, 'Matheus Soares do Nascimento', '12345678', '02/10/2004', '2024')
    aluno.create(al, esc)

    print('Aluno adicionado')
