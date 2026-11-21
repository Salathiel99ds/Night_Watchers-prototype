import pygame

class TelaVitoria:
    def __init__(self): #iniciar e guarda no objeto 
        self.fonte_titulo = pygame.font.SysFont("Arial", 90)
        self.fonte_texto = pygame.font.SysFont("Arial", 36)

    def desenhar(self, tela):
        largura, altura = tela.get_size() #largura e altura em pixels

        tela.fill((15,18,28)) #preenche a superficie de uma cor, o plano de fundo quando ganhar

        titulo = self.fonte_titulo.render( #o render(n exibe) prepara a apenas a superficie e a fonte
            "YOU WIN", True, (255,215,0) #texto exibido, antialising, cor do texto
        )

        mensagem = self.fonte_texto.render(
            "Você concluiu sua missão!", True, (255,255,255)
        )

        reiniciar = self.fonte_texto.render(
            "Pressione R para jogar novamente.", True, (220, 220, 220)
        )

        sair = self.fonte_texto.render(
            "Pressione ESC para sair.", True, (180, 180, 180)
        )

        tela.blit( #desenha uma superfice sobre outra, que nesse caso eh a janela
            titulo,
            titulo.get_rect(center=(largura // 2, altura // 2)) #get_rect cria um retangulo c dimensoes da superficies q tem no texto
        )

        tela.blit(
            mensagem,
            mensagem.get_rect(center=(largura // 2, altura // 2 + 80))
        )

        tela.blit(
            reiniciar,
            reiniciar.get_rect(center=(largura // 2, altura // 2 + 150))
        )

        tela.blit(
            sair,
            sair.get_rect(center=(largura // 2, altura // 2 + 195))
        )
    def processar_evento(self, evento):
        if evento.type == pygame.KEYDOWN: #caso o evento seja uma tecla pressionada
            if evento.key == pygame.K_r: #caso o evento seja a tecla r
                return "reiniciar"
            elif evento.key == pygame.K_ESCAPE:
                return "sair"
        return ""