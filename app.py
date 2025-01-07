from flask import Flask, render_template, request, session, flash, redirect, url_for
from database import aluno, banco, connection_tables, turma, escola, gestor
import database.professor as prof
import database.coordenador as coor
import sqlite3

app = Flask(__name__)
app.secret_key = 'insightedu'

banco.create_database()

#@app.route('/lista_alunos')
#def lista_alunos():
#    print(alunos)

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

@app.route('/home_gestor')
def home_gestor():
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
                
                elif categoria == 'gestor':
                     session['usuario_logado'] = request.form['nome']
                     flash(f"gestor(a) {request.form['nome']} foi logado(a) com sucesso!")
                     return redirect(url_for('home_gestor'))
                
                
            else:
                flash('Não logado, tente novamente!')
                return render_template('login.html')
            
        finally:
            connection.close()

    return render_template('login.html')

@app.route('/buscar_turma_prof', methods=['POST'])
def buscar_turma_prof():
    turma = request.form['turma']

    connection = sqlite3.connect('database/banco.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM professores_turmas_materias  WHERE turmas_id = ?", (turma,))
    turma_encontrada = cursor.fetchone()

    if turma_encontrada:
        cursor.execute("""
            SELECT alunos.id, alunos.nome
            FROM alunos
            JOIN turmas_alunos ON alunos.id = turmas_alunos.alunos_id
            WHERE turmas_alunos.turmas_id = ?
        """, (turma_encontrada[0],))  
        alunos = cursor.fetchall()  

        connection.close()

     
        return render_template('turma_encontrada.html', turma=turma_encontrada, alunos=alunos)
    else:
        flash('Turma não encontrada!')  
        connection.close()
        return redirect(url_for('home_professor'))
    


@app.route('/buscar_turma_coor', methods=['POST'])
def buscar_turma_coor():
    turma = request.form['turma']

    connection = sqlite3.connect('database/banco.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM coordenadores_turmas  WHERE turmas_id = ?", (turma,))
    turma_encontrada = cursor.fetchone()

    if turma_encontrada:
        cursor.execute("""
            SELECT alunos.id, alunos.nome
            FROM alunos
            JOIN turmas_alunos ON alunos.id = turmas_alunos.alunos_id
            WHERE turmas_alunos.turmas_id = ?
        """, (turma_encontrada[0],))  
        alunos = cursor.fetchall()  

        connection.close()

     
        return render_template('turma_encontrada.html', turma=turma_encontrada, alunos=alunos)
    else:
        flash('Turma não encontrada!')  
        connection.close()
        return redirect(url_for('home_coordenador'))
    

@app.route('/buscar_turma_gestor', methods=['POST'])
def buscar_turma_gestor():
    turma = request.form['turma']

    connection = sqlite3.connect('database/banco.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM turmas  WHERE id = ?", (turma,))
    turma_encontrada = cursor.fetchone()

    if turma_encontrada:
        cursor.execute("""
            SELECT alunos.id, alunos.nome
            FROM alunos
            JOIN turmas ON alunos.id = turmas.id
            WHERE turmas.id = ?
        """, (turma_encontrada[0],))  
        alunos = cursor.fetchall()  

        connection.close()

        return render_template('turma_encontrada.html', turma=turma_encontrada, alunos=alunos)
    else:
        flash('Turma não encontrada!')  
        connection.close()
        return redirect(url_for('home_gestor'))
    
if __name__ == '__main__':
    app.run(debug=True)
