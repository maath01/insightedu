from database.scripts.banco import connect_db
from database.scripts.connection_tables import escolas_turmas
import sqlite3
from random import randint


class Turma:
    """Modelo de dados da tabela turmas"""

    def __init__(self, tur_id=0, serie=0, letra='') -> None:
        self.tur_id = tur_id
        self.serie = serie
        self.letra = letra

    def __str__(self) -> str:
        return str(self.tur_id) + ' ' + str(self.serie) + ' ' + self.letra
    
def create(turma: Turma, escola):
    """Insere uma nova turma no banco de dados"""
    connection, cursor = connect_db()

    try:
        tur_id = generate_class_id(turma, escola)

        cursor.execute('INSERT INTO turmas (id, serie, letra) VALUES (?, ?, ?)', (tur_id, turma.serie, turma.letra))
        connection.commit()

    except sqlite3.IntegrityError:
        print('ID duplicado')
    else:
        escolas_turmas(escola.escola_id, tur_id, cursor, connection)
        turma.tur_id = tur_id

    connection.close()


def delete(tur_id):
    """Deleta uma turma do banco de dados"""
    connection, cursor = connect_db()

    tables = ['turmas_alunos', 'professores_turmas_materias', 'escolas_turmas', 'coordenadores_turmas']

    cursor.execute('DELETE FROM turmas WHERE id = ?', (str(tur_id),))
    connection.commit()

    for table in tables:
        cursor.execute(f'DELETE FROM {table} WHERE turmas_id = ?', (str(tur_id),))
        connection.commit()
    
    connection.close()


def list_classes():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM turmas')
    classes_1 = cursor.fetchall() # Lista com os dados da tabela
    classes_2: list[Turma] = [] # Lista de Objetos(Turma) com os dados da tabela

    for class_ in classes_1:
        classes_2.append(Turma(class_[0], class_[1], class_[2]))

    connection.close()

    return classes_2

def get(tur_id):
    """Pega uma turma especifica do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM turmas WHERE id = ?', (str(tur_id),))
    row = cursor.fetchall()[0]
    turma = Turma(row[0], row[1], row[2])

    connection.close()

    return turma


def update(tur_id, turma: Turma):
    """Atualiza um elemento no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('UPDATE turmas SET serie = ?, letra = ? WHERE id = ?',
                (turma.serie, turma.letra, tur_id))
    
    connection.commit()
    connection.close()


def generate_class_id(turma: Turma, escola):
    """Gera um id para a turma"""
    cod = str(escola.escola_id) + str(turma.serie)
    
    for n in range(3):
        cod += str(randint(0, 9))
    
    return cod



def list_classes_by_teacher(prof_id): #-> list:
    """Lista as classes por professor"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM professores_turmas_materias WHERE professores_id = ?', (str(prof_id),))
    classes_id = []
    classes_obj: list[Turma] = []
    rows = cursor.fetchall()
    
    for row in rows:
        if row[1] not in classes_id:
            classes_id.append(row[1])

    placeholders = ', '.join('?' for _ in classes_id)
    cursor.execute(f'SELECT * FROM turmas WHERE id IN ({placeholders})', classes_id)
    classes = cursor.fetchall()

    for class_ in classes:
        classes_obj.append(Turma(class_[0], class_[1], class_[2]))

    connection.close()

    return classes_obj


def list_classes_by_school(school_id): #-> list:
    """Lista as classes por escola"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM escolas_turmas WHERE escolas_id = ?', (str(school_id),))
    classes_id = []
    classes_obj: list[Turma] = []
    rows = cursor.fetchall()
    
    for row in rows:
        if row[1] not in classes_id:
            classes_id.append(row[1])

    placeholders = ', '.join('?' for _ in classes_id)
    cursor.execute(f'SELECT * FROM turmas WHERE id IN ({placeholders})', classes_id)
    classes = cursor.fetchall()

    for class_ in classes:
        print(class_)
        classes_obj.append(Turma(class_[0], class_[1], class_[2]))

    connection.close()

    return classes_obj


def list_classes_by_coordinator(coor_id): #-> list:
    """Lista as classes por coordenadors"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM coordenadores_turmas WHERE coordenadores_id = ?', (str(coor_id),))
    classes_id = []
    classes_obj: list[Turma] = []
    rows = cursor.fetchall()
    
    for row in rows:
        if row[1] not in classes_id:
            classes_id.append(row[1])

    placeholders = ', '.join('?' for _ in classes_id)
    cursor.execute(f'SELECT * FROM turmas WHERE id IN ({placeholders})', classes_id)
    classes = cursor.fetchall()

    for class_ in classes:
        print(class_)
        classes_obj.append(Turma(class_[0], class_[1], class_[2]))

    connection.close()

    return classes_obj