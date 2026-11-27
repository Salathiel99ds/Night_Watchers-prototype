import pygame

class MarcoZero:
    def __init__(self, tela):
        self.tela = tela
        self.fonte = pygame.font.Font(None, 48)

    def atualizar(self, dt):
        pass

    def desenhar(self):
        self.tela.fill((12, 16, 32))

        titulo = self.fonte.render(
            "Marco Zero - Recife",
            True,
            (230, 210, 160)
        )

        posicao = titulo.get_rect(
            center=self.tela.get_rect().center
        )

        self.tela.blit(titulo, posicao)


