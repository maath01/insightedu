from flask import Flask, render_template, request, session, flash, redirect, url_for
from database import aluno, banco, connection_tables, turma, escola, gestor
import database.professor as prof
import database.coordenador as coor
import sqlite3

app = Flask(__name__)
app.secret_key = 'insightedu'


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
    return render_template('home_aluno.html')

@app.route('/home_professor')
def home_professor():
    return render_template('home_professor.html')

@app.route('/home_coordenador')
def home_coordenador():
    return render_template('home_coordenador.html')

@app.route('/login_geral', methods=['GET', 'POST'])
def login_geral():
    if request.method == 'POST':
        categoria = request.form['categoria']
        nome = request.form['nome']
        senha = request.form['senha']

        tabela = ''
        if categoria == 'aluno':
            tabela = 'alunos'
        elif categoria == 'professor':
            tabela = 'professores'
        elif categoria == 'coordenador':
            tabela = 'coordenadores'

        connection = sqlite3.connect('database/banco.db')
        cursor = connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM {tabela} WHERE nome = ? AND senha = ?", (nome, senha))
            user = cursor.fetchone()

            if user:

                if categoria == 'aluno':
                    session['usuario_logado'] = request.form['nome']
                    flash(f"Aluno(a) {request.form['nome']} foi logado(a) com sucesso!")
                    return redirect(url_for('home_aluno'))
                  
                elif categoria == 'professor':
                      session['usuario_logado'] = request.form['nome']
                      flash(f"Professor(a) {request.form['nome']} foi logado(a) com sucesso!")
                      return redirect(url_for('home_professor'))
                
                elif categoria == 'coordenador':
                     session['usuario_logado'] = request.form['nome']
                     flash(f"coordenador(a) {request.form['nome']} foi logado(a) com sucesso!")
                     return redirect(url_for('home_coordenador'))
                
            else:
                flash('Não logado, tente novamente!')
                return render_template('login_geral.html')
            
        finally:
            connection.close()

    return render_template('login_geral.html')
if __name__ == '__main__':
    app.run(debug=True)
