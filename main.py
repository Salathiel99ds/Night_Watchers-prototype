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

        # coleta do crachá
        self.tem_cracha = False
        self.cracha = pygame.Rect(520, 300, 24, 16)

        # coleta do jornal
        self.tem_jornal = False
        self.jornal = pygame.Rect(100, 205, 28, 18)
        self.mostrar_jornal_ate = 0
        self.fonte_jornal = pygame.font.SysFont("Arial", 24)

        # coleta do smartphone
        self.smartphone_lido = False
        self.smartphone = pygame.Rect(472, 245, 16, 28)
        self.mostrar_smartphone_ate = 0
        self.fonte_smartphone = pygame.font.SysFont("Arial", 22)


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

                    elif evento.key == pygame.K_e:
                        if self.mapa.nome == "jardim_interno" and not self.smartphone_lido:

                            jogador_rect = pygame.Rect(
                                self.jogador.posicao.x,
                                self.jogador.posicao.y,
                                32, 32
                            )

                            area_interacao = self.smartphone.inflate(180, 140)

                            if jogador_rect.colliderect(area_interacao):
                                self.smartphone_lido = True
                                self.mostrar_smartphone_ate = pygame.time.get_ticks() + 12000

            if self.estado == "game_over":
                self.tela_morte.desenhar(self.tela)
            else:
                teclas = pygame.key.get_pressed()
                self.jogador.atualizar(teclas, dt, self.obstaculos)
                self.jogador.limitar_na_tela(*self.tela.get_size())

                jogador_rect = pygame.Rect(
                    self.jogador.posicao.x,
                    self.jogador.posicao.y,
                    32, 32
                )

                # personagem coleta crachá
                if self.mapa.nome == "exterior_cin" and not self.tem_cracha:

                   if jogador_rect.colliderect(self.cracha):
                        self.tem_cracha = True

                # personagem coleta jornal
                if self.mapa.nome == "hall_cin" and not self.tem_jornal:
                    if jogador_rect.colliderect(self.jornal):
                        self.tem_jornal = True
                        self.mostrar_jornal_ate = pygame.time.get_ticks() + 10000

                # transição de mapas
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
                    # Hall -> Entrada
                    if self.jogador.posicao.x <= 0:
                        self.mapa = Mapa("entrada_cin")
                        self.obstaculos = self.mapa.obstaculos

                        self.jogador.posicao.x = 880
                        self.jogador.posicao.y = 254

                    # Hall -> jardim interno
                    elif self.jogador.posicao.x >= 928:
                        self.mapa = Mapa("jardim_interno")
                        self.obstaculos = self.mapa.obstaculos

                        self.jogador.posicao.x = 16
                        self.jogador.posicao.y = 254

                elif self.mapa.nome == "jardim_interno":
                    # jardim interno -> Hall
                    if self.jogador.posicao.x <= 0:
                        self.mapa = Mapa("hall_cin")
                        self.obstaculos = self.mapa.obstaculos
                        self.jogador.posicao.x = 880
                        self.jogador.posicao.y = 254

                    # Jardim interno -> Grad05
                    elif self.jogador.posicao.x >= 928:
                        self.mapa = Mapa("grad05")
                        self.obstaculos = self.mapa.obstaculos

                        self.jogador.posicao.x = 16
                        self.jogador.posicao.y = 254

                elif self.mapa.nome == "grad05":
                    # Grad05 -> Jardim interno
                    if self.jogador.posicao.x <= 0:
                        self.mapa = Mapa("jardim_interno")
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

                if self.mapa.nome == "hall_cin" and not self.tem_jornal:
                    pygame.draw.rect(
                        self.tela,
                        (235, 235, 235),
                        self.jornal
                    )

                if self.mapa.nome == "jardim_interno" and not self.smartphone_lido:
                    pygame.draw.rect(
                        self.tela, (35, 40, 55),
                        self.smartphone,
                        border_radius=4
                    )

                titulo = self.fonte.render(
                    "NIGHT WATCHERS", True, (235, 235, 235)
                )

                self.tela.blit(titulo, (300, 230))
                self.jogador.desenhar(self.tela)

                # textos do jornal
                if pygame.time.get_ticks() < self.mostrar_jornal_ate:
                
                    pygame.draw.rect(
                        self.tela,
                        (30, 30, 40),
                        (50, 320, 860, 170),
                        border_radius=10
                    )
                
                    linha1 = self.fonte_jornal.render(
                    "JORNAL ENCONTRADO", True, (255, 255, 255)
                    )

                    linha2 = self.fonte_jornal.render(
                    "CRISE INSTITUCIONAL EM TODO O BRASIL", True, (255, 255, 255)
                    )

                    linha3 = self.fonte_jornal.render(
                    "APÓS O MASSACRE DOS TRÊS PODERES", True, (255, 255, 255)
                    )

                    # Desenho das três linhas
                    self.tela.blit(linha1, (480 - linha1.get_width() // 2, 340))
                    self.tela.blit(linha2, (480 - linha2.get_width() // 2, 382))
                    self.tela.blit(linha3, (480 - linha3.get_width() // 2, 424))

                # Exibição da mensagem na tela de bloqueio do smartphone
                if pygame.time.get_ticks() < self.mostrar_smartphone_ate:

                    pygame.draw.rect(
                        self.tela,
                        (25, 30, 45),
                        (120, 130, 720, 300),
                        border_radius=12
                    )

                    mensagens = [
                        "SMARTPHONE DE LVN",
                        "Nova mensagem de AC:",
                        "Relaxa, vamos terminar o projeto ainda hoje.",
                        "Estou chegando na Grad05",
                        "em poucos minutos."
                    ]

                    for i in range(len(mensagens)):
                        texto = self.fonte_smartphone.render(
                            mensagens[i], True, (240, 240, 240)
                        )

                        x = 480 - texto.get_width() // 2
                        y = 165 + i * 48

                        self.tela.blit(texto, (x, y))
                    

                
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
  jogo = Jogo()
  jogo.executar() 
  
