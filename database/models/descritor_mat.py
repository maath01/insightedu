from database.scripts.banco import connect_db

class Descritor:
    """Modelo de dados da tabela de Descritores Matemática"""

    def __init__(self,id=None, habilidade='', serie=0, numero=0, materia=''):
          self.id = id
          self.habilidade = habilidade
          self.serie = serie
          self.numero = numero
          self.materia = materia

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.habilidade
    

def list_descs():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM descritores_mat')
    descritor_1 = cursor.fetchall() # Lista com os dados da tabela
    descritor_2: list[Descritor] = [] # Lista de Objetos(Descritor) com os dados da tabela

    for descritor  in descritor_1:
        descritor_2.append(Descritor(descritor[0], descritor[1], descritor[2], descritor[3], descritor[4]))

    connection.close()

    return descritor_2


def get(desc_id):
    """Pega um descritor especifico do banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM descritores_mat WHERE id = ?', (str(desc_id),))
    row = cursor.fetchall()[0]
    descritor = Descritor(row[0], row[1], row[2], row[3],row[4])

    connection.close()

    return descritor


    

    





