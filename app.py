from flask import Flask, render_template
from database import banco, connection_tables, aluno, turma, escola, gestor
import database.professor as prof
import database.coordenador as coor

app = Flask(__name__)

banco.create_database()

esc = escola.Escola(0, 'IFCE', 'Crato', 'CE')
professor = prof.Professor(0, 'Matheus Soares', 'matheus@gmail.com', '1234', 'CE', '02-10-2004')
prof.create(professor, esc)

lista = prof.list_teachers()

for item in lista:
    print(item)

# @app.route('/')
# def index():
    # return render_template('index.html')

