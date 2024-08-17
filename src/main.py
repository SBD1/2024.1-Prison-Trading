import psycopg2

logo = """
 ██▓███   ██▀███   ██▓  ██████  ▒█████   ███▄    █    ▄▄▄█████▓ ██▀███   ▄▄▄      ▓█████▄  ██▓ ███▄    █   ▄████ 
▓██░  ██▒▓██ ▒ ██▒▓██▒▒██    ▒ ▒██▒  ██▒ ██ ▀█   █    ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██▒░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒   ██▒▒██   ██░▓██▒  ▐▌██▒   ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
▒██▒ ░  ░░██▓ ▒██▒░██░▒██████▒▒░ ████▓▒░▒██░   ▓██░     ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒      ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
░▒ ░       ░▒ ░ ▒░ ▒ ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░       ░      ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
░░         ░░   ░  ▒ ░░  ░  ░  ░ ░ ░ ▒     ░   ░ ░      ░        ░░   ░   ░   ▒    ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
            ░      ░        ░      ░ ░           ░                ░           ░  ░   ░     ░           ░       ░ 
                                                                                   ░                             
"""

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


    db.close()

