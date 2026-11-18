import pygame

class Mapa:
    def __init__(self):
        self.nome = "exterior_cin"

        self.obstaculos = [
            pygame.Rect(0, 0, 960, 130),
            pygame.Rect(0, 410, 960, 130),
            pygame.Rect(275, 360, 36, 50),
            pygame.Rect(690, 130, 36, 50)
        ]
    def desenhar(self, tela):
        tela.fill((185, 180, 169))

        # lateral do CIn
        pygame.draw.rect(
          tela,
          (175, 105, 117),
          self.obstaculos[0]
        )

        # Area de vegetação 
        pygame.draw.rect(
          tela,
          (66, 105, 117),
          self.obstaculos[1]
        )

        # troncos das árvores
        for arvore in self.obstaculos[2:]:
            pygame.draw.rect(
                tela,
                (89, 70, 56),
                arvore
            )