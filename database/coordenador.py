from database.banco import connect_db
from database.connection_tables import escolas_coordenadores
import sqlite3
from random import randint

class Coordenador:
    """Modelo de dados da tabela coordenadores"""
    
    def __init__(self, coordenador_id=0, nome='',email='',nascimento='',senha='') -> None:
        self.coordenador_id = coordenador_id
        self.nome = nome
        self.email = email
        self.nascimento=nascimento
        self.senha=senha

    def __str__(self) -> str:
        return str(self.coordenador_id) + ' ' + str(self.nome) 
 
def create(coordenador: Coordenador, escola):
   
    connection, cursor = connect_db()

    try:
        coordenador_id = generate_coordinator_id(coordenador, escola)

        cursor.execute('INSERT INTO coordenadores (id,nome,email,nascimento,senha) VALUES (?, ?, ?, ?,?)',
                        (coordenador_id, coordenador.nome, coordenador.email, coordenador.nascimento,coordenador.senha))
        connection.commit()

    except sqlite3.IntegrityError:
        print('ID duplicado')
    else:
        escolas_coordenadores(escola.escola_id, coordenador_id, cursor, connection)
    
    connection.close()


def delete(coordenador_id):
    """Deleta um coordenador do banco de dados"""
    connection, cursor = connect_db()

    tables = ['escolas_coordenadores', 'coordenadores_turmas']

    cursor.execute('DELETE FROM coodenadores WHERE id = ?', (str(coordenador_id),))
    connection.commit()

    for table in tables:
        cursor.execute(f'DELETE FROM {table} WHERE coordenadores_id = ?', (str(coordenador_id),))
        connection.commit()

    connection.close()


def list_coordinators():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM coordenadores')
    coordenadores_1 = cursor.fetchall() # Lista com os dados da tabela
    coordenadores_2: list[Coordenador] = [] # Lista de Objetos(Professor) com os dados da tabela

    for coordenador  in coordenadores_1:
       coordenadores_2.append(Coordenador(coordenador[0],coordenador[1], coordenador[2],coordenador[3],coordenador[4]))

    connection.close()

    return coordenadores_2


def get(coordenador_id):
    """Pega um coordenador especifico do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM coordenadores WHERE id = ?', (str(coordenador_id),))
    row = cursor.fetchall()[0]
    coordenador = Coordenador(row[0], row[1], row[2], row[3], row[4])

    connection.close()

    return coordenador

def update_coordinator(coordenador_id,coordenador: Coordenador):
    """Atualiza um elemento no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute("UPDATE coordenadores SET  nome= ?, email = ?, nascimento = ?, senha = ? WHERE id = ?", 
                   (coordenador.nome, coordenador.email,coordenador.nascimento,coordenador.senha, coordenador_id))
    
    connection.commit()
    connection.close()  



def generate_coordinator_id(coordenador: Coordenador, escola):
    nascimento = coordenador.nascimento[6:]
    cod = nascimento + str(escola.escola_id)
    
    for n in range(3):
        cod += str(randint(0, 9))
    
    return cod


