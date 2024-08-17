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


class Game:
    def __init__(self, largura=900, altura=600, limiteFPS=100):
        pygame.init()
        self.largura = largura
        self.altura = altura
        self.limiteFPS = limiteFPS
        self.ticks = 1000 / limiteFPS
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Prison Trading")
        self.isrunning = True
        self.titulo = pygame.font.Font(None, 36)
        self.subtitulo = pygame.font.Font(None, 20)
        self.fps = 0
        self.clock = pygame.time.Clock()
        self.proximo_tick = pygame.time.get_ticks()
        self.db = DatabaseConnection()

        # ----- INFO DO JOGO ------- #
        self.lugar_atualID = ""
        self.lugar_atual = ""
        self.descricao_lugar_atual = ""
        self.lugares = []
        self.itens = []
        self.itens = ""

    def update(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.isrunning = False

    def render(self):
        self.tela.fill((0, 0, 0))

        fps_texto = self.titulo.render(f'FPS: {self.fps:.0f}', True, (255, 255, 255))
        self.tela.blit(fps_texto, (10, 10))

        lugar_texo = self.titulo.render(f'{self.lugar_atual}', True, (255, 255, 255))
        descricao_lugar_texto = self.subtitulo.render(f'{self.descricao_lugar_atual}', True, (255, 255, 255))
        self.tela.blit(lugar_texo, (10, 500))
        self.tela.blit(descricao_lugar_texto, (10, 550))

        y_offset = 150
        for lugar, regiao in self.lugares:
            lugar_texto = self.subtitulo.render(f'{lugar} - {regiao}', True, (255, 255, 255))
            self.tela.blit(lugar_texto, (10, y_offset))
            y_offset += 30

        pygame.display.flip()

    def main(self):
        while self.isrunning:
            self.update()
            self.fps = self.clock.get_fps()
            self.render()
            self.proximo_tick += self.ticks
            sleep_time = self.proximo_tick - pygame.time.get_ticks()
            if sleep_time > 0:
                time.sleep(sleep_time / 1000.0)
            self.clock.tick(self.limiteFPS)
        pygame.quit()

    def atualizaItens(self):

        self.db.cursor.execute("""
            SELECT COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
            FROM instancia_item ins
            LEFT JOIN arma arm ON arm.id = ins.item
            LEFT JOIN ferramenta fer ON fer.id = ins.item
            LEFT JOIN comida com ON com.id = ins.item
            LEFT JOIN medicamento med ON med.id = ins.item
            LEFT JOIN utilizavel uti ON uti.id = ins.item
            WHERE ins.lugar = %s
            ORDER BY COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome);
        """, (self.lugar_atualID,))
        resultado = self.db.cursor.fetchall()

        print(resultado)




    def atualizarLugar(self):

        self.db.cursor.execute("""
            SELECT lug.nome, lug.descricao, jog.lugar
            FROM jogador jog
            LEFT JOIN lugar lug ON lug.id = jog.lugar
            WHERE jog.id = 1;
        """)

        resultado = self.db.cursor.fetchone()
        if resultado:
            lugar_atual, descricao_lugar_atual, lugar_atual_id = resultado
            self.lugar_atual = lugar_atual.strip()
            self.descricao_lugar_atual = descricao_lugar_atual.strip()
            self.lugar_atualID = lugar_atual_id

            self.db.cursor.execute("""
                SELECT lug.nome, reg.nome
                FROM lugar_origem_destino ori
                JOIN lugar lug ON ori.lugar_destino = lug.id
                JOIN regiao reg ON lug.regiao = reg.id
                WHERE ori.lugar_origem = %s
                ORDER BY lug.nome;
            """, (lugar_atual_id,))

            resultado = self.db.cursor.fetchall()
            self.lugares = [[lugar.strip(), regiao.strip()] for lugar, regiao in resultado]

    def start(self):
        self.db.connect()
        self.atualizarLugar()
        self.atualizaItens()
        self.main()
        self.db.close()



if __name__ == "__main__":
    prison_trading = Game()
    prison_trading.start()
