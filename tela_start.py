import pygame


class TelaStart:
    def __init__(self):
        self.fonte_titulo = pygame.font.SysFont("Arial", 80)
        self.fonte_texto = pygame.font.SysFont("Arial", 32)

        self.opcoes = ["Jogar", "Tutorial", "Sair"]
        self.selecionada = 0

        self.botoes = []
        for i in range(len(self.opcoes)):
            self.botoes.append(pygame.Rect(380, 250 + i * 80, 200, 56))

    def desenhar(self, tela):
        largura, altura = tela.get_size()

        tela.fill((15, 18, 28))

        titulo = self.fonte_titulo.render(
            "NIGHT WATCHERS", True, (235, 235, 235)
        )
        tela.blit(titulo, titulo.get_rect(center=(largura // 2, 140)))

        for i in range(len(self.opcoes)):
            if i == self.selecionada:
                cor_fundo = (255, 215, 0)
                cor_texto = (15, 18, 28)
            else:
                cor_fundo = (30, 30, 40)
                cor_texto = (235, 235, 235)

            pygame.draw.rect(tela, cor_fundo, self.botoes[i], border_radius=10)

            texto = self.fonte_texto.render(self.opcoes[i], True, cor_texto)
            tela.blit(texto, texto.get_rect(center=self.botoes[i].center))

    def processar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_UP, pygame.K_w):
                self.selecionada = (self.selecionada - 1) % len(self.opcoes)

            elif evento.key in (pygame.K_DOWN, pygame.K_s):
                self.selecionada = (self.selecionada + 1) % len(self.opcoes)

            elif evento.key == pygame.K_RETURN:
                return self.opcoes[self.selecionada].lower()

            elif evento.key == pygame.K_ESCAPE:
                return "sair"

        elif evento.type == pygame.MOUSEMOTION:
            for i in range(len(self.botoes)):
                if self.botoes[i].collidepoint(evento.pos):
                    self.selecionada = i

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            for i in range(len(self.botoes)):
                if self.botoes[i].collidepoint(evento.pos):
                    return self.opcoes[i].lower()

        return ""

