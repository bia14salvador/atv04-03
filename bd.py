import sqlite3


def cria_tabela():
    conn = sqlite3.connect('listadelivros.bd')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS listadelivros(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(55) NOT NULL,
            tempoDeLeitura VARCHAR(15) NOT NULL,
            genero VARCHAR(20) NOT NULL,
            paginas VARCHAR(10) NOT NULL,
            autor VARCHAR (30)NOT NULL,
        );
    """)
    conn.close()
    def nova_lista_de_livros(nome, tempoDeLeitura, genero, paginas, autor):
     conn = sqlite3.connect('listadelivros.bd')
     cursor = conn.cursor()

    def nova_lista_de_livros(nome, tempoDeLeitura, genero, paginas, autor):
     conn = sqlite3.connect('listadelivros.bd')
     cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO listadelivros(nome, tempoDeLeitura, genero, paginas, autor)
        VALUES('{nome}', '{tempoDeLeitura}', {genero}, {paginas}, {autor});
    """)
    conn.commit()
    conn.close()

def listar_livros():
    conn = sqlite3.connect('listadelivros.bd')
    cursor = conn.cursor()
    values = cursor.execute("SELECT * FROM listadelivros")
    resultado = []
    for item in values.fetchall():
        resultado.append({
            'id': item[0],
            'nome': item[1],
            'tempoDeLeitura': item[2],
            'genero': item[3],
            'paginas': item[4],
            'autor': item[5]
        })
    print(resultado)
    conn.close()
    return resultado

