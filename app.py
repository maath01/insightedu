from flask import Flask, render_template, request
from database import aluno, banco, connection_tables, turma, escola, gestor
import database.professor as prof
import database.coordenador as coor
import sqlite3

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


@app.route('/home_aluno', methods=['GET', 'POST'])
def home_aluno():
    return render_template('/home_aluno')



@app.route('/login_aluno', methods=['GET', 'POST'])
def login_aluno():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        connection = sqlite3.connect('database/banco.db')
        cursor = connection.cursor()

        try:
            cursor.execute('SELECT * FROM alunos WHERE nome = ? AND senha = ?', (nome, senha))
            user = cursor.fetchone()

            if user:
                return render_template('home_aluno.html', nome=user[1])
            else:
                return render_template('login_aluno.html', error='Usuário ou senha incorretos')
        finally:
            connection.close()

    return render_template('login_aluno.html')
if __name__ == '__main__':
    app.run(debug=True)
