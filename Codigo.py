import sqlite3

conexao = sqlite3.connect("Franquias.db")
cursor = conexao.cursor()


cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Consoles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        fabricante TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        genero TEXT NOT NULL,
        preco INTEGER NOT NULL,
        console_id INTEGER NOT NULL,
        FOREIGN KEY (console_id) REFERENCES Consoles(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Avaliacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jogo_id INTEGER NOT NULL,
        nota INTEGER NOT NULL,
        comentario TEXT NOT NULL,
        FOREIGN KEY (jogo_id) REFERENCES Jogos(id)
    )
''')
def adicionar_console(nome,fabricante):
    cursor.execute("INSERT INTO Consoles (nome,fabricante) VALUES (?,?) ",(nome,fabricante))
    conexao.commit()
    print(f"O console {nome} foi adicionado corretamente!")

def adicionar_jogos(nome,genero,preco,console_id):
    cursor.execute("INSERT INTO Jogos (nome, genero, preco, console_id) VALUES (?, ?, ?, ?)", (nome, genero, preco, console_id))

    conexao.commit()
    print(f"O jogo {nome} foi adicionado com sucesso! Seu preço é de {preco} !")

def adicionar_avaliacoes(jogo_id,nota,comentario):
    cursor.execute("INSERT INTO Avaliacoes (jogo_id, nota, comentario) VALUES (?, ?, ?)", (jogo_id, nota, comentario))


    conexao.commit()
    print(f"Sua nota é de {nota}! O comentário em destaque é ''{comentario}''")


def listar_console():
    cursor.execute("SELECT * FROM Consoles")
    Consoles = cursor.fetchall()
    for Console in Consoles:
        print(Console)

def listar_jogo():
    cursor.execute("SELECT * FROM Jogos")
    Jogos = cursor.fetchall()
    for Jogo in Jogos:
        print(Jogo)

def listar_Avaliacoes():
    cursor.execute("SELECT * FROM Avaliacoes")
    Avaliacoes = cursor.fetchall()
    for Avaliacao in Avaliacoes:
        print(Avaliacao)


add_console = input("Você deseja adicionar um novo console? Digite 'S' para sim e 'N' para não: ").strip().upper()
if add_console == 'S':
    print("Adicionando console...")
    adicionar_console ("Xbox one","Flex")
    adicionar_console ("Playstation 5","Sony")
    adicionar_console("Nintendo Console","Nintendo")

elif add_console == 'N':
    print("Você desejou não adicionar um novo console.")

else:
    print("Comando errado, tente novamente.")
    conexao.close()


add_jogos = input("Você deseja adicionar algum novo jogo? Digite 'S' para sim e 'N' para não: ").strip().upper()
if add_jogos == 'S':
    print("Você desejou adicionar um novo jogo, adicionando...")
    adicionar_jogos("Devil may cry 5","Acão",65,1)
    adicionar_jogos("Read Dead Redemption 2","Drama",299,2)
    adicionar_jogos("Assasins Creed","Ação",30,3)

elif add_jogos == 'N':
    print("Você desejou não adicionar nenhum jogo.")

else:
    print("Comando inválido, tente novamente.")
    conexao.close()

add_avaliacoes = input("Você deseja adicionar alguma nova avaliação? Digite 'S' para sim e 'N' para não :").strip().upper()
if add_avaliacoes == 'S':
    print("Você desejou adicionar uma nova avaliação, adicionando...")
    adicionar_avaliacoes(1,7.5,"Jogo excelente, porém a história é muito fraca, não gosto da gameplay com o V também.")
    adicionar_avaliacoes(2,9,"Jogo excelente, gráficos bons, porém o realismo depois de um tempo jogando cansa, creio que poderia ter algo pra melhorar.")
    adicionar_avaliacoes(3,7,"Jogo muito bom, história interessante, mas ainda contém muito bugs, infelizmente a franquia não soube lidar muito bem com a nova engine.")

elif add_avaliacoes =='N':
    print("Você desejou não adicionar nada.")

else:
    print("Comando inválido, tente novamente.")

















conexao.close()
