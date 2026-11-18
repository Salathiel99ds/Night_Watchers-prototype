import pygame 
from game_over import TelaMorte
from jogador import Jogador

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
                self.jogador.atualizar(teclas, dt)
                self.jogador.limitar_na_tela(*self.tela.get_size())

                self.tela.fill((15, 18, 28))

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
  
