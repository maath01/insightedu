from flask import Flask, render_template, request, session, flash, redirect, url_for, Response
from io import BytesIO
import matplotlib.pyplot as plt
from database import aluno, banco, connection_tables, turma, escola, gestor, nota
from database.turma import list_classes_by_teacher, list_classes_by_coordinator, list_classes_by_school
from database.avaliacao import list_evaluations_by_teacher, get_matter
from database.aluno import list_students_by_class
from database.connection_tables import professores_turmas_materias
import database.professor as prof 
import database.coordenador as coor
import database.avaliacao as av
import sqlite3
from database.professor import list_teachers_by_school
from database.escola import get_school_id

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
        id = request.form['id']
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
            cursor.execute(f"SELECT * FROM {tabela} WHERE id = ? AND nome = ? AND senha = ?", (id, nome, senha))
            user = cursor.fetchone()

            if user:
                session['id'] = id
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

@app.route('/perfil_professor/<int:prof_id>')
def perfil_professor(prof_id):
    professor = prof.get(prof_id)
    if professor:
        return render_template('perfil_professor.html', professor=professor)
    else:
        return ("Erro") 


@app.route('/home/ferramentas/lista_professores')
def list_teachers():
    if session.get('user_type') == 'gestor':
        id_gestor=session.get('id')
        school_id = get_school_id(id_gestor)
        professores = prof.list_teachers_by_school(school_id)
        return render_template('lista_profs.html', professores=professores)
    else:
        return render_template('home.html')
    

@app.route('/home/ferramentas/avaliacoes')
def avaliacoes():
    if session.get('user_type') == 'professor':
        avaliacoes = av.list_evaluations_by_teacher(session['id'])
        return render_template('avaliacoes.html', avaliacoes=avaliacoes)
    else:
        return render_template('home.html')
    
@app.route('/home/ferramentas/avaliacoes/<int:av_id>')
def avaliacao(av_id):
    if session.get('user_type') == 'professor':
        avaliacao = av.get(av_id)
        alunos = list_students_by_class(avaliacao.turma_id)
        materia = get_matter(avaliacao)
        return render_template('avaliacao.html', avaliacao=avaliacao, alunos=alunos,materia=materia)
    else:
        return render_template('home.html')

@app.route('/home/ferramentas')
def ferramentas():
    if session['user_type'] == 'aluno':
        return render_template('ferramentas_aluno.html')
    elif session['user_type'] == 'professor':
        return render_template('ferramentas_prof.html')
    elif session['user_type'] == 'coordenador':
        return render_template('ferramentas_coordenador.html')
    elif session['user_type'] == 'gestor':
        return render_template('ferramentas_gestor.html')
    

@app.route('/logout', methods=['POST'])
def logout():
    session['nome'] = None
    redirect(url_for('login'))

#ainda não revisado
@app.route('/home/ferramentas/alunos/<int:school_id>')
def lista_alunos_por_escola(school_id):
    if session.get('user_type') != 'gestor':
        flash("Você não tem permissão para acessar esta página.")
        return redirect(url_for('home'))

    try:
        gestor_id = session('id')
        escola_id = get_school_id(session('id'))

        alunos = aluno.list_student_by_school(escola_id)

        return render_template('lista_alunos_por_escola.html', alunos=alunos, escola_id=escola_id)
    except Exception as e:
        flash("Ocorreu um erro ao listar os alunos. Por favor, tente novamente.")
        return redirect(url_for('home'))

@app.route('/cadastro/aluno', methods=['POST'])
def cadastro_aluno():
    if session.get('user_type') != 'gestor':
        flash("Você não tem permissão para acessar esta funcionalidade.")
        return redirect(url_for('home'))
        
    try:
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        ano_matricula = request.form['ano_matricula']
        cpf = request.form['cpf']
        idade = int(request.form['idade'])
        
        gestor_id = session.get('id')
        escola_id = get_school_id(gestor_id)
        esc = escola.get(escola_id)
        
        novo_aluno = aluno.Aluno(
            id=0,
            nome=nome,
            data_nascimento=data_nascimento,
            ano_matricula=ano_matricula,
            cpf=cpf,
            idade=idade
        )
        
        novo_aluno.create(esc)
        
        flash("Aluno cadastrado com sucesso!")
        return redirect(url_for('lista_alunos_por_escola', school_id=escola_id))
    
    except ValueError as e:
        flash(f"Erro nos dados fornecidos: {str(e)}")
        return redirect(url_for('home'))
    
    except Exception as e:
        flash("Ocorreu um erro ao cadastrar o aluno. Por favor, tente novamente.")
        return redirect(url_for('home'))


@app.route('/cadastro/turma', methods=['POST'])
def cadastro_turma():
    
    if 'user_type' not in session or session['user_type'] != 'professor':
        flash("Você não tem permissão para acessar esta funcionalidade.")
        return redirect(url_for('home'))
    
    try:
        serie = request.form.get('serie')
        letra = request.form.get('letra')
        
        if not validar_dados_turma(serie, letra):
            return redirect(url_for('turmas'))

        escola_id = get_school_id( session['id'])
        esc = escola.get(escola_id)
        
        nova_turma = turma.Turma(0, serie, letra.upper())
        turma.create(nova_turma, esc)
        
        flash("Turma cadastrada com sucesso!")
        return redirect(url_for('turmas'))
    
    except Exception as e:
        app.logger.error(f"Erro ao cadastrar turma: {e}")
        flash("Ocorreu um erro ao cadastrar a turma. Por favor, tente novamente.")
        return redirect(url_for('turmas'))


def validar_dados_turma(serie, letra):

    if not serie or not letra:
        flash("Todos os campos são obrigatórios!")
        return False
    
    if not serie.isdigit() or int(serie) not in range(1, 10):
        flash("A série deve ser um número entre 1 e 9.")
        return False
    
    if not letra.isalpha() or len(letra) != 1:
        flash("A letra deve ser um único caractere alfabético.")
        return False
    
    return True

if __name__ == "__main__":
    app.run(debug=True)
