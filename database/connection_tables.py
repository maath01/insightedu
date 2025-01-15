
def turmas_alunos(turma_id, aluno_id, cursor, connection):
    """Associa uma turma e um aluno"""
    cursor.execute('INSERT INTO turmas_alunos (turmas_id, alunos_id) VALUES (?, ?)', (turma_id, aluno_id))

    connection.commit()

def professores_turmas_materias(professor_id, turma_id, materia_id, cursor, connection):
    """Associa uma turma a professores e os professores a materias"""
    cursor.execute('INSERT INTO professores_turmas_materias (professores_id, turmas_id, materias_id) VALUES (?, ?, ?)',
                    (professor_id,turma_id, materia_id))
    
    connection.commit()


def escolas_gestores(escola_id, gestor_id, cursor, connection):
    """Associa uma escola e um gestor"""
    cursor.execute('INSERT INTO escolas_gestores (escolas_id, gestores_id) VALUES (?, ?)', (escola_id, gestor_id))

    connection.commit()


def escolas_turmas(escola_id, turma_id, cursor, connection):
    """Associa uma escola e uma turma"""
    cursor.execute('INSERT INTO escolas_turmas (escolas_id, turmas_id) VALUES (?, ?)', (escola_id, turma_id))

    connection.commit()


def escolas_coordenadores(escola_id, coordenador_id, cursor, connection):
    """Associa uma escola e um coordenador"""
    cursor.execute('INSERT INTO escolas_coordenadores (escolas_id, coordenadores_id) VALUES (?, ?)', (escola_id, coordenador_id))

    connection.commit()


def escolas_professores(escola_id, professor_id, cursor, connection):
    """Associa uma escola e um professor"""
    cursor.execute('INSERT INTO escolas_professores (escolas_id, professores_id) VALUES (?, ?)', (escola_id, professor_id))

    connection.commit()


def escolas_alunos(escola_id, aluno_id, cursor, connection):
    """Associa uma escola e um aluno"""
    cursor.execute('INSERT INTO escolas_alunos (escolas_id, alunos_id) VALUES (?, ?)', (escola_id, aluno_id))

    connection.commit()


def coordenadores_turmas(coordenador_id, turma_id, cursor, connection):
    """Associa um coordenador a uma turma"""
    cursor.execute('INSERT INTO coordenadores_turmas (coordenadores_id, turmas_id) VALUES (?, ?)', (coordenador_id, turma_id))

    connection.commit()


def materias_avaliacoes(materia, avaliacao_id, cursor, connection):
    """Associa uma avaliação a uma materia"""
    cursor.execute('SELECT id FROM materias WHERE nome = ?', (materia,))
    id_materia = cursor.fetchall()[0][0]

    cursor.execute('INSERT INTO materias_avaliacoes (materias_id, avaliacoes_id) VALUES (?, ?)', (id_materia, avaliacao_id))

    connection.commit()