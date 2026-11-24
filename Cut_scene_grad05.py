import pygame

class CutsceneGrad05:
    def __init__(self):
        self.quadros = [
            "Grad05 - Inicio da cutscene",
            "sequencia narrativa em desenvolvimento",
            "Fim da cutscene"
        ]

        self.indice = 0
        self.finalizada = False

    def processar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if self.indice < len(self.quadros) - 1:
                    self.indice += 1
                else:
                    self.finalizada = True

    def desenhar(self, tela):
        tela.fill((15, 15, 25))

        fonte = pygame.font.Font(None, 32)

        texto = fonte.render(
            self.quadros[self.indice],
            True,
            (255, 255, 255)
        )

        tela.blit(texto, (100, 250))

if __name__ == "__main__":
    pygame.init()

    tela = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Cutscene - Grad05")

    relogio = pygame.time.Clock()
    cutscene = CutsceneGrad05()

    executando = True

    while executando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            else:
                cutscene.processar_evento(evento)

        if cutscene.finalizada:
            executando = False
        else:
            cutscene.desenhar(tela)

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
