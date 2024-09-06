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
              "\n'INFO' - Para ver as informações de um item."
              "\n'MOVER' + ' ' + ID - Para se movimentar de um lugar para outro."
              "\n'PEGAR' + ' ' + ID - Para pegar um item no chão."
              "\n'LARGAR' + ' ' + ID - Para largar um item do inventário no chão."
              "\n'LIVRO' - Para ver as fabricações."
              "\n'BRIGAR' - Para brigar contra um prisioneiro na prisão."
              "\n'CONSUMIR' + ' ' + ID - Para consumir um item."
              "\n'MALHAR' - Para malhar e ganhar força."
              "\n'HELP' - Para ver os possíveis comandos."
              "\n'TROCA' + ' ' + ID - Para abrir a interface de troca com uma pessoa."
              "\n'GANGUE' - Para entrar em uma gangue."
              "\n'RGANGUE' - Para sair de uma gangue."
              "\n'CRAFT' + ' ' + ID - Para realizar uma fabricação."
              "\n'VCRAFT' + ' ' + ID - Para ver todos os crafts com um item especifico."
              "\n'CLEAR' - Para limpar o terminal."
              "\n'SAIR' - Para fechar o jogo.")

    def lugar_at(self):
        query = db.execute_fetchone("SELECT id, nome, descricao FROM detalhes_lugar WHERE id_jogador = %s;", (self.id_jogador,))
        if query:
            return query

    def regiao_at(self):
        query = db.execute_fetchone("SELECT * FROM detalhes_regiao WHERE id_jogador = %s;", (self.id_jogador,))
        if query:
            return query

    def mapa(self):
        query = db.execute_fetchall("SELECT * FROM lugares_ori_des_detalhado WHERE lugar_origem = %s;", (self.lugar_atual,))
        if query:
            return query

    def pessoas(self):
        query = db.execute_fetchall("SELECT * FROM pessoas_lugar WHERE lugar = %s;", (self.lugar_atual,))
        if query:
            return query

    def itens(self):
        query = db.execute_fetchall("SELECT * FROM instancias_detalhadas WHERE lugar = %s;", (self.lugar_atual,))
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

    def info(self):
        nomeItem = str(input("\033[93mDigite nome do item: \033[0m"))
        query = db.execute_fetchall("SELECT * FROM info_item WHERE nome = %s;", (nomeItem,))
        if query:
            for resultado in query:
                if resultado[0] is not None:
                    tipo = resultado[10]
                    detalhes = f"{resultado[0]}\nTamanho: {resultado[1]}\n{resultado[2]}"
                    if tipo == "arma":
                        detalhes += f"\nDano: {resultado[3]}"
                    elif tipo == "ferramenta":
                        detalhes += f"\nUtilidade: {resultado[4]}"
                    elif tipo == "comida":
                        detalhes += f"\nRaridade: {resultado[5]}\nQuantidade: {resultado[6]}\nRecuperação de Vida: {resultado[7]}"
                    elif tipo == "medicamento":
                        detalhes += f"\nRaridade: {resultado[5]}\nQuantidade: {resultado[6]}\nCura: {resultado[8]}"
                    elif tipo == "utilizavel":
                        detalhes += f"\nRaridade: {resultado[5]}\nQuantidade: {resultado[6]}\nDurabilidade: {resultado[9]}"
                    print(detalhes)
        else:
            print("Nenhuma informação para ver.")

    def login(self):
        opcoes = ["\tENTRAR", "\tREGISTRAR", "\tCRÉDITOS", "\tSAIR"]
        opcao = self.criar_menu(opcoes)

        if opcao == 0:
            print("\033[92mÁREA DE LOGIN\n\033[0m")
            query = db.execute_fetchall("SELECT jog.id, jog.nome, jog.nivel FROM jogador jog ORDER BY jog.id;")
            if query:
                linha = "+----------------+---------------+--------------------------------------------------------------------+"
                print(linha)
                for resultado in query:
                    print(f'| ID: {resultado[0]:02}\t | Nível: {resultado[2]:02}\t | Nome: {resultado[1]} |')
                print(linha)
                self.id_jogador = input("\033[92mDigite o ID do jogador escolhido para selecioná-lo: \033[0m")
                query = db.execute_fetchone("SELECT nome FROM jogador WHERE id = %s;", (self.id_jogador,))
                if query:
                    print(f'\033[92mLogin realizado com sucesso. \nBem-vindo {query[0]}\033[0m')
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
        query = db.execute_fetchone("SELECT * FROM status_jogador WHERE id = %s;", (self.id_jogador,))
        if query:
            id, self.nome, self.habilidade_briga, self.vida, self.forca, self.tempo_vida, self.gangue, self.nivel, self.missao, self.lugar_atual, self.regiao_atual, tamanho, self.inventario_ocupado= query
            id, nome, descricao = self.lugar_at()
            id_reg, nome_reg, descricao_reg, a = self.regiao_at()

            print("\033[93m" + "+-" * (110 // 2) + "+")
            print(f'ID: {self.id_jogador}\t\t\tNível: {self.nivel} \t\tNome: {self.nome}')
            print(f'Gangue: {self.gangue}\t\tMissão: {self.missao}\t\tTempo de vida: {self.tempo_vida}/10')
            print(f'Vida: {self.vida}/10\t\tForça:{self.forca}/10\t\tHabilidade de briga: {self.habilidade_briga}/10\tInventário: {self.inventario_ocupado}/{tamanho}')
            print("+-" * (110 // 2) + "+" + "\033[0m")
            print("\033[92m" + "+-" * (110 // 2) + "+")
            print(f'ID: {id}\t\t\tNome: {nome}')
            descricao_formatada = textwrap.fill(descricao, width=100)
            print(f'Descrição: {descricao_formatada}')
            print("+-" * (110 // 2) + "+" + "\033[0m")
            print("\033[36m" + "+-" * (110 // 2) + "+")
            print(f'ID: {id_reg}\t\t\tNome: {nome_reg}')
            descricao_formatada = textwrap.fill(descricao_reg, width=100)
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
                    print(f'{resultado[0]:02} - {resultado[2]:02} - {resultado[1].strip()}')
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

            query = db.execute_fetchall("SELECT * FROM itens_inventario WHERE pessoa = %s;", (self.id_jogador,))
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

            self.move_cursor_to(0, 23)

    def mover(self, input_usuario):
        _, lugar_id = input_usuario.split(maxsplit=1)
        db.execute_commit("SELECT movimenta_jogador(%s, %s);", (self.id_jogador, lugar_id))

    def pegar(self, input_usuario):
        _, id_inst = input_usuario.split(maxsplit=1)
        db.execute_commit("SELECT pegar_item_chao(%s, %s);", (self.id_jogador, id_inst))

    def largar(self, input_usuario):
        _, id_inst = input_usuario.split(maxsplit=1)
        db.execute_commit("SELECT dropar_item_chao(%s, %s);", (self.id_jogador, id_inst))

    def brigar(self):
        query = db.execute_fetchall("SELECT * FROM status_prisioneiro;")
        if query:
            print("======================================================================")
            for resultado in query:
                print(f'| Nome: {resultado[1]} |')
                print(f'| ID: {resultado[0]:02}\tHabilidade: {resultado[2]:02}\t\tVida: {resultado[3]:02}\tForça: {resultado[4]:02}    |')
                print("======================================================================")

        id_prisioneiro = input("\033[93mDigite o ID do prisioneiro: \033[0m")
        db.execute_commit("SELECT combate(%s, %s)", (self.id_jogador, id_prisioneiro))
        self.clear()

    def livro(self):
        query = db.execute_fetchall("SELECT id, nome FROM livro_fabricacao", )
        if query:
            for resultado in query:
                print(f'ID: {resultado[0]}\tNome: {resultado[1]}')

        tipo_livro = input("\033[93mDigite o id do livro: \033[0m")
        query = db.execute_fetchall("SELECT * FROM itens_livro_fabricacao WHERE livro_fabricacao = %s;", (tipo_livro,))
        if query:
            for resultado in query:
                print(f'ID: {resultado[0]}\tNome: {resultado[1]}')

        id_item = input("\033[93mDigite o id do item que deseja visualizar a receita de fabricação: \033[0m")
        query = db.execute_fetchall("SELECT * FROM craft_item WHERE fabricacao = %s;", (id_item,))
        if query:
            print("\033[92m\nItens necessários:\033[93m")
            for resultado in query:
                print(f'\033[92m • {resultado[1]}\033[93m')

    def craft(self, input_usuario):
        _, id_item = input_usuario.split(maxsplit=1)
        db.execute_commit("SELECT realizar_craft(%s, %s);",(self.id_jogador, id_item))

    def consumir(self, input_usuario):
        _, id_item = input_usuario.split(maxsplit=1)
        db.execute_commit("SELECT consumir_item(%s, %s);",(self.id_jogador, id_item))

    def malhar(self):
        db.execute_commit("SELECT malhar_jogador(%s);", (self.id_jogador,))
        time.sleep(2)
        self.clear()

    def troca(self, input_usuario):
        _, id_pessoa = input_usuario.split(maxsplit=1)
        query = db.execute_fetchall("SELECT id, nome FROM itens_inventario WHERE pessoa = %s;",(id_pessoa,) )
        if query[0][0] is not None:
            print('+-----------------------------------------------+')
            for resultado in query:
                print(f'| ID: {resultado[0]}\tNome: {resultado[1]} |')
                print('+-----------------------------------------------+')
        else:
            print(f'\nA pessoa {id_pessoa} não possui itens no inventário.')
            return
        id_inst_pessoa = input("\033[93mDigite o ID do item que deseja: \033[0m")
        id_inst_jogador = input("\033[93mDigite o ID do item dará em troca: \033[0m")
        db.execute_commit("SELECT troca(%s, %s, %s, %s);", (self.id_jogador, id_pessoa, id_inst_jogador, id_inst_pessoa,))
        self.clear()

    def entrar_gangue(self):
        gangue = input("\033[93mDigite o nome do gangue [palhaco ou polvo]: \033[0m")
        db.execute_commit("SELECT selecionar_gangue(%s, %s);",(self.id_jogador, gangue,))
        self.clear()

    def sair_gangue(self):
        db.execute_commit("SELECT remover_gangue(%s);",(self.id_jogador,))
        self.clear()

    def ver_craft(self, input_usuario):
        _, id_inst = input_usuario.split(maxsplit=1)
        query = db.execute_fetchall("SELECT * FROM crafts_relacionados WHERE id = %s;", (id_inst,))
        if query[0][0] is not None:
            print('+---------------------------------------+')
            for resultado in query:
                print(f'| ID: {resultado[0]}\tNome: {resultado[1]} |')
                print('+---------------------------------------+')
        else:
            print(f'\nO item {id_inst} não está em nenhuma fabricação.')

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        if self.id_jogador != '':
            self.status_jogador()

    def gameLoop(self):
        comandos = {
            "HELP": self.help,
            "CLEAR": self.clear,
            "INFO": self.info,
            "LIVRO": self.livro,
            "BRIGAR": self.brigar,
            "MALHAR": self.malhar,
            "GANGUE": self.entrar_gangue,
            "RGANGUE": self.sair_gangue,
        }

        while True:
            if self.tempo_vida == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(logo)
                print('Você perdeu\n')
                break
            else:
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
                elif input_usuario.startswith("CRAFT "):
                    self.craft(input_usuario)
                    input("\n\033[93mPrecione qualquer tecla atualizar\033[0m")
                    self.clear()
                elif input_usuario.startswith("VCRAFT "):
                    self.ver_craft(input_usuario)
                    input("\n\033[93mPrecione qualquer tecla atualizar\033[0m")
                    self.clear()
                elif input_usuario.startswith("TROCA "):
                    self.troca(input_usuario)
                    input("\n\033[93mPrecione qualquer tecla atualizar\033[0m")
                    self.clear()
                elif input_usuario.startswith("CONSUMIR "):
                    self.consumir(input_usuario)
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