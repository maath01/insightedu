from flask import Flask, render_template, request, session, flash, redirect, url_for
from database import aluno, banco, connection_tables, turma, escola, gestor, nota
from database.turma import list_classes_by_teacher, list_classes_by_coordinator, list_classes_by_school
from database.connection_tables import professores_turmas_materias
import database.professor as prof
import database.coordenador as coor
import database.avaliacao as av
import database.descritor_port as desc_p

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
        turmas = turma.list_classes_by_teacher(session['id'])
        return render_template('home_professor.html', turmas=turmas)

    elif session['user_type'] == 'coordenador':
        return render_template('home_coordenador.html')
    
    elif session['user_type'] == 'gestor':
        return render_template('home_gestor.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        categoria = request.form['categoria']
        user_id = request.form['id']
        nome = request.form['nome']
        senha = request.form['senha']

        user = banco.check_login(categoria, user_id, nome, senha)

        if user:
            session['usuario_logado'] = request.form['nome']
            session['id'] = user_id
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
        
    return render_template('login.html')


@app.route ('/turmas/<int:turma_id>')
def lista_alunos(turma_id):
    try:    
        alunos = aluno.list_students_by_class(turma_id)
        if alunos:
            return render_template('lista_alunos.html', turma=turma_id, alunos=alunos)
        else:
            return f"<h1>Não há alunos cadastrados na turma {turma_id}.</h1>"
    finally:
        pass


@app.route('/perfil_aluno/<int:aluno_id>')
def perfil_aluno(aluno_id):

    try:  
        student = aluno.get(aluno_id) 
        if student:
            return render_template('perfil_aluno.html', aluno=student)
        else:
            return render_template('erro.html', mensagem=f"Aluno com ID {aluno_id} não encontrado.")
    finally:
        pass


@app.route('/home/ferramentas')
def ferramentas():
    return render_template('ferramentas.html')


if __name__ == '__main__':
    app.run(debug=True)

