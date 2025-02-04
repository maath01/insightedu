from database.banco import connect_db
import sqlite3

class DominioDescritoresMat:
    def __init__(self, id=None, aluno_id=0, ds:list[int]=[]):
        self.id =id
        self.aluno_id = aluno_id
        self.dominio = ds

    def return_list(self):
        lista = self.dominio.copy()
        lista.insert(0, self.aluno_id)
        tupla = tuple(lista)
        return tupla

    def __str__(self) -> str:
        string = str(self.id) + ' ' + str(self.aluno_id)
        for d in self.dominio:
            string += f' - {str(d)}'
        
        return string

#-----------------------------------------------------------------------------------------------------------------------------------------------
def create(dominiodescritoresmat: DominioDescritoresMat):
    """Insere um novo registro de descritores de matemática no banco de dados"""
    connection, cursor = connect_db()

    try:
        cursor.execute('SELECT 1 FROM dominio_descritores_mat WHERE aluno_id = ?', (dominiodescritoresmat.aluno_id,))
        existe = cursor.fetchone() 

        if existe:
            print (f"Erro: O aluno com ID {dominiodescritoresmat.aluno_id} já está cadastrado no banco de dados.")
            return

        cursor.execute('''
            INSERT INTO dominio_descritores_mat (
            aluno_id, descritor_1, descritor_2, descritor_3, descritor_4, descritor_5, descritor_6, descritor_7, descritor_8, descritor_9, descritor_10, descritor_11, descritor_12, descritor_13, descritor_14, descritor_15, descritor_16, descritor_17, descritor_18, descritor_19, descritor_20, descritor_21, descritor_22, descritor_23, descritor_24, descritor_25, descritor_26, descritor_27, descritor_28, descritor_29, descritor_30, descritor_31) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)''',
            dominiodescritoresmat.return_list())

        connection.commit()

    except sqlite3.Error as e:
        print(f"Erro ao inserir no banco de dados: {e}")

    connection.close()


def delete(aluno_id):
    """Deleta um registro de descritores de matemática no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('DELETE FROM dominio_descritores_mat WHERE aluno_id = ?', (str(aluno_id),))
    connection.commit()

    connection.close()


def list_dom_desc():
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM dominio_descritores_mat')
    dominio_mat_1 = cursor.fetchall() # Lista com os dados da tabela
    dominio_mat_2: list[DominioDescritoresMat] = [] # Lista de Objetos com os dados da tabela

    for dominio_mat in dominio_mat_1:
        lista = [dominio_mat[2], dominio_mat[3], dominio_mat[4], dominio_mat[5], dominio_mat[6], dominio_mat[7], dominio_mat[8], dominio_mat[9], dominio_mat[10], dominio_mat[11], dominio_mat[12], dominio_mat[13], dominio_mat[14], dominio_mat[15], dominio_mat[16], dominio_mat[17], dominio_mat[18], dominio_mat[19], dominio_mat[20], dominio_mat[21], dominio_mat[22], dominio_mat[23], dominio_mat[24], dominio_mat[25], dominio_mat[26], dominio_mat[27], dominio_mat[28], dominio_mat[29], dominio_mat[30], dominio_mat[31], dominio_mat[32]]
        dominio_mat_2.append(DominioDescritoresMat(dominio_mat[0], dominio_mat[1], lista))

    connection.close()

    return dominio_mat_2



def get(aluno_id):
    """Pega um registro de descritores de matemática especifico no banco de dados"""
    connection, cursor = connect_db()

    cursor.execute('SELECT * FROM dominio_descritores_mat WHERE aluno_id = ?', (str(aluno_id),))
    row = cursor.fetchall()[0]
    lista = [row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32]]
    dominio_mat = DominioDescritoresMat(row[0], row[1], lista)

    connection.close()

    return dominio_mat


def get_dom_by_class(alunos):

    doms = []
    for aluno in alunos:
        dom = get(aluno.al_id)
        doms.append(dom)

    
    return doms


def update_descritores(id, dominiodescritoresmat: DominioDescritoresMat):
    """Atualiza um elemento no banco de dados com base no id ."""
    connection, cursor = connect_db()

    descritores = dominiodescritoresmat.return_list()

    
    print(len(descritores))  
    cursor.execute("""
        UPDATE dominio_descritores_mat
        SET aluno_id = ?, descritor_1 = ?, descritor_2 = ?, descritor_3 = ?, descritor_4 = ?, 
            descritor_5 = ?, descritor_6 = ?, descritor_7 = ?, descritor_8 = ?, descritor_9 = ?, 
            descritor_10 = ?, descritor_11 = ?, descritor_12 = ?, descritor_13 = ?, descritor_14 = ?, 
            descritor_15 = ?, descritor_16 = ?, descritor_17 = ?, descritor_18 = ?, descritor_19 = ?, 
            descritor_20 = ?, descritor_21 = ?, descritor_22 = ?, descritor_23 = ?, descritor_24 = ?, 
            descritor_25 = ?, descritor_26 = ?, descritor_27 = ?, descritor_28 = ?, descritor_29 = ?,
            descritor_30 = ?, descritor_31 = ?
        WHERE id = ?
    """, tuple(descritores) + (id,)) 

    connection.commit()
    connection.close()


descritores = ['{}'.format(1) for i in range(1, 32)]  # Lista de 29 descritores
dominio_descritores = DominioDescritoresMat(id=1, aluno_id=123, ds=descritores)

# Chamando a função para atualizar a base de dados
update_descritores(1, dominio_descritores)