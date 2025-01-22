from flask import Flask, render_template, request, session, flash, redirect, url_for
from database import aluno, banco, connection_tables, turma, escola, gestor, nota
from database.turma import list_classes_by_teacher, list_classes_by_coordinator, list_classes_by_school
import database.professor as prof
import database.coordenador as coor
import database.avaliacao as av
import sqlite3

app = Flask(__name__)
app.secret_key = 'insightedu'

banco.create_database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if session['user_type'] == 'aluno':
        return render_template('home_aluno.html')
    elif session['user_type'] == 'professor':
        return render_template('home_professor.html')
    elif session['user_type'] == 'coordenador':
        return render_template('home_coordenador.html')
    elif session['user_type'] == 'gestor':
        return render_template('home_gestor.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
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
        elif categoria == 'gestor':
            tabela = 'gestores'

        connection = sqlite3.connect('database/banco.db')
        cursor = connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM {tabela} WHERE nome = ? AND senha = ?", (nome, senha))
            user = cursor.fetchone()

            if user:
                session['usuario_logado'] = request.form['nome']
                if categoria == 'aluno':
                    session['user_type'] = 'aluno'
                    flash(f"Aluno(a) {request.form['nome']} foi logado(a) com sucesso!")                  
                elif categoria == 'professor':
                    session['user_type'] = 'professor'
                    flash(f"Professor(a) {request.form['nome']} foi logado(a) com sucesso!")
                elif categoria == 'coordenador':
                    session['user_type'] = 'coordenador'
                    flash(f"coordenador(a) {request.form['nome']} foi logado(a) com sucesso!")
                elif categoria == 'gestor':
                    session['user_type'] = 'gestor'
                    flash(f"gestor(a) {request.form['nome']} foi logado(a) com sucesso!")

                return redirect(url_for('home'))
                
                
            else:
                flash('Não logado, tente novamente!')
                return render_template('login.html')
            
        finally:
            connection.close()

    return render_template('login.html')

