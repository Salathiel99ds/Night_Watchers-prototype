import pygame

class Jogador:
    def __init__(self, x, y):
        self.posicao = pygame.Vector2(x, y)
        self.velocidade = 240
        self.tamanho = 32
        self.cor = (70, 160, 240)

    def atualizar(self, teclas, dt, obstaculos):
        movimento = pygame.Vector2(0, 0)

        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            movimento.y -= 1

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            movimento.y += 1

        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            movimento.x -= 1

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            movimento.x += 1

        if movimento.length_squared() > 0:
            movimento = movimento.normalize()

        deslocamento = movimento * self.velocidade * dt 

        retangulo = pygame.Rect(
            round(self.posicao.x),
            round(self.posicao.y),
            self.tamanho,
            self.tamanho
        )

        # Movimento Horizontal
        self.posicao.x += deslocamento.x
        retangulo.x = round(self.posicao.x)

        for parede in obstaculos:
            if retangulo.colliderect(parede):
                if deslocamento.x > 0:
                    self.posicao.x = parede.left - self.tamanho
                elif deslocamento.x < 0:
                    self.posicao.x = parede.right

                retangulo.x = round(self.posicao.x)

        # Movimento Vertical
        self.posicao.y += deslocamento.y
        retangulo.y = round(self.posicao.y)

        for parede in obstaculos:
            if retangulo.colliderect(parede):
                if deslocamento.y > 0:
                    self.posicao.y = parede.top - self.tamanho
                elif deslocamento.y < 0:
                    self.posicao.y = parede.bottom

                retangulo.y = round(self.posicao.y)


    def limitar_na_tela(self, largura, altura):
        self.posicao.x = max(0, min(self.posicao.x, largura - self.tamanho)
        )

        self.posicao.y = max(0, min(self.posicao.y, altura - self.tamanho)
        )
        

    def desenhar(self, tela):
        retangulo = pygame.Rect(
            round(self.posicao.x),
            round(self.posicao.y),
            self.tamanho,
            self.tamanho
        )
        pygame.draw.rect(tela, self.cor, retangulo)
