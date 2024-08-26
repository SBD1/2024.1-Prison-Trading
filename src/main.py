import psycopg2
import os
import sys
import time
import keyboard

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

    def help(self):
        print("Bem-vindo, digite "
              "\n'ATUAL' - Para ver sua localização atual."
              "\n'MAPA' - Para ver os possíveis lugares onde você pode ir."
              "\n'PESSOAS' - Para ver as pessoas que estão no mesmo lugar que você."
              "\n'ITENS' - Para ver os itens que estão no mesmo lugar que você."
              "\n'MOVER + ' ' + ID' - Para se movimentar de um lugar para outro."
              "\n'HELP' - Para ver os possíveis comandos."
              "\n'CLEAR' - Para limpar o terminal."
              "\n'SAIR' - Para fechar o jogo.")

    def atual(self):
        query = db.execute_fetchone("""
            SELECT lug.id, lug.nome, lug.descricao
            FROM jogador jog
            LEFT JOIN lugar lug ON lug.id = jog.lugar
            WHERE jog.id = 1;
        """)
        id, nome, descricao = query
        print(f"ID: {id}\tLugar: {nome}\tDescrição: {descricao}")

    def mapa(self):
        query = db.execute_fetchall("""
            SELECT lug.id, lug.nome, reg.nome
            FROM lugar_origem_destino ori
            JOIN lugar lug ON ori.lugar_destino = lug.id
            JOIN regiao reg ON lug.regiao = reg.id
            WHERE ori.lugar_origem = %s
            ORDER BY lug.nome;
        """, (self.lugar_atual,))
        print("Lugares conectados com sua posição atual:")
        for lugar in query:
            print(f"ID do Lugar: {lugar[0]} \tLugar: {lugar[1]} \tRegião: {lugar[2]}")

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
            SELECT pes.nome, tip.tipo
            FROM pessoas pes, pessoa tip
            WHERE pes.id = tip.id AND pes.lugar = %s
            ORDER BY tip.tipo, pes.nome;
        """, (self.lugar_atual,))
        print("Pessoas no lugar:")
        for resultado in query:
            print("Nome: " + resultado[0] + "\tTipo: " + resultado[1])

    def itens(self):
        query = db.execute_fetchall("""
            SELECT COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
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
            print("Itens no lugar:")
            for resultado in query:
                print(resultado[0])
        else:
            print("Nenhum item nessa sala.")

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

    def login(self):
        opcoes = ["\tENTRAR", "\tREGISTRAR", "\tCRÉDITOS", "\tSAIR"]
        opcao = self.criar_menu(opcoes)

        if opcao == 0:
            print("\033[92mLOGIN\n\033[0m")
            query = db.execute_fetchall("""
                SELECT jog.id, jog.nome, jog.nivel
                FROM jogador jog
                ORDER BY jog.id;
            """)
            if query:
                print("Jogadores disponíveis:")
                for resultado in query:
                    print(f'ID: {resultado[0]}\tNome: {resultado[1]}\tNível: {resultado[2]}')
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
            print("\033[92mREGISTRO\n\033[0m")

            nome = input("Digite o nome do jogador: ")

            db.execute_commit("""
                BEGIN;
                INSERT INTO pessoa (tipo)
                VALUES ('jogador')
                RETURNING id;

                DO $$ 
                DECLARE 
                    novo_id INT;
                BEGIN
                    SELECT MAX(id) INTO novo_id FROM pessoa;
                    INSERT INTO jogador (id, nome, habilidade_briga, vida, forca, tempo_vida, gangue, nivel, missao, lugar, regiao)
                    VALUES (novo_id, %s, 2, 5, 3, 10, NULL, 0, NULL, 2, 1);
                END $$;
                COMMIT;
            """, (nome,))
            print("\033[92mJogador salvo com sucesso.\033[0m")
            time.sleep(3)
            self.clear()
            return self.login()

        elif opcao == 2:
            print("\033[92mCRÉDITOS\033[0m\n")
            print("Prison Trading é um jogo de trocas baseado em 'The Escapists',"
                  "\ncriado no semestre 2024-1 na disciplina Sistema de Banco de Dados 1 com professor Mauricio Serrano."
                  "\n\n\033[94mFundadores do jogo:\033[0m\n"
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


    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)


    def gameLoop(self):
        comandos = {
            "ATUAL": self.atual,
            "MAPA": self.mapa,
            "PESSOAS": self.pessoas,
            "ITENS": self.itens,
            "HELP": self.help,
            "CLEAR": self.clear
        }

        while True:
            input_usuario = input('\033[91mDigite o comando: \033[0m').strip().upper()
            if input_usuario.startswith("MOVER "):
                self.mover(input_usuario)
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
