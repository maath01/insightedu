from flask import Flask, render_template, request, session, flash, redirect, url_for, Response
from io import BytesIO
import matplotlib.pyplot as plt
from database.aluno import list_students_by_class
from database import aluno, banco, connection_tables, turma, escola, gestor, nota
import database.professor as prof 
import database.coordenador as coor
import database.avaliacao as av
import database.dominio_descritores_port as dom_dp
import database.dominio_descritores_mat as dom_mt

app = Flask(__name__)
app.secret_key = 'insightedu'

banco.create_database()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        categoria = request.form['categoria']
        user_id = request.form['id']
        senha = request.form['senha']

        user = banco.check_login(categoria, user_id, senha)

        if user:
            session['id'] = user_id
            if categoria == 'aluno':
                session['user_type'] = 'aluno'
                flash(f"Aluno(a) foi logado(a) com sucesso!")   

            elif categoria == 'professor':
                session['user_type'] = 'professor'
                flash(f"Professor(a) foi logado(a) com sucesso!")

            elif categoria == 'coordenador':
                session['user_type'] = 'coordenador'
                flash(f"coordenador(a) foi logado(a) com sucesso!")

            elif categoria == 'gestor':
                session['user_type'] = 'gestor'
                flash(f"gestor(a) foi logado(a) com sucesso!")

            return redirect(url_for('home'))
            
        else:
            flash('Não logado, tente novamente!')
            return render_template('login.html')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('id')
    session.pop('user_type')
    return redirect(url_for('login'))


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
    

@app.route('/perfil_aluno/<int:aluno_id>/<int:serie>')
def perfil_aluno(aluno_id, serie):

    try:  
        student = aluno.get(aluno_id) 
        if student:
            return render_template('perfil_aluno.html', aluno=student, serie=serie)
        else:
            return render_template('erro.html', mensagem=f"Aluno com ID {aluno_id} não encontrado.")
    finally:
        pass


@app.route('/home/ferramentas/lista_professores')
def list_teachers():
    if session.get('user_type') == 'gestor':
        id_gestor=session.get('id')
        school_id = escola.get_school_id(id_gestor)
        professores = prof.list_teachers_by_school(school_id)
        return render_template('lista_profs.html', professores=professores)
    else:
        return render_template('home.html')


@app.route('/home/ferramentas/lista_professores/<int:prof_id>')
def perfil_professor(prof_id):
    professor = prof.get(prof_id)
    if professor:
        return render_template('perfil_professor.html', professor=professor)
    else:
        return ("Erro") 


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
        alunos = aluno.list_students_by_class(avaliacao.turma_id)
        materia = av.get_matter(avaliacao)
        return render_template('avaliacao.html', avaliacao=avaliacao, alunos=alunos, materia=materia)
    else:
        return render_template('home.html')
    

@app.route('/home/ferramentas/turmas')
def turmas():
    turmas_ = turma.list_classes_by_teacher(session['id'])
    return render_template('turmas.html', turmas=turmas_)


@app.route ('/home/ferramentas/turmas/<int:turma_id>')
def lista_alunos(turma_id):
    try:    
        alunos = aluno.list_students_by_class(turma_id)
        turma_ = turma.get(turma_id)
        if alunos:
            return render_template('lista_alunos.html', turma=turma_, alunos=alunos)
        else:
            return f"<h1>Não há alunos cadastrados na turma {turma_id}.</h1>"
    finally:
        pass


@app.route('/home/ferramentas/alunos/<int:school_id>')
def lista_alunos_por_escola(school_id):
    if session.get('user_type') != 'gestor':
        flash("Você não tem permissão para acessar esta página.")
        return redirect(url_for('home'))

    try:
        gestor_id = session['id']
        escola_id = escola.get_school_id(session['id'])

        alunos = aluno.list_students_by_school(escola_id)

        return render_template('lista_alunos_por_escola.html', alunos=alunos, escola_id=escola_id)
    except Exception as e:
        flash("Ocorreu um erro ao listar os alunos. Por favor, tente novamente.")
        return redirect(url_for('home'))


@app.route('/cadastro/notas/<int:av_id>', methods=['POST'])
def cadastro_notas(av_id):
    for aluno_id, nt in request.form.items():
        avl = av.get(av_id)
        materia = av.get_matter(avl)
        notes = nota.get_student_notes(aluno_id[5:])

        if notes[f'{avl.serie} ano'][materia][f'{avl.bimestre} bim'] == None:
            nota_ = nota.Nota(0, aluno_id[5:], av_id, nt)
            nota.create(nota_)
        elif notes[f'{avl.serie} ano'][materia][f'{avl.bimestre} bim'] != None:
            notas = banco.search('notas', 'avaliacao_id', av_id)
            for n in notas:
                if str(n[1]) == aluno_id[5:]:
                    nt_ = nota.get(n[0])
                    nt_.nota = nt
                    nota.update(nt_.nota_id, nt_)
    return redirect(url_for('avaliacao', av_id=av_id))


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
        escola_id = escola.get_school_id(gestor_id)
        esc = escola.get(escola_id)
        
        novo_aluno = aluno.Aluno(
            al_id=0,
            nome=nome,
            data_nascimento=data_nascimento,
            ano_matricula=ano_matricula,
            cpf=cpf,
            idade=idade
        )
        
        aluno.create(novo_aluno,esc)
        
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

        escola_id = escola.get_school_id( session['id'])
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


@app.route('/plot/turma/materias/medias/<int:turma_id>/<string:materia>')
def plot_class_matters_average(turma_id, materia):
    turma_ = turma.get(turma_id)
    medias = nota.get_averages_by_matter(materia, turma_id, turma_.serie)
    alunos_nome = []
    for a in list_students_by_class(turma_id):
        alunos_nome.append(a.nome)
    
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.bar(alunos_nome, medias)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return Response(buf, mimetype='image/png')

@app.route('/plot/aluno/materias/medias/<int:al_id>/<int:serie>')
def plot_student_matters_average(al_id=0, serie=0):
    lista_materias = ['Português', 'Matemática','Ciencias', 'Historia', 'Geografia']
    lista_medias = []
    for materia in lista_materias:
        media = nota.get_student_average_by_matter(al_id, materia, serie)
        lista_medias.append(media)
        
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.bar(lista_materias, lista_medias)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return Response(buf, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
