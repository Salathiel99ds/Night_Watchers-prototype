import pygame 

class Jogo:
  def __init__(self):
    pygame.init()
    
    self.tela = pygame.display.set_mode((960,540))
    pygame.display.set_caption("Night Watchers")
    
    self.relogio = pygame.time.Clock()
    self.fps = 144
    self.rodando = True
    
    
    self.fonte = pygame.font.SysFonte("Arial", 36)

def executar(self):
  while self.rodando:
    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        self.rodando = False

        elif evento.type == pygame.KEYDOWN:
          if evento.key == pygame.K_ESCAPE:
            self.rodando = False
    
    self.tela.fill((15, 18, 28))
  
    titulo = self.fonte.render(
    "NIGHT WATCHERS", True, (235, 235, 235)
    )
    self.tela.blit(titulo, (300, 230))

    pygame.display.flip()
    self.relogio.tick(self.fps)
  
  pygame.quit()


if __name__ == "__main__":
  jogo = Jogo()
  jogo.executar()
    
