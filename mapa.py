import pygame

class Mapa:
    def __init__(self, nome="exterior_cin"):
        self.nome = nome

        if self.nome == "exterior_cin":
         # Obstáculos do exterior 
         self.obstaculos = [
            pygame.Rect(0, 0, 960, 130),
            pygame.Rect(0, 410, 960, 130),
            pygame.Rect(275, 360, 36, 50),
            pygame.Rect(690, 130, 36, 50)
        ]
         
        elif self.nome == "entrada_cin":
          # Obstáculos da entrada
          self.obstaculos = [
             pygame.Rect(0, 0, 960, 110),
             pygame.Rect(0, 430, 960, 110),
             pygame.Rect(230, 350, 70, 80),
             pygame.Rect(690, 110, 36, 50)
          ]

        elif self.nome == "hall_cin":
           # Obstáculos da recepcao e do hall
           self.obstaculos = [
              pygame.Rect(0, 0, 960, 90),
              pygame.Rect(0, 450, 960, 90),
              pygame.Rect(170, 110, 180, 65),
              pygame.Rect(620, 315, 50, 75)
         ]
            
        elif self.nome == "corredor1_cin":
            # Corredor obstruído à esquerda do hall
            self.obstaculos = [
               pygame.Rect(0, 0, 960, 90),
               pygame.Rect(0, 450, 960, 90),

             # Bloqueio da passagem
               pygame.Rect(300, 90, 60, 360)
        ]

                
       elif self.nome == "jardim_interno":
           # obstáculos do jardim
           self.obstaculos = [
              pygame.Rect(0, 0, 960, 90),
              pygame.Rect(0, 450, 960, 90),
              pygame.Rect(420, 230, 120, 60)
         ]

        elif self.nome == "corredor2_cin":
            # Corredor alternativo
            self.obstaculos = [
                pygame.Rect(0, 0, 960, 90),
                pygame.Rect(0, 450, 960, 90),

                # Obstáculos do corredor alternativo 
                pygame.Rect(430, 90, 70, 100),
                pygame.Rect(630, 350, 70, 100)
        ]
                

        elif self.nome == "grad05":
           # Obstáculos da sala Grad05
            self.obstaculos = [
              pygame.Rect(0, 0, 960, 90),
              pygame.Rect(0, 450, 960, 90),
              pygame.Rect(380, 125, 200, 65)
        ]
           

    def desenhar(self, tela):
        tela.fill((185, 180, 169))

        if self.nome == "corredor1_cin":
            # Piso do corredor
            tela.fill((170, 173, 176))

            # Paredes superior e inferior
            pygame.draw.rect(
                tela, (95, 95, 95),
                self.obstaculos[0]
            )
            
            pygame.draw.rect(
                tela, (95, 95, 95),
                self.obstaculos[1]
            )
            
            # Passagem Obstruída
            pygame.draw.rect(
                tela, (125, 75, 55),
                self.obstaculos[2]
            )
            
            return

        if self.nome == "corredor2_cin":
            # Piso do corredor alternativo
            tela.fill((170, 173, 176))

           # Paredes do Corredor
           pygame.draw.rect(
               tela, (95, 95, 95),
               self.obstaculos[0]
           )

           pygame.draw.rect(
               tela, (95, 95, 95),
               self.obstaculos[1]
           )

           pygame.draw.rect(
               tela, (125, 105, 85),
               self.obstaculos[2]
           )

           pygame.draw.rect(
               tela, (125, 105, 85),
               self.obstaculos[3]
           )

           return

        if self.nome == "grad05":
           # Piso da sala
           tela.fill((185, 180, 169))

           # Parede superior
           pygame.draw.rect(
              tela, (95, 95, 95),
              self.obstaculos[0]
           )

           # Parede inferior
           pygame.draw.rect(
              tela, (95, 95, 95),
              self.obstaculos[1]
           )

           # Mesa
           pygame.draw.rect(
              tela, (110, 75, 50),
              self.obstaculos[2]
           )

        if self.nome == "jardim_interno":
           # Piso do jardim
           tela.fill((110, 145, 110))

           # Limites do cenário
           pygame.draw.rect(
              tela, (95, 95, 95),
              self.obstaculos[0]
           )

           pygame.draw.rect(
              tela, (95, 95, 95),
              self.obstaculos[1]
           )

           # Mesa de madeira
           pygame.draw.rect(
              tela, (125, 80, 45),
              self.obstaculos[2]
           )

           return

        if self.nome == "hall_cin":
           #piso do hall
           tela.fill((170, 173, 176))

           # paredes
           pygame.draw.rect(
              tela, (110,115, 122),
              self.obstaculos[0]
           )

           pygame.draw.rect(
              tela, (110, 115, 122),
              self.obstaculos[1]
           )

           # Balcão da recepção
           pygame.draw.rect(
              tela, (125, 85, 65),
              self.obstaculos[2]
           )

           # pilar 
           pygame.draw.rect(
              tela, (90, 95, 105),
              self.obstaculos[3]
           )

           return
        
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
