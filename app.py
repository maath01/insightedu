from flask import Flask, render_template, request, session, flash, redirect, url_for, Response
from io import BytesIO
from functools import wraps
import matplotlib.pyplot as plt
from database.models import aluno, turma, escola, nota, questao
from database.scripts import banco, connection_tables
import database.models.professor as prof 
import database.models.coordenador as coor
import database.models.avaliacao as av
import database.models.dominio_descritores_port as dom_pt
import database.models.dominio_descritores_mat as dom_mt
import database.models.descritor_port as desc_p
import database.models.descritor_mat as desc_m


app = Flask(__name__)
app.secret_key = 'insightedu'

banco.create_database()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id' not in session:  # Verifica se o usuário está autenticado
            return redirect(url_for('login'))  # Redireciona para a página de login
        return f(*args, **kwargs)  # Permite o acesso à rota protegida
    return decorated_function


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
                flash(f"Aluno(a) {user[1]}, foi logado(a) com sucesso!")   

            elif categoria == 'professor':
                session['user_type'] = 'professor'
                flash(f"Professor(a) {user[1]}, foi logado(a) com sucesso!")

            elif categoria == 'coordenador':
                session['user_type'] = 'coordenador'
                flash(f"Coordenador(a) {user[1]}, foi logado(a) com sucesso!")

            elif categoria == 'gestor':
                session['user_type'] = 'gestor'
                flash(f"Gestor(a) {user[1]}, foi logado(a) com sucesso!")

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
@login_required
def home():
    if session['user_type'] == 'aluno':
        return render_template('home_aluno.html')
    
    elif session['user_type'] == 'professor':
        return render_template('home_professor.html')

    elif session['user_type'] == 'coordenador':
        return render_template('home_coordenador.html')
    
    elif session['user_type'] == 'gestor':
        return render_template('home_gestor.html')



@app.route('/perfil_aluno/<int:aluno_id>')
@login_required
def perfil_aluno(aluno_id):
    try:  
        student = aluno.get(aluno_id) 
        notas = nota.get_student_notes(aluno_id)
        if student:

            return render_template('perfil_aluno.html', aluno=student, notas=notas)
        else:
            return render_template('erro.html', mensagem=f"Aluno com ID {aluno_id} não encontrado.")
    finally:
        pass


@app.route('/home/lista_professores')
@login_required
def list_teachers():
    if session.get('user_type') == 'gestor':
        id_gestor=session.get('id')
        school_id = escola.get_school_id(id_gestor)
        professores = prof.list_teachers_by_school(school_id)
        return render_template('lista_profs.html', professores=professores)
    else:
        return render_template('home.html')


@app.route('/home/lista_professores/<int:prof_id>')
@login_required
def perfil_professor(prof_id):
    professor = prof.get(prof_id)
    if professor:
        return render_template('perfil_professor.html', professor=professor)
    else:
        return ("Erro") 


@app.route('/home/avaliacoes')
@login_required
def avaliacoes():
    if session.get('user_type') == 'professor':
        avaliacoes = av.list_evaluations_by_teacher(session['id'])
        return render_template('avaliacoes.html', avaliacoes=avaliacoes)
    else:
        return render_template('home.html')
    

@app.route('/home/avaliacoes/<int:av_id>')
@login_required
def avaliacao(av_id):
    if session.get('user_type') == 'professor':
        avaliacao = av.get(av_id)
        alunos = aluno.list_students_by_class(avaliacao.turma_id)
        materia = av.get_matter(avaliacao)
        return render_template('avaliacao.html', avaliacao=avaliacao, alunos=alunos, materia=materia)
    else:
        return render_template('home.html')
    

@app.route('/home/turmas')
@login_required
def turmas():
    if session['user_type'] == 'gestor':
        escola_id = escola.get_school_id(session['id'])
        turmas_ = turma.list_classes_by_school(escola_id)
        profs = prof.list_teachers_by_school(escola_id)
        return render_template('turmas.html', turmas=turmas_, professores=profs, user_type=session['user_type'])
    elif session['user_type'] == 'professor': 
        turmas_ = turma.list_classes_by_teacher(session['id'])
        return render_template('turmas.html', turmas=turmas_, user_type=session['user_type'])


@app.route ('/home/turmas/<int:turma_id>')
@login_required
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


@app.route('/home/alunos')
@login_required
def lista_alunos_por_escola():
    if session.get('user_type') != 'gestor':
        flash("Você não tem permissão para acessar esta página.")
        return redirect(url_for('home'))

    try:
        escola_id = escola.get_school_id(session['id'])
        alunos = aluno.list_students_by_school(escola_id)

        return render_template('lista_alunos_por_escola.html', alunos=alunos, escola_id=escola_id)
    except Exception as e:
        flash("Ocorreu um erro ao listar os alunos. Por favor, tente novamente.")
        return redirect(url_for('home'))
    

