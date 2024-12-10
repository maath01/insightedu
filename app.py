from flask import Flask, render_template
from database import banco, connection_tables
import database.professor as prof
import database.aluno as aluno
import database.turma as turma
import database.escola as escola
import database.coordenador as coor
import database.gestor as gestor

app = Flask(__name__)

banco.create_database()

@app.route('/')
def index():
    return render_template('index.html')

