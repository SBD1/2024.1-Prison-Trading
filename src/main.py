import psycopg2
import time
import pygame

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


if __name__ == "__main__":
    db = DatabaseConnection()
    db.connect()

    db.cursor.execute("""
        SELECT jog.lugar
        FROM jogador jog
        WHERE jog.id = 1;
    """)
    results = db.cursor.fetchall()
    lugar_atual = results[0][0]

    print("Bem-vindo, digite "
          "\n'ATUAL' - Para ver sua localização atual."
          "\n'MAPA' - Para ver os possíveis lugares onde você pode ir."
          "\n'PESSOAS' - Para ver as pessoas que estão no mesmo lugar que você."
          "\n'ITENS' - Para ver os itens que estão no mesmo lugar que você."
          "\n'MOVER + ' ' + ID' - Para se movimentar de um lugar para outro."
          "\n'HELP' - Para ver os possíveis comandos."
          "\n'SAIR' - Para fechar o jogo.")

    while True:
        user_input = input()

        if user_input == "ATUAL":
            db.cursor.execute("""
                SELECT lug.nome, lug.descricao
                FROM jogador jog
                LEFT JOIN lugar lug ON lug.id = jog.lugar
                WHERE jog.id = 1;
            """)
            resultado = db.cursor.fetchone()
            nome, descricao = resultado
            print(f"Lugar: {nome}\tDescrição: {descricao}")

        elif user_input == "MAPA":
            db.cursor.execute("""
               SELECT lug.id, lug.nome, reg.nome
               FROM lugar_origem_destino ori
               JOIN lugar lug ON ori.lugar_destino = lug.id
               JOIN regiao reg ON lug.regiao = reg.id
               WHERE ori.lugar_origem = %s
               ORDER BY lug.nome;
            """, (lugar_atual,))
            resultados = db.cursor.fetchall()
            print("Lugares conectados com sua posição atual:")
            for lugar in resultados:
                print(f"ID do Lugar: {lugar[0]} \tLugar: {lugar[1]} \tRegião: {lugar[2]}")

        elif user_input == "PESSOAS":
            db.cursor.execute("""
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
            """, (lugar_atual,))
            resultado = db.cursor.fetchall()
            print("Pessoas no lugar:")
            for resultado in resultado:
                print("Nome: " + resultado[0] + "\tTipo: " + resultado[1])


        elif user_input == "ITENS":
            db.cursor.execute("""
                SELECT COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
                FROM instancia_item ins
                LEFT JOIN arma arm ON arm.id = ins.item
                LEFT JOIN ferramenta fer ON fer.id = ins.item
                LEFT JOIN comida com ON com.id = ins.item
                LEFT JOIN medicamento med ON med.id = ins.item
                LEFT JOIN utilizavel uti ON uti.id = ins.item
                WHERE ins.lugar = %s
                ORDER BY nome;
            """, (lugar_atual,))
            resultado = db.cursor.fetchall()
            if resultado:
                print("Itens no lugar:")
                for resultado in resultado:
                    print(resultado)
            else:
                print("Nenhum item nessa sala.")

        elif user_input.startswith("MOVER "):

            _, lugar_id = user_input.split(maxsplit=1)
            print(f"Movendo para o lugar com ID: {lugar_id}")

        elif user_input == "HELP":
            print("Bem-vindo, digite "
                  "\n'ATUAL' - Para ver sua localização atual."
                  "\n'MAPA' - Para ver os possíveis lugares onde você pode ir."
                  "\n'PESSOAS' - Para ver as pessoas que estão no mesmo lugar que você."
                  "\n'ITENS' - Para ver os itens que estão no mesmo lugar que você."
                  "\n'MOVER + ' ' + ID' - Para se movimentar de um lugar para outro."
                  "\n'HELP' - Para ver os possíveis comandos."
                  "\n'SAIR' - Para fechar o jogo.")

        elif user_input == "SAIR":
            print("Obrigado por jogar o jogo.")
            break

        else:
            print("Comando desconhecido. Digite 'HELP' para ver os possíveis comandos.")


    db.close()
