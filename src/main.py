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
          "\n'MOVER + ' ' + ID' - Para se movimentar de um lugar para outro."
          "\n'HELP' - Para ver os possíveis comandos.")

    while True:
        user_input = input()

        if user_input == "ATUAL":
            db.cursor.execute("""
                SELECT lug.nome, lug.descricao, jog.lugar
                FROM jogador jog
                LEFT JOIN lugar lug ON lug.id = jog.lugar
                WHERE jog.id = 1;
            """)
            resultado = db.cursor.fetchall()
            print(resultado)

        elif user_input == "MAPA":
            db.cursor.execute("""
               SELECT lug.nome, reg.nome
               FROM lugar_origem_destino ori
               JOIN lugar lug ON ori.lugar_destino = lug.id
               JOIN regiao reg ON lug.regiao = reg.id
               WHERE ori.lugar_origem = %s
               ORDER BY lug.nome;
            """, (lugar_atual,))
            resultado = db.cursor.fetchall()
            headers = ["Lugar", "Região"]
            print(tabulate(resultado, headers=headers, tablefmt="grid"))

        elif user_input.startswith("MOVER "):

            _, lugar_id = user_input.split(maxsplit=1)
            print(f"Movendo para o lugar com ID: {lugar_id}")

        elif user_input == "HELP":
            print("Bem-vindo, digite "
                  "\n'MAPA' - Para ver os possíveis lugares onde você pode ir."
                  "\n'MOVER + ' ' + ID' - Para se movimentar de um lugar para outro."
                  "\n'HELP' - Para ver os possíveis comandos.")
        else:
            print("Comando desconhecido. Digite 'HELP' para ver os possíveis comandos.")

    db.close()
