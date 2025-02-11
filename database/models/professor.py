from database.scripts.banco import connect_db
from database.scripts.connection_tables import escolas_professores
import sqlite3
from random import randint


class Professor:
    """Modelo de dados da tabela professores"""

    def __init__(self, prof_id=0, nome='', email='', senha='', uf='', data_nascimento='', cpf='', idade=0) -> None:
        self.prof_id = prof_id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.uf = uf
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.idade = idade

    def __str__(self) -> str:
        return str(self.prof_id) + ' ' + self.nome
    
def create(professor: Professor, escola):
    """Insere um novo professor no banco de dados"""
    connection, cursor = connect_db()

    try:
        prof_id = generate_teacher_id(professor, escola)

        cursor.execute('INSERT INTO professores (id, nome, email, senha, uf, data_nascimento, cpf, idade) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                        (prof_id, professor.nome, professor.email, professor.senha, professor.uf, professor.data_nascimento, professor.cpf, professor.idade))
        connection.commit() 

    except sqlite3.IntegrityError:
        print('ID duplicado')
    else:
        escolas_professores(escola.escola_id, prof_id, cursor, connection)
        professor.prof_id = prof_id
    
    connection.close()


def delete(prof_id):
    """Deleta um professor do banco de dados"""
    connection, cursor = connect_db()

    tables = ['professores_turmas_materias', 'escolas_professores']

    cursor.execute('DELETE FROM professores WHERE id = ?', (str(prof_id),))
    connection.commit()

    for table in tables:
        cursor.execute(f'DELETE FROM {table} WHERE professores_id = ?', (str(prof_id),))
        connection.commit()

    connection.close()


def list_teachers():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM professores')
    profs_1 = cursor.fetchall() # Lista com os dados da tabela
    profs_2: list[Professor] = [] # Lista de Objetos(Professor) com os dados da tabela

    for prof in profs_1:
        profs_2.append(Professor(prof[0], prof[1], prof[2], prof[3], prof[4], prof[5], prof[6], prof[7]))

    connection.close()

    return profs_2


def get(prof_id):
    """Pega um professor especifico do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM professores WHERE id = ?', (str(prof_id),))
    row = cursor.fetchall()[0]
    prof = Professor(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    connection.close()

    return prof

def update(prof_id, prof: Professor):
    """Atualiza um elemento no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('UPDATE professores SET nome = ?, email = ?, senha = ?, uf = ?, data_nascimento = ?, cpf = ?, idade = ? WHERE id = ?',
                (prof.nome, prof.email, prof.senha, prof.uf, prof.data_nascimento, prof.cpf, prof.idade, prof_id))
    
    connection.commit()
    connection.close()


def generate_teacher_id(professor: Professor, escola):
    """Gera um id para o professor"""
    nascimento = professor.data_nascimento[6:]
    cod = nascimento + str(escola.escola_id)
    
    for n in range(3):
        cod += str(randint(0, 9))
    
    return cod


def list_teachers_by_school(school_id):
    """Devovle uma lista de professores que são da mesma escola"""

    connection, cursor = connect_db()
    cursor.execute('SELECT * FROM escolas_professores WHERE escolas_id = ?', (str(school_id),))
    teachers_id = []
    teachers_obj = []
    rows = cursor.fetchall()

    for row in rows:
        if row[1] not in teachers_id:
            teachers_id.append(row[1])

    placeholders = ', '.join('?' for _ in teachers_id)
    cursor.execute(f'SELECT * FROM professores WHERE id IN ({placeholders})', teachers_id)
    teachers = cursor.fetchall()

    for teacher in teachers:
        teachers_obj.append(Professor(teacher[0], teacher[1], teacher[2], teacher[3], teacher[4], teacher[5], teacher[6], teacher[7]))

    connection.close()

    return teachers_obj

