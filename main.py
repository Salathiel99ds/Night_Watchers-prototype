import pygame 
from game_over import TelaMorte
from jogador import Jogador
from mapa import Mapa

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((960,540))
        pygame.display.set_caption("Night Watchers")

        self.relogio = pygame.time.Clock()
        self.fps = 144
        self.rodando = True
        self.estado = "inicio"

        self.fonte = pygame.font.SysFont("Arial", 36)
        self.tela_morte = TelaMorte()
        self.jogador = Jogador(464, 254)
        self.mapa = Mapa()
        self.obstaculos = self.mapa.obstaculos

        # coletáveis
        self.tem_cracha = False
        self.cracha = pygame.Rect(520, 300, 24, 16)


    def executar(self):
        while self.rodando:
            dt = self.relogio.tick(self.fps)/1000
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

                elif evento.type == pygame.KEYDOWN:
                    if self.estado == "game_over":
                        acao = self.tela_morte.processar_evento(evento)

                        if acao == "reiniciar":
                            self.estado = "inicio"
                        elif acao == "sair":
                            self.rodando = False

                    elif evento.key == pygame.K_g:
                        self.estado = "game_over"

                    elif evento.key == pygame.K_ESCAPE:
                        self.rodando = False

            if self.estado == "game_over":
                self.tela_morte.desenhar(self.tela)
            else:
                teclas = pygame.key.get_pressed()
                self.jogador.atualizar(teclas, dt, self.obstaculos)
                self.jogador.limitar_na_tela(*self.tela.get_size())

                # personagem coletando
                if self.mapa.nome == "exterior_cin" and not self.tem_cracha:

                    jogador_rect = pygame.Rect(
                        self.jogador.posicao.x,
                        self.jogador.posicao.y,
                        32, 32
                    )

                    if jogador_rect.colliderect(self.cracha):
                        self.tem_cracha = True
                        print("Crachá de acesso adquirido!")

                if self.mapa.nome == "exterior_cin":
                    if self.jogador.posicao.x >= 928 and self.tem_cracha:
                        self.mapa = Mapa("entrada_cin")
                        self.obstaculos = self.mapa.obstaculos

                        self.jogador.posicao.x = 16
                        self.jogador.posicao.y = 254

                elif self.mapa.nome == "entrada_cin":
                    if self.jogador.posicao.x <= 0:
                        self.mapa = Mapa("exterior_cin")
                        self.obstaculos = self.mapa.obstaculos

                        self.jogador.posicao.x = 880
                        self.jogador.posicao.y = 254

                    elif self.jogador.posicao.x >= 928:
                        self.mapa = Mapa("hall_cin")
                        self.obstaculos = self.mapa.obstaculos

                        self.jogador.posicao.x = 16
                        self.jogador.posicao.y = 254


                elif self.mapa.nome == "hall_cin":
                    if self.jogador.posicao.x <= 0:
                        self.mapa = Mapa("entrada_cin")
                        self.obstaculos = self.mapa.obstaculos

                        self.jogador.posicao.x = 880
                        self.jogador.posicao.y = 254
                

                self.tela.fill((15, 18, 28))

                self.mapa.desenhar(self.tela)

                # Desenho do coletável
                if self.mapa.nome == "exterior_cin" and not self.tem_cracha:
                    pygame.draw.rect(
                        self.tela,
                        (255, 215, 0),
                        self.cracha
                    )

                titulo = self.fonte.render(
                    "NIGHT WATCHERS", True, (235, 235, 235)
                )

                self.tela.blit(titulo, (300, 230))
                self.jogador.desenhar(self.tela)

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
  jogo = Jogo()
  jogo.executar() 
  
