import sqlite3
from database.scripts.banco import connect_db
import database.models.avaliacao as avl
import database.models.turma as turma
from database.models.aluno import list_students_by_class
from random import randint


class Nota:
    def __init__(self, nota_id=0, al_id=0, av_id=0, nota=0.0):
        self.nota_id = nota_id
        self.al_id = al_id
        self.av_id = av_id
        self.nota = nota

    def __str__(self):
        return f'{self.nota_id} - Aluno: {self.al_id}, Avaliação: {self.av_id}, Nota: {self.nota}'

def create(nota: Nota):
    """Insere uma nova nota no banco de dados."""

    connection, cursor = connect_db()

    try:

        nota_id = generate_nota_id(nota.al_id, nota.av_id)

        cursor.execute('INSERT INTO notas (id, aluno_id, avaliacao_id, nota) VALUES (?, ?, ?, ?)',
                       (nota_id, nota.al_id, nota.av_id, nota.nota))
        connection.commit()

    except sqlite3.IntegrityError:
        print('ID duplicado')
    
    else:
        nota.nota_id = nota_id

    connection.close()

def delete(nota_id):
    """Deleta uma nota do banco de dados."""

    connection, cursor = connect_db()

    cursor.execute('DELETE FROM notas WHERE id = ?', (nota_id,))
    connection.commit()
    connection.close()

def list_notes():
    """Lista todas as notas do banco de dados."""

    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM notas')
    notas_1 = cursor.fetchall()  # Lista com os dados da tabela
    notas_2: list[Nota] = []  # Lista de objetos Nota com os dados da tabela

    for nota in notas_1:
        notas_2.append(Nota(nota[0], nota[1], nota[2], nota[3]))

    connection.close()

    return notas_2

def get(nota_id):
    """Recupera uma nota do banco de dados."""

    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM notas WHERE id = ?', (nota_id,))
    row = cursor.fetchone()

    if row:
        nota = Nota(row[0], row[1], row[2], row[3])
    else:
        nota = None

    connection.close()

    return nota


