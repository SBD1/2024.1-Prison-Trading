import psycopg2
import os
import sys
import time
import keyboard
import textwrap


os.system(f"mode con: cols=168 lines=40")

logo = """\033[91m

  ██████╗ ██████╗ ██╗███████╗ ██████╗ ███╗   ██╗    ████████╗██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗
  ██╔══██╗██╔══██╗██║██╔════╝██╔═══██╗████╗  ██║    ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝
  ██████╔╝██████╔╝██║███████╗██║   ██║██╔██╗ ██║       ██║   ██████╔╝███████║██║  ██║██║██╔██╗ ██║██║  ███╗
  ██╔═══╝ ██╔══██╗██║╚════██║██║   ██║██║╚██╗██║       ██║   ██╔══██╗██╔══██║██║  ██║██║██║╚██╗██║██║   ██║
  ██║     ██║  ██║██║███████║╚██████╔╝██║ ╚████║       ██║   ██║  ██║██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝
  ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝
\033[0m"""


class DatabaseConnection:
    def __init__(self):
        self.database = "Prison-Trading"
        self.user = "prison_trading_user"
        self.password = "123"
        self.host = "localhost"
        self.port = "5432"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print(logo)
        except Exception as error:
            print("Erro ao conectar ou consultar o banco de dados:", error)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute_fetchone(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Exception as error:
            print("Erro ao executar a consulta:", error)
            return None

    def execute_fetchall(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as error:
            print("Erro ao executar a consulta:", error)
            return None

    def execute_commit(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("\033[92mAlterações salvas no banco de dados.\033[0m")
        except Exception as error:
            print("\033[91mErro ao executar e salvar a consulta:\033[0m", error)
            self.connection.rollback()

db = DatabaseConnection()

class Game:
    def __init__(self):
        self.id_jogador = ''
        self.lugar_atual = ''
        self.regiao_atual = ''
        self.nome = ''
        self.habilidade_briga = ''
        self.vida = ''
        self.forca = ''
        self.tempo_vida = ''
        self.gangue = ''
        self.missao = ''
        self.nivel = ''
        self.inventario_ocupado = ''

    def help(self):
        print("Bem-vindo, digite "
              "\n'INVENTARIO' - Para ver os itens que estão no seu inventário."
              "\n'INFO' - Para ver as informações de um item."
              "\n'MOVER + ' ' + ID' - Para se movimentar de um lugar para outro."
              "\n'PEGAR + ' ' + ID' - Para pegar um item no chão."
              "\n'LARGAR + ' ' + ID' - Para largar um item do inventário no chão."
              "\n'HELP' - Para ver os possíveis comandos."
              "\n'CLEAR' - Para limpar o terminal."
              "\n'SAIR' - Para fechar o jogo.")

    def atual(self):
        query = db.execute_fetchone("""
            SELECT lug.id, lug.nome, lug.descricao
            FROM jogador jog
            LEFT JOIN lugar lug ON lug.id = jog.lugar
            WHERE jog.id = %s;
        """, (self.id_jogador,))
        if query:
            return query

    def mapa(self):
        query = db.execute_fetchall("""
            SELECT lug.id, lug.nome
            FROM lugar_origem_destino ori
            JOIN lugar lug ON ori.lugar_destino = lug.id
            JOIN regiao reg ON lug.regiao = reg.id
            WHERE ori.lugar_origem = %s
            ORDER BY lug.nome;
        """, (self.lugar_atual,))
        if query:
            return query

    def pessoas(self):
        query = db.execute_fetchall("""
            WITH Pessoas AS (
                SELECT id, nome, lugar FROM jogador
                UNION ALL
                SELECT id, nome, lugar FROM policial
                UNION ALL
                SELECT id, nome, lugar FROM prisioneiro
                UNION ALL
                SELECT id, nome, lugar FROM informante
            )
            SELECT pes.nome, tip.tipo, pes.id
            FROM pessoas pes, pessoa tip
            WHERE pes.id = tip.id AND pes.lugar = %s
            ORDER BY tip.tipo, pes.id;
        """, (self.lugar_atual,))
        if query:
            return query

    def itens(self):
        query = db.execute_fetchall("""
            SELECT ins.id, COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
            FROM instancia_item ins
            LEFT JOIN arma arm ON arm.id = ins.item
            LEFT JOIN ferramenta fer ON fer.id = ins.item
            LEFT JOIN comida com ON com.id = ins.item
            LEFT JOIN medicamento med ON med.id = ins.item
            LEFT JOIN utilizavel uti ON uti.id = ins.item
            WHERE ins.lugar = %s
            ORDER BY nome;
        """, (self.lugar_atual,))
        if query:
            return query

    def criar_menu(self, opcoes):
        opcao = 0
        opcao_anterior = -1
        tam = len(opcoes)
        while True:
            if opcao != opcao_anterior:
                self.clear()
                for i, opc in enumerate(opcoes):
                    if i == opcao:
                        print(f"\033[93m{opc}\033[0m")
                    else:
                        print(opc)
                opcao_anterior = opcao
            if keyboard.is_pressed('down') or keyboard.is_pressed('s'):
                opcao = (opcao + 1) % tam
                time.sleep(0.2)
            elif keyboard.is_pressed('up') or keyboard.is_pressed('w'):
                opcao = (opcao - 1) % tam
                time.sleep(0.2)
            elif keyboard.is_pressed('enter'):
                input()
                self.clear()
                return opcao

    def inventario(self):
        query = db.execute_fetchall("""
            SELECT COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome, i.inventario_ocupado, i.tamanho
            FROM inventario AS i
            LEFT JOIN instancia_item AS t ON i.id = t.inventario
            LEFT JOIN arma AS arm ON arm.id = t.item
            LEFT JOIN ferramenta AS fer ON fer.id = t.item
            LEFT JOIN comida AS com ON com.id = t.item
            LEFT JOIN medicamento AS med ON med.id = t.item
            LEFT JOIN utilizavel AS uti ON uti.id = t.item
            WHERE i.pessoa = %s
            ORDER BY nome;
        """, (self.id_jogador,))

        if query:
            print("Inventário:")
            print("Tamanho do Inventário: " + str(query[0][2]) + "\tTamanho Ocupado: " + str(query[0][1]))
            for resultado in query:
                if query[0][0] is not None:
                    print(resultado[0])
        if any(resultado[0] is None for resultado in query):
            print("Nenhum item no inventário.")

    def info(self):
        nomeItem = str(input("Digite nome do item: "))

        query = db.execute_fetchall("""
            SELECT COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome,
                   COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho) AS tamanho,
                   COALESCE(arm.descricao, fer.descricao, com.descricao, med.descricao, uti.descricao) AS descricao,
                   arm.dano AS dano,
                   fer.utilidade AS utilidade,
                   COALESCE(com.raridade, med.raridade, uti.raridade) AS raridade,
                   COALESCE(com.quantidade, med.quantidade, uti.quantidade) AS quantidade,
                   com.recuperacao_vida AS recuperacao_vida,
                   med.cura AS cura,
                   uti.durabilidade AS durabilidade,
                   CASE
                        WHEN arm.nome IS NOT NULL THEN 'arma'
                        WHEN fer.nome IS NOT NULL THEN 'ferramenta'
                        WHEN com.nome IS NOT NULL THEN 'comida'
                        WHEN med.nome IS NOT NULL THEN 'medicamento'
                        WHEN uti.nome IS NOT NULL THEN 'utilizavel'
                   ELSE 'desconhecido'
               END AS tipo
            FROM inventario AS i
            LEFT JOIN instancia_item AS t ON i.id = t.inventario
            LEFT JOIN arma AS arm ON arm.id = t.item
            LEFT JOIN ferramenta AS fer ON fer.id = t.item
            LEFT JOIN comida AS com ON com.id = t.item
            LEFT JOIN medicamento AS med ON med.id = t.item
            LEFT JOIN utilizavel AS uti ON uti.id = t.item
            WHERE i.pessoa = %s AND COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) = %s
        """, (self.id_jogador, nomeItem,))

        if query:
            for resultado in query:
                if resultado[0] is not None:
                    if resultado[10] == "arma":
                        print(resultado[0] + "\nTamanho: " + str(resultado[1]) + "\n" + resultado[2] + "\nDano: " + str(
                            resultado[3]))
                    if resultado[10] == "ferramenta":
                        print(resultado[0] + "\nTamanho: " + str(resultado[1]) + "\n" + resultado[
                            2] + "\nUtilidade: " + str(resultado[4]))
                    if resultado[10] == "comida":
                        print(resultado[0] + "\nTamanho: " + str(resultado[1]) + "\n" + resultado[
                            2] + "\nRaridade: " + str(resultado[5]) + "\nQuantidade: " + str(
                            resultado[6]) + "\nRecuperacao de Vida: " + str(resultado[7]))
                    if resultado[10] == "medicamento":
                        print(resultado[0] + "\nTamanho: " + str(resultado[1]) + "\n" + resultado[
                            2] + "\nRaridade: " + str(resultado[5]) + "\nQuantidade: " + str(
                            resultado[6]) + "\nCura: " + str(resultado[8]))
                    if resultado[10] == "utilizavel":
                        print(resultado[0] + "\nTamanho: " + str(resultado[1]) + "\n" + resultado[
                            2] + "\nRaridade: " + str(resultado[5]) + "\nQuantidade: " + str(
                            resultado[6]) + "\nDurabilidade: " + str(resultado[9]))
        else:
            print("Nenhuma informação para ver.")

    def login(self):
        opcoes = ["\tENTRAR", "\tREGISTRAR", "\tCRÉDITOS", "\tSAIR"]
        opcao = self.criar_menu(opcoes)

        if opcao == 0:
            print("\033[92mÁREA DE LOGIN\n\033[0m")
            query = db.execute_fetchall("""
                SELECT jog.id, jog.nome, jog.nivel
                FROM jogador jog
                ORDER BY jog.id;
            """)
            if query:
                print("+----------------+---------------+--------------------------------------------------------------------+")
                for resultado in query:
                    print(f'| ID: {resultado[0]:02}\t | Nível: {resultado[2]:02}\t | Nome: {resultado[1]} |')
                print("+----------------+---------------+--------------------------------------------------------------------+")
                self.id_jogador = input("\033[92mDigite o ID do jogador escolhido para selecioná-lo: \033[0m")
                query = db.execute_fetchone("""
                    SELECT jog.nome, jog.lugar, jog.regiao
                    FROM jogador jog
                    WHERE jog.id = %s;
                """, (self.id_jogador,))
                if query:
                    nome, self.lugar_atual, self.regiao_atual = query
                    print(f'\033[92mLogin realizado com sucesso. \nBem-vindo {nome}\033[0m')
                    time.sleep(3)
                    self.clear()
                    return
                else:
                    print("\033[91mID de jogador não encontrado.\033[0m")
                    return self.login()

        elif opcao == 1:
            print("\033[92mÁREA DE REGISTRO\n\033[0m")
            nome = input("Digite o nome do jogador: ")
            db.execute_commit("""
                INSERT INTO jogador (id, nome, habilidade_briga, vida, forca, tempo_vida, gangue, nivel, missao, lugar, regiao)
                VALUES (1, %s, 2, 5, 3, 10, NULL, 0, NULL, 2, 1);
            """, (nome,))
            print("\033[92mJogador salvo com sucesso.\033[0m")
            time.sleep(3)
            self.clear()
            return self.login()

        elif opcao == 2:
            print("\033[92mCRÉDITOS\033[0m\n")
            print("Prison Trading é um jogo de trocas baseado em 'The Escapists',"
                  "\ncriado no semestre 2024-1 na disciplina Sistema de Banco de Dados 1 com professor Mauricio Serrano."
                  "\n\n\033[97mFundadores do jogo:\033[0m\n"
                  "\n Breno Alexandre Soares Garcia - 200035703"
                  "\n Fernando Gabriel dos Santos Carrijo - 221008033"
                  "\n João Antonio Ginuino Carvalho - 221008150"
                  "\n Júlio Cesar Gomes de Souza Crispim - 221007591")
            input("\n\033[93mPrecione qualquer tecla para sair\033[0m")
            time.sleep(1)
            self.clear()
            return self.login()

        elif opcao == 3:
            print("\033[92mObrigado por jogar :)\033[0m")
            sys.exit(0)

    def move_cursor_to(self, x, y):
        print(f"\033[{y};{x}H", end='')

    def status_jogador(self):
        query = db.execute_fetchone("""
            SELECT j.nome, j.habilidade_briga, j.vida, j.forca, j.tempo_vida, j.gangue, j.nivel, j.missao, j.lugar, j.regiao, i.tamanho, i.inventario_ocupado
            FROM jogador j
            JOIN inventario i ON i.pessoa = j.id
            WHERE j.id = %s;
        """, (self.id_jogador,))
        if query:
            self.nome, self.habilidade_briga, self.vida, self.forca, self.tempo_vida, self.gangue, self.nivel, self.missao, self.lugar_atual, self.regiao_atual, tamanho, self.inventario_ocupado= query
            id, nome, descricao = self.atual()

            print("\033[93m" + "+-" * (110 // 2) + "+")
            print(f'ID: {self.id_jogador}\t\t\tNível: {self.nivel} \t\tNome: {self.nome}')
            print(f'Gangue: {self.gangue}\t\tMissão: {self.missao}\t\tTempo de vida: {self.tempo_vida}/10')
            print(f'Vida: {self.vida}/10\t\tForça:{self.forca}/10\t\tHabilidade de briga: {self.habilidade_briga}/10\tInventário: {self.inventario_ocupado}/{tamanho}')
            print("+-" * (110 // 2) + "+" + "\033[0m")
            print("\033[36m" + "+-" * (110 // 2) + "+")
            print(f'ID: {id}\t\t\tNome: {nome}')
            descricao_formatada = textwrap.fill(descricao, width=100)
            print(f'Descrição: {descricao_formatada}')
            print("+-" * (110 // 2) + "+" + "\033[0m")

            linha_atual = 1
            for i in range(40):
                self.move_cursor_to(112, i)
                print("\033[91m||\033[0m")
            self.move_cursor_to(114, linha_atual)
            print("\033[91m======================================================\033[0m")
            linha_atual+=1
            self.move_cursor_to(115, linha_atual)
            print("\t\tPESSOAS NO LUGAR:")
            linha_atual+=2
            pessoas = self.pessoas()
            for resultado in pessoas:
                self.move_cursor_to(115, linha_atual)
                if resultado[1] == "policial":
                    print(f'\033[96m{resultado[2]:02} - {resultado[0].strip()}\033[0m')
                else:
                    print(f'\033[93m{resultado[2]:02} - {resultado[0].strip()}\033[0m')
                linha_atual+=1
            linha_atual += 1
            self.move_cursor_to(114, linha_atual)
            print("\033[91m======================================================\033[0m")

            linha_atual += 1
            self.move_cursor_to(115, linha_atual)
            print("\t\tITENS NO LUGAR:")
            linha_atual += 2
            itens = self.itens()
            if itens:
                for resultado in itens:
                    self.move_cursor_to(115, linha_atual)
                    print(f'{resultado[0]:02} - {resultado[1].strip()}')
                    linha_atual += 1
            else:
                self.move_cursor_to(115, linha_atual)
                print(f'Nenhum item nesse lugar.')
                linha_atual += 1
            linha_atual += 1
            self.move_cursor_to(114, linha_atual)
            print("\033[91m======================================================\033[0m")

            linha_atual += 1
            self.move_cursor_to(115, linha_atual)
            print("\t\tLUGARES CONECTADOS:")
            linha_atual += 2
            mapa = self.mapa()
            for resultado in mapa:
                self.move_cursor_to(115, linha_atual)
                print(f'{resultado[0]:02} - {resultado[1].strip()}')
                linha_atual += 1
            linha_atual += 1
            self.move_cursor_to(114, linha_atual)
            print("\033[91m======================================================\033[0m")

            query = db.execute_fetchall("""
                SELECT t.id, COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
                FROM inventario AS i
                LEFT JOIN instancia_item AS t ON i.id = t.inventario
                LEFT JOIN arma AS arm ON arm.id = t.item
                LEFT JOIN ferramenta AS fer ON fer.id = t.item
                LEFT JOIN comida AS com ON com.id = t.item
                LEFT JOIN medicamento AS med ON med.id = t.item
                LEFT JOIN utilizavel AS uti ON uti.id = t.item
                WHERE i.pessoa = %s
                ORDER BY nome;
            """, (self.id_jogador,))
            linha_atual += 1
            self.move_cursor_to(115, linha_atual)
            print("\t\tINVENTÁRIO:")
            linha_atual += 2
            if query[0][0] is not None:
                for resultado in query:
                    self.move_cursor_to(115, linha_atual)
                    print(f'{resultado[0]:02} - {resultado[1].strip()}')
                    linha_atual += 1
            else:
                self.move_cursor_to(115, linha_atual)
                print(f'Inventário vazio.')
                linha_atual += 1
            linha_atual += 1
            self.move_cursor_to(114, linha_atual)
            print("\033[91m======================================================\033[0m")

            self.move_cursor_to(0, 20)

    def mover(self, input_usuario):
        _, lugar_id = input_usuario.split(maxsplit=1)

        query = db.execute_fetchall("""
            SELECT lug.id
            FROM lugar_origem_destino ori
            JOIN lugar lug ON ori.lugar_destino = lug.id
            JOIN regiao reg ON lug.regiao = reg.id
            WHERE ori.lugar_origem = %s
            ORDER BY lug.nome;
        """, (self.lugar_atual,))

        verifica = any(str(resultado[0]) == lugar_id for resultado in query)

        if verifica:
            query = db.execute_fetchall("""
               SELECT regiao
               FROM lugar
               WHERE id = %s;
            """, (lugar_id,))
            regiao = query[0][0]

            db.execute_commit("""
                UPDATE Jogador
                SET lugar = %s, regiao = %s
                WHERE id = 1;
            """, (lugar_id, regiao))

            self.lugar_atual = lugar_id
            self.regiao_atual = regiao
            print("Posição movida com sucesso.")
        else:
            print("A sala atual não possui conexões com a que o jogador digitou.")

    def pegar(self, input_usuario):
        _, id_inst = input_usuario.split(maxsplit=1)
        db.execute_commit("""
            SELECT pegar_item_chao(%s, %s);
        """, (self.id_jogador, id_inst))

    def largar(self, input_usuario):
        _, id_inst = input_usuario.split(maxsplit=1)
        db.execute_commit("""
            SELECT dropar_item_chao(%s, %s);
        """, (self.id_jogador, id_inst))

    def livro(self):
        # TODO ADICIONAR AS VIEWS DE CRAFT
        query = db.execute_fetchall("""
           SELECT id, nome
           FROM livro_fabricacao
        """, )
        if query:
            for resultado in query:
                print(f'ID: {resultado[0]}\tNome: {resultado[1]}')

        tipo_livro = input("Digite o id do livro: ")

        query = db.execute_fetchall("""
            SELECT fabricacao.id, COALESCE(arma.nome, ferr.nome) AS nome
            FROM fabricacao
            LEFT JOIN arma arma ON fabricacao.item_fabricavel = arma.id
            LEFT JOIN ferramenta ferr ON fabricacao.item_fabricavel = ferr.id
            WHERE fabricacao.livro_fabricacao = %s
            ORDER BY fabricacao.id;
        """, (tipo_livro,))
        if query:
            for resultado in query:
                print(f'ID: {resultado[0]}\tNome: {resultado[1]}')

        id_item = input("Digite o id do item que deseja visualizar a receita de fabricação: ")

        query = db.execute_fetchall("""
            SELECT COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
            FROM lista_fabricacao AS t
            LEFT JOIN arma AS arm ON arm.id = t.item
            LEFT JOIN ferramenta AS fer ON fer.id = t.item
            LEFT JOIN comida AS com ON com.id = t.item
            LEFT JOIN medicamento AS med ON med.id = t.item
            LEFT JOIN utilizavel AS uti ON uti.id = t.item
            WHERE t.item_fabricavel = %s;
        """, (id_item,))
        if query:
            for resultado in query:
                print(f'Nome: {resultado[0]}')

    def craft(self):
        id_item = input("Digite o id da fabricação: ")
        db.execute_commit("""
            SELECT realizar_craft(%s, %s);
        """, (self.id_jogador, id_item))

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.id_jogador != '':
            print("\n\n")
        print(logo)
        if self.id_jogador != '':
            self.status_jogador()

    def gameLoop(self):
        comandos = {
            "HELP": self.help,
            "CLEAR": self.clear,
            "INVENTARIO": self.inventario,
            "INFO": self.info,
            "LIVRO": self.livro,
            "CRAFT": self.craft,
        }

        while True:
            input_usuario = input('\033[91mDigite o comando: \033[0m').strip().upper()
            if input_usuario.startswith("MOVER "):
                self.mover(input_usuario)
                input("\n\033[93mPrecione qualquer tecla atualizar\033[0m")
                self.clear()
            elif input_usuario.startswith("PEGAR "):
                self.pegar(input_usuario)
                input("\n\033[93mPrecione qualquer tecla atualizar\033[0m")
                self.clear()
            elif input_usuario.startswith("LARGAR "):
                self.largar(input_usuario)
                input("\n\033[93mPrecione qualquer tecla atualizar\033[0m")
                self.clear()
            elif input_usuario == "SAIR":
                break
            elif input_usuario in comandos:
                comandos[input_usuario]()
            else:
                print("Opção inválida, digite 'HELP' para ver os comandos suportados.")

    def start(self):
        self.clear()
        self.login()
        self.gameLoop()


Prison_Tradign = Game()
db.connect()
Prison_Tradign.start()
db.close()
