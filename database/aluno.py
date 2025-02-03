import sqlite3
from random import randint
from database.banco import connect_db
from database.connection_tables import escolas_alunos


class Aluno:
    """Modelo de dados da tabela alunos"""

    def __init__(self, al_id=0, nome='', senha='', data_nascimento='', ano_matricula='', cpf='', idade=0) -> None:
        self.al_id = al_id
        self.nome = nome
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.ano_matricula = ano_matricula
        self.cpf = cpf
        self.idade = idade

    def __str__(self) -> str:
        return str(self.al_id) + ' ' + self.nome
    

def create(aluno: Aluno, escola):
    """Insere um novo aluno no banco de dados"""
    connection, cursor = connect_db()

    try:
        al_id = generate_student_id(aluno, escola)

        cursor.execute('INSERT INTO alunos (id, nome, senha, data_nascimento, ano_matricula, cpf, idade) VALUES (?, ?, ?, ?, ?, ?, ?)',
                        (al_id, aluno.nome, aluno.senha, aluno.data_nascimento, aluno.ano_matricula, aluno.cpf, aluno.idade))
        connection.commit()

    except sqlite3.IntegrityError:
        print('ID duplicado')
    else:
        escolas_alunos(escola.escola_id, al_id, cursor, connection)
        aluno.al_id = al_id
    
    connection.close()


def delete(al_id):
    """Deleta um aluno do banco de dados"""
    connection, cursor = connect_db()

    tables = ['turmas_alunos', 'escolas_alunos'] # Tabelas de conexão

    cursor.execute('DELETE FROM alunos WHERE id = ?', (str(al_id),))
    connection.commit()

    for table in tables:
        cursor.execute(f'DELETE FROM {table} WHERE alunos_id = ?', (str(al_id),))
        connection.commit()

    connection.close()


def list_students():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM alunos')
    alunos_1 = cursor.fetchall() # Lista com os dados da tabela
    alunos_2: list[Aluno] = [] # Lista de Objetos(Aluno) com os dados da tabela

    for aluno in alunos_1:
        alunos_2.append(Aluno(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5], aluno[6]))

    connection.close()

    return alunos_2


def get(al_id):
    """Pega um aluno especifico do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM alunos WHERE id = ?', (str(al_id),))
    row = cursor.fetchall()[0]
    aluno = Aluno(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

    connection.close()

    return aluno


def update(al_id, aluno: Aluno):
    """Atualiza um elemento no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('UPDATE alunos SET nome = ?, senha = ?, data_nascimento = ?, ano_matricula = ?, cpf = ?, idade = ? WHERE id = ?',
                (aluno.nome, aluno.senha, aluno.data_nascimento, aluno.ano_matricula, aluno.cpf, aluno.idade, al_id))
    
    connection.commit()
    connection.close()


def generate_student_id(aluno: Aluno, escola):
    """Gera um id para o aluno"""
    cod = aluno.ano_matricula + str(escola.escola_id)

    for i in range(4):
        cod += str(randint(0, 9))

    return cod


def list_students_by_class(class_id): #-> list:
    """Lista os alunos por turma"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM turmas_alunos WHERE turmas_id = ?', (str(class_id),))
    students_id = []
    students_obj: list[Aluno] = []
    rows = cursor.fetchall()
    
    for row in rows:
        if row[1] not in students_id:
            students_id.append(row[1])

    placeholders = ', '.join('?' for _ in students_id)
    cursor.execute(f'SELECT * FROM alunos WHERE id IN ({placeholders})', students_id)
    students = cursor.fetchall()

    for student in students:
        students_obj.append(Aluno(student[0], student[1], student[2], student[3], student[4], student[5], student[6]))

    connection.close()

    return students_obj


def list_students_by_school(school_id): #-> list:
    """Lista os alunos por escola"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM escolas_alunos WHERE escolas_id = ?', (str(school_id),))
    students_id = []
    students_obj: list[Aluno] = []
    rows = cursor.fetchall()
    
    for row in rows:
        if row[1] not in students_id:
            students_id.append(row[1])

    placeholders = ', '.join('?' for _ in students_id)
    cursor.execute(f'SELECT * FROM alunos WHERE id IN ({placeholders})', students_id)
    students = cursor.fetchall()

    for student in students:
        students_obj.append(Aluno(student[0], student[1], student[2], student[3], student[4], student[5], student[6]))

    connection.close()

    return students_obj
