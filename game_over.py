import pygame


class TelaMorte:
  def __init__(self):
    self.fonte_titulo = pygame.font.SysFont("Arial", 90)
    self.fonte_texto = pygame.font.SysFont("Arial", 36)
  
  def desenhar(self, tela):
    largura, altura = tela.get_size()
    
    tela.fill((15,18,28))

    titulo = self.fonte_titulo.render(
      "VOCÊ PERECEU", True, (220, 65, 65)
    )
    
    mensagem = self.fonte_texto.render(
    "Levi foi morto.", True, (235, 235, 235)
    )
    
    reiniciar = self.fonte_texto.render(
    "pressione R para tentar mais uma vez", True, (220, 220, 220)
    )
    
    sair = self.fonte_texto.render(
    "pressione ESC pra sair", True, (180, 180, 180)
    )
    
    tela.blit(
    titulo,
    titulo.get_rect(center=(largura // 2, altura // 2 - 120))
    )
    
    tela.blit(
    mensagem,
    mensagem.get_rect(center=(largura // 2, altura // 2))
    )
    
    tela.blit(
    reiniciar,
    reiniciar.get_rect(center=(largura // 2, altura // 2 + 90))
    )
    
    tela.blit(
    sair,
    sair.get_rect(center=(largura // 2, altura // 2 + 140))
    )
    
  def processar_evento(self, evento):
    if evento.type == pygame.KEYDOWN:
      if evento.key == pygame.K_r:
        return "reiniciar"
      
      elif evento.key == pygame.K_ESCAPE:
        return "sair"
    
    return ""
    
    
    