def update(nota_id, nota: Nota):
    """Atualiza um elemento no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute("UPDATE notas SET  aluno_id = ?, avaliacao_id = ?, nota = ? WHERE id = ?",
                  (nota.al_id, nota.av_id, nota.nota, nota_id))
    connection.commit()
    connection.close()  


def generate_nota_id(al_id, av_id):
    """Gera um ID único para a nota."""
    nota_id = f"{al_id}{str(av_id)[0:3]}"

    for _ in range(2):
        nota_id += str(randint(0, 9))
    
    return nota_id


def get_student_notes(al_id):
    """Devolve todas as notas de um aluno"""

    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM notas WHERE aluno_id = ?', (str(al_id),))
    rows = cursor.fetchall()
    connection.close()

    notas = {
        '1 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '2 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '3 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '4 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '5 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '6 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '7 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '8 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '9 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '1 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '2 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '3 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '4 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '5 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '6 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '7 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '8 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        '9 ano': {'Português': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Matemática': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Ciencias': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Geografia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}, 'Historia': {'1 bim': None, '2 bim': None, '3 bim': None, '4 bim': None}},
        }

    for row in rows:
        av = avl.get(row[2])
        materia = avl.get_matter(av)

        if notas[f'{str(av.serie)} ano'][materia][f'{str(av.bimestre)} bim'] == None:
            notas[f'{str(av.serie)} ano'][materia][f'{str(av.bimestre)} bim'] = row[3]
        else:
            notas[f'{str(av.serie)} ano'][materia][f'{str(av.bimestre)} bim'] += row[3]

    return notas


def get_student_average_general(al_id, serie):
    """Calcula a media de um aluno em uma determinada serie"""

    notes = get_student_notes(al_id)
    soma = 0
    count = 0

    for materia in notes[f'{str(serie)} ano'].values():
        for nota in materia.values():
            if nota != None:
                soma += nota
                count += 1
    try:
        media = soma/count
    except ZeroDivisionError:
        return 0
    
    return media


def get_student_average_by_bim(al_id, serie, bimestre):
    """Calcula a media de um aluno em uma determinada serie e bimestre"""
    notes = get_student_notes(al_id)
    soma = 0
    count = 0

    for materia in notes[f'{str(serie)} ano'].values():
        for bim, nota in materia.items():
            if nota != None and bim[0] == str(bimestre):
                soma += nota
                count += 1
    
    try:
        media = soma/count
    except ZeroDivisionError:
        return 0
    return media


def get_class_average_general(alunos, tur_id):
    """Calcula a media de uma classe"""

    turma_ = turma.get(tur_id)
    soma = 0
    count = 0

    for aluno in alunos:
        media = get_student_average_general(aluno.al_id, turma_.serie)
        soma += media
        count += 1
    
    try:
        media = soma/count
    except ZeroDivisionError:
        return 0

    return media


def acess_notes_data(notes: dict, serie: int, bimestre: int, materia: str):
    """Recebe um dicionario de notas, juntamente a serie, o bimestre e a materia e devolve a nota correspondente"""
    if 0 <= serie >= 10:
        return None
    if 0 <= bimestre >= 5:
        return None
    
    nota = notes[f'{str(serie)} ano'][materia][f'{str(bimestre)} bim']
    return nota


def get_student_average_by_matter(id_aluno, materia, serie_atual):
    """Função que calcula a média de determinado aluno na matéria solicitada"""
    
    notas = get_student_notes(id_aluno)
    soma = 0
    count = 0
    serie= str(serie_atual)+' ano'
    for nota in notas[serie][materia].items():
        if nota[1] is not None:
                  soma +=nota[1]
                  count +=1

    try:
        media = soma / count
    except ZeroDivisionError:
        return 0 
    
    return media
 
 
def get_averages_by_matter(materia, id_turma, serie):
    """Função que retorna uma lista com a média das notas dos alunos que pertencem a mesma turma em determinada matéria  """

    lista_alunos=list_students_by_class(id_turma)
    media_list=[]
    for aluno in lista_alunos:
       media=get_student_average_by_matter(aluno.al_id, materia,serie)
       media_list.append(media)

    return media_list


def get_class_average_by_matter(materia, id_turma, serie):
    """Função que calcula a médias das notas dos alunos que pertencem a mesma turma em determinada matéria  """

    aluno_notas =get_averages_by_matter( materia,id_turma,serie )
    soma=0
    count=0
    for nota in aluno_notas:
        if nota != None:
            soma +=nota
            count +=1
    try:
        media=soma/count
    except ZeroDivisionError:
        return 0
    return media


def get_averages_general(id_turma, serie):
    """Função que retorna uma lista com as médias de notas de todas as matérias dos alunos que pertencem a mesma turma """

    lista_alunos=list_students_by_class(id_turma)
    list_notas_gerais=[]
    for aluno in lista_alunos:
        notas_gerais=get_student_average_general(aluno.al_id,serie)
        print(notas_gerais)
        list_notas_gerais.append(notas_gerais)

    return list_notas_gerais


def get_student_average_by_matter(id_aluno, materia, serie_atual):
    """Função que calcula a média de determinado aluno na matéria solicitada"""
    
    notas = get_student_notes(id_aluno)
    soma = 0
    count = 0
    serie= str(serie_atual)+' ano'
    for nota in notas[serie][materia].items():
        if nota[1] is not None:
                  soma +=nota[1]
                  count +=1

    try:
        media = soma / count
    except ZeroDivisionError:
        return 0 
    
    return media
 
 
def get_averages_by_matter(materia, id_turma, serie):
    """Função que retorna uma lista com a média das notas dos alunos que pertencem a mesma turma em determinada matéria  """

    lista_alunos=list_students_by_class(id_turma)
    media_list=[]
    for aluno in lista_alunos:
       media=get_student_average_by_matter(aluno.al_id, materia,serie)
       media_list.append(media)

    return media_list


def get_class_average_by_matter(materia, id_turma, serie):
    """Função que calcula a médias das notas dos alunos que pertencem a mesma turma em determinada matéria  """

    aluno_notas =get_averages_by_matter( materia,id_turma,serie )
    soma=0
    count=0
    for nota in aluno_notas:
        if nota != None:
            soma +=nota
            count +=1
    try:
        media=soma/count
    except ZeroDivisionError:
        return 0
    return media


def get_averages_general(id_turma, serie):
    """Função que retorna uma lista com as médias de notas de todas as matérias dos alunos que pertencem a mesma turma """

    lista_alunos=list_students_by_class(id_turma)
    list_notas_gerais=[]
    for aluno in lista_alunos:
        notas_gerais=get_student_average_general(aluno.al_id,serie)
        print(notas_gerais)
        list_notas_gerais.append(notas_gerais)

    return list_notas_gerais


def get_student_average_by_matter(id_aluno, materia, serie_atual):

    """Função que calcula a média de determinado aluno na matéria solicitada"""
    
    notas = get_student_notes(id_aluno)
    soma = 0
    count = 0
    serie= str(serie_atual)+' ano'
    for nota in notas[serie][materia].items():
        if nota[1] is not None:
                  soma +=nota[1]
                  count +=1

    try:
        media = soma / count
    except ZeroDivisionError:
        return 0 
    
    return media

def get_averages_by_matter( materia,id_turma,serie ):

    """Função que retorna uma lista com a média das notas dos alunos que pertencem a mesma turma em determinada matéria  """

    lista_alunos=list_students_by_class(id_turma)
    media_list=[]
    for aluno in lista_alunos:
       media=get_student_average_by_matter(aluno.al_id, materia,serie)
       media_list.append(media)

    return media_list

def get_class_average_by_matter( materia,id_turma,serie):

    """Função que calcula a médias das notas dos alunos que pertencem a mesma turma em determinada matéria  """

    aluno_notas =get_averages_by_matter( materia,id_turma,serie )
    soma=0
    count=0
    for nota in aluno_notas:
        if nota != None:
            soma +=nota
            count +=1
    try:
        media=soma/count
    except ZeroDivisionError:
        return 0
    return media

def get_averages_general(id_turma,serie):

    """Função que retorna uma lista com as médias de notas de todas as matérias dos alunos que pertencem a mesma turma """

    lista_alunos=list_students_by_class(id_turma)
    list_notas_gerais=[]
    for aluno in lista_alunos:
        notas_gerais=get_student_average_general(aluno.al_id,serie)
        print(notas_gerais)
        list_notas_gerais.append(notas_gerais)

    return list_notas_gerais

def get_class_average_by_bim_and_matter(alunos, id_turma, bim, materia):
    """Calcula a media da turma em um bimestre, em determinada materia"""
    turma_ = turma.get(id_turma)
    total = 0
    count = 0
    
    for aluno in alunos:
        notas = get_student_notes(aluno.al_id)
        nota = acess_notes_data(notas, turma_.serie, bim, materia)
        total += nota
        count += 1

    try:
        media = total / count
    except ZeroDivisionError:
        return 0
    return media