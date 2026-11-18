import pygame

class Mapa:
    def __init__(self, nome="exterior_cin"):
        self.nome = nome

        if self.nome == "entrada_cin":
         self.obstaculos = [
            pygame.Rect(0, 0, 960, 130),
            pygame.Rect(0, 410, 960, 130),
            pygame.Rect(275, 360, 36, 50),
            pygame.Rect(690, 130, 36, 50)
        ]
         
        else:
          self.obstaculos = [
             pygame.Rect(0, 0, 960, 110),
             pygame.Rect(0, 430, 960, 110),
             pygame.Rect(230, 350, 70, 80),
             pygame.Rect(690, 110, 36, 50)
          ]

    def desenhar(self, tela):
        tela.fill((185, 180, 169))
        
        if self.nome == "entrada_cin":
        
           # Fachada do edifício
           pygame.draw.rect(
              tela, (155, 85, 88),
              self.obstaculos[0]
           )

           # vegetação 
           pygame.draw.rect(
              tela, (70, 122, 76),
              self.obstaculos[1]
           )

           # canteiro
           pygame.draw.rect(
              tela, (90, 120, 70),
              self.obstaculos[2]
           )

           # Arvore
           pygame.draw.rect(
              tela, (89, 70, 56),
              self.obstaculos[3]
           )

           return
        
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