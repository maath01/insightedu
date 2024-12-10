from flask import Flask, render_template
from database import banco, connection_tables, aluno, turma, escola, gestor
import database.professor as prof
import database.coordenador as coor

app = Flask(__name__)

banco.create_database()

@app.route('/')
def index():
    return render_template('index.html')

