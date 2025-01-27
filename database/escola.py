from database.banco import connect_db
import sqlite3
from random import randint


class Escola:
    """Modelo de dados da tabela escolas"""

    def __init__(self, escola_id=0, nome='', cidade='', uf=''):
          self.escola_id= escola_id
          self.nome=nome
          self.cidade=cidade
          self.uf=uf

    def __str__(self) -> str:
        return str(self.escola_id) + ' ' + self.nome
    
def create(escola: Escola):
    """Insere uma nova escola no banco de dados"""
    connection, cursor = connect_db()

    try:
        escola_id = generate_school_id(escola)

        cursor.execute('INSERT INTO escolas (id, nome, cidade, uf) VALUES (?, ?, ?, ?)',
                        (escola_id, escola.nome, escola.cidade, escola.uf))

    except sqlite3.IntegrityError:
        print('ID duplicado')
    
    connection.commit()
    connection.close()

def list_schools():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM escolas')
    escolas_1 = cursor.fetchall() # Lista com os dados da tabela
    escolas_2: list[Escola] = [] # Lista de Objetos(Escola) com os dados da tabela

    for escola  in escolas_1:
        escolas_2.append(Escola(escola[0], escola[1], escola[2], escola[3], escola[4]))

    connection.close()

    return escolas_2


def delete(escola_id):
    """Deleta uma escola do banco de dados"""
    connection, cursor = connect_db()

    tables = ['escolas_gestores', 'escolas_turmas', 'escolas_professores', 'escolas_alunos', 'escolas_coordenadores']

    cursor.execute('DELETE FROM escolas WHERE id = ?', (str(escola_id),))
    connection.commit()

    for table in tables:
        cursor.execute(f'DELETE FROM {table} WHERE escolas_id = ?', (str(escola_id),))
        connection.commit()

    connection.close()


def get(escola_id):
    """Pega uma escola especifica do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM escolas WHERE id = ?', (str(escola_id),))
    row = cursor.fetchall()[0]
    escola = Escola(row[0], row[1], row[2], row[3])

    connection.close()

    return escola

def update_school(escola_id,escola: Escola):
    """Atualiza um elemento no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute("UPDATE escolas SET  nome= ?, cidade = ?, uf = ? WHERE id = ?",
                  (escola.nome, escola.cidade,escola.uf, escola_id))
    connection.commit()
    connection.close()  

def generate_school_id(escola: Escola):
    """Gera um id para a escola"""
    connection, cursor = connect_db()

    cursor.execute('SELECT id FROM ufs WHERE sigla = ?', (escola.uf,))
    uf_cod = cursor.fetchall()[0][0]

    cod = str(uf_cod)
    for n in range(4):
        cod += str(randint(0, 9))
    
    return cod


def get_school_id(p_id):
    """Recebe um id de um professor, gestor ou coordenador e coleta o id de sua escola"""
    school_id = ''
    if len(str(p_id)) == 12:
        school_id = str(p_id)[4:9]
    elif len(str(p_id)) == 13:
        school_id = str(p_id)[4:10]
    
    return school_id