@app.route('/home/questoes')
@login_required
def questoes():
    """Acessa o banco de questões"""
    questions = questao.list_questions()
    return render_template('questoes.html', questions=questions)

@app.route('/home/questoes/filtradas', methods=['POST'])
@login_required
def questoes_filtradas():
    """Recebe parametros e pesquisa questoes no banco de dados"""
    serie = request.form['serie']
    materia = request.form['materia']
    assunto = request.form['assunto']
    if serie == 'todas' and materia == 'todas' and assunto == '':
        return redirect(url_for('questoes'))
    
    questions = questao.list_questions_filtered(serie, materia, assunto)
    return render_template('questoes.html', questions=questions)


@app.route('/cadastro/notas/<int:av_id>', methods=['POST'])
@login_required
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
@login_required
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
@login_required
def cadastro_turma():
    
    if 'user_type' not in session or session['user_type'] != 'gestor':
        flash("Você não tem permissão para acessar esta funcionalidade.")
        return redirect(url_for('home'))
    
    try:
        serie = request.form.get('serie')
        letra = request.form.get('letra')
        prof_port = request.form.get('prof-portugues')
        prof_mat = request.form.get('prof-matematica')
        prof_cie = request.form.get('prof-ciencias')
        prof_hist = request.form.get('prof-historia')
        prof_geo = request.form.get('prof-geografia')
        
        if not validar_dados_turma(serie, letra):
            return redirect(url_for('turmas'))

        escola_id = escola.get_school_id( session['id'])
        esc = escola.get(escola_id)
        
        nova_turma = turma.Turma(0, serie, letra.upper())
        turma.create(nova_turma, esc)
        connection, cursor = banco.connect_db()
        connection_tables.professores_turmas_materias(prof_port, nova_turma.tur_id, 1, cursor, connection)
        connection_tables.professores_turmas_materias(prof_mat, nova_turma.tur_id, 2, cursor, connection)
        connection_tables.professores_turmas_materias(prof_cie, nova_turma.tur_id, 3, cursor, connection)
        connection_tables.professores_turmas_materias(prof_hist, nova_turma.tur_id, 4, cursor, connection)
        connection_tables.professores_turmas_materias(prof_geo, nova_turma.tur_id, 5, cursor, connection)
        connection.close()
        
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


@app.route('/cadastro/questao', methods=['POST'])
@login_required
def cadastro_questao():
    """Cadastra uma questão no banco de dados"""
    enunciado = request.form['enunciado']
    serie = request.form['serie']
    materia = request.form['materia']
    assunto = request.form['assunto']
    resposta = request.form['resposta']

    nova_questao = questao.Questao(0, enunciado, serie, materia, assunto, resposta)
    questao.create(nova_questao)

    return redirect(url_for('questoes'))

@app.route('/cadastro/avaliacao', methods=['POST'])
def cadastro_avaliacao():
    serie = request.form['serie']
    bimestre = request.form['bimestre']
    turma_id = request.form['turma_id']
    data_aplicacao = request.form['data_aplicacao']
    materia = request.form['materia']
    
    professor_id = session['id']
    
    nova_avaliacao = av.Avaliacao(0, serie, bimestre, professor_id, turma_id, data_aplicacao)
    
    av.create(nova_avaliacao, materia)
    
    return redirect(url_for('avaliacoes'))
#funcionando 

@app.route('/cadastro/coordenador', methods=['POST'])
def cadastro_coordenador():
    nome = request.form['nome']
    email = request.form['email']
    data_nascimento = request.form['data_nascimento']
    cpf = request.form['cpf']
    idade = request.form['idade']
    
    escola_id = escola.get_school_id(session['id'])
    esc = escola.get(escola_id)
    
    novo_coordenador = coor.Coordenador(0, nome, email, data_nascimento, '12345678', cpf, idade)
    coor.create(novo_coordenador, esc)
    
    return redirect(url_for('lista_coordenadores'))


@app.route('/plot/turma/materias/medias/<int:turma_id>/<string:materia>')
@login_required
def plot_class_matters_average(turma_id, materia):
    turma_ = turma.get(turma_id)
    medias = nota.get_averages_by_matter(materia, turma_id, turma_.serie)
    alunos_nome = []
    for a in aluno.list_students_by_class(turma_id):
        alunos_nome.append(a.nome)
    
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.bar(alunos_nome, medias)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return Response(buf, mimetype='image/png')

@app.route('/plot/aluno/materias/medias/<int:al_id>')
@login_required
def plot_student_matters_average(al_id=0):
    lista_materias = ['Português', 'Matemática','Ciencias', 'Historia', 'Geografia']
    lista_medias = []
    turma_ = aluno.get_class(al_id)
    for materia in lista_materias:
        media = nota.get_student_average_by_matter(al_id, materia, turma_.serie)
        lista_medias.append(media)
        
    fig, ax = plt.subplots(figsize=(5, 2.7))
    ax.bar(lista_materias, lista_medias)
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return Response(buf, mimetype='image/png')


'''Busca por aluno através do nome enviado por requisição no form do arquivo buscar_alunos.html'''
@app.route('/buscar/alunos', methods=['GET', 'POST'])
@login_required
def buscar_alunos():
    try:
        name = request.form['nome'] 
    except:
        return render_template('buscar_alunos.html', alunos=[])  
    connection, cursor = banco.connect_db()  
    query = "SELECT * FROM alunos WHERE nome LIKE ?"  
    cursor.execute(query, (f"%{name}%",)) 
    resultados = cursor.fetchall()  
    connection.close()  
    alunos = [aluno.Aluno(*dados) for dados in resultados]
    return render_template('buscar_alunos.html', alunos=alunos)



@app.route('/matricular/aluno/<int:aluno_id>')
@login_required
def matricular_aluno(aluno_id):
    try:
        connection, cursor = banco.connect_db()
        escola_id = escola.get_school_id(session.get('id'))

        if escola_id is None:
            flash("Erro: ID da escola não encontrado!", "error")
            return redirect(url_for('perfil_aluno', aluno_id=aluno_id))
        
        connection_tables.escolas_alunos(escola_id, aluno_id, cursor, connection)
        
        connection.commit()
    except Exception as e:
        flash(f"Erro ao matricular aluno: {str(e)}", "error")
    
    finally:
        if connection:
            connection.close()
    return redirect(url_for('perfil_aluno', aluno_id=aluno_id))


@app.route('/plot/turma/materias/bimestre/<int:turma_id>')
def plot_class_matter_bim_average(turma_id):
    materias = ['Português', 'Matemática', 'Ciencias', 'Historia', 'Geografia']
    
    alunos = aluno.list_students_by_class(turma_id)
    
    portugues = []
    matematica = []
    ciencias = []
    historia = []
    geografia = []
    
    for i in range(1, 5):
        for materia in materias:
            media = nota.get_class_average_by_bim_and_matter(alunos, turma_id, i, materia)
            
            if materia == 'Português':
                portugues.append(media)
            elif materia == 'Matemática':
                matematica.append(media)
            elif materia == 'Ciencias':
                ciencias.append(media)
            elif materia == 'Historia':
                historia.append(media)
            elif materia == 'Geografia':
                geografia.append(media)
    
    fig, ax = plt.subplots()
    ax.plot(['1', '2', '3', '4'], portugues, label='Português')
    ax.plot(['1', '2', '3', '4'], matematica, label='Matemática')
    ax.plot(['1', '2', '3', '4'], ciencias, label='Ciencias')
    ax.plot(['1', '2', '3', '4'], historia, label='Historia')
    ax.plot(['1', '2', '3', '4'], geografia, label='Geografia')
    ax.legend()
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    return Response(buf.getvalue(), mimetype='image/png')


@app.route('/plot/aluno/desempenho/notas/<int:al_id>')
def plot_student_performance_by_notes(al_id):

    notas = nota.get_student_notes(al_id)

    serie = aluno.get_class(al_id).serie

    materias_dict = {"Português": [], "Matemática": [], "Ciencias": [], "Historia": [], "Geografia": []}
    

    for serie_nome, materias in notas.items():
        if serie_nome.startswith(str(serie)):
            for materia, bimestres in materias.items():
                if materia in materias_dict:
                    for bim in range(1, 5):  # 4 bimestres
                        nota_ = bimestres.get(f"{bim} bim", 0)
                        materias_dict[materia].append(nota_ if nota_ is not None else 0)

    fig, ax = plt.subplots()
    bimestres_labels = ['1', '2', '3', '4']
    
    for materia, notas_lista in materias_dict.items():
        ax.plot(bimestres_labels, notas_lista, label=materia)
    
    ax.set_title(f'Desempenho do Aluno {al_id} na Série {serie}')
    ax.set_xlabel('Bimestres')
    ax.set_ylabel('Notas')
    ax.legend()
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    return Response(buf.getvalue(), mimetype='image/png')


@app.route('/home/lista_coordenadores')
def lista_coordenadores():

    escola_id = escola.get_school_id(session['id'])    
    coordenadores = coor.list_coordinators_by_school(escola_id)
    return render_template('lista_coordenadores.html', coordenadores=coordenadores)


if __name__ == "__main__":
    app.run(debug=True)



