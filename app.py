from flask import Flask, render_template
from database import banco
import database.professor as prof
import database.aluno as aluno
import database.turma as turma


app = Flask(__name__)

banco.create_database()

@app.route('/')
def index():
    return render_template('index.html')

