import pygame

class MarcoZero:
    def __init__(self, tela):
        self.tela = tela
        self.fonte = pygame.font.Font(None, 48)

    def atualizar(self, dt):
        pass

    def desenhar(self):
        largura, altura = self.tela.get_size()

        self.tela.fill((12, 20, 33))

        # estuario do capibaribe pro atlântico
        pygame.draw.rect(
            self.tela,
            (12, 20, 33),
            (0, altura * 0.30, largura, 15)
        )

        # Piso do MZ
        pygame.draw.rect(
            self.tela,
            (152, 88, 74),
            (0, altura * 0.30 + 15, largura, altura * 0.70)
        )

        # Pavimentação do MZ
        inicio_piso = int(altura * 0.30) + 15
        tamanho_lajota = 60
        cor_linhas = (130, 106, 79)

        # Linhas horizontais
        for y in range(inicio_piso, altura, tamanho_lajota):
            pygame.draw.line(
                self.tela,
                cor_linhas,
                (0, y),
                (largura, y),
                1
            )

        # Linhas verticais
        for x in range(0, largura, tamanho_lajota):
            pygame.draw.line(
                self.tela,
                cor_linhas,
                (x, inicio_piso),
                (x, altura),
                1
            )

        # Rua em frente aos edificios
        rua_y = int(altura * 0.27)
        rua_h = int(altura * 0.09)

        pygame.draw.rect(
            self.tela,
            (42, 43, 49),
            (0, rua_y, largura, rua_h)
        )

        # calcada dos edificios
        pygame.draw.rect(
            self.tela,
            (112, 106, 96),
            (0, rua_y, largura, 12)
        )

        # Calcada do MZ
        pygame.draw.rect(
            self.tela,
            (145, 130, 112),
            (0, rua_y + rua_h - 8, largura, 8)
        )

        # Edificio circular
        ex = int(largura * 0.03)
        ey = int(altura * 0.08)
        el = int(largura * 0.15)
        eh = int(altura * 0.22)

        # Estrutura principal
        pygame.draw.rect(
            self.tela,
            (38, 55, 70),
            (ex, ey, el, eh),
            border_radius=15
        )

        # Fachada de vidro
        pygame.draw.rect(
            self.tela,
            (25, 44,61),
            (ex + 8, ey + 8, el - 16, eh - 12),
            border_radius=10
        )

        # Divisões horizontais dos edificio
        for i in range(1, 7):
            x = ey + int(eh * i/7)

            pygame.draw.line(
                self.tela,
                (155, 165, 175),
                (ex + 4, y),
                (ex + el - 4, y),
                3
            )

            # Divisões verticais dos vidros
            for i in range(1, 6):
                x = ex + int(el * i/6)

                pygame.draw.line(
                    self.tela,
                    (83, 102, 117),
                    (x, ey + 8),
                    (x, ey + eh - 4),
                    2
                )

        # cobertura arredondada
        pygame.draw.ellipse(
            self.tela,
            (119, 122, 128),
            (ex, ey - 6, el, 18)
        )

        pygame.draw.ellipse(
            self.tela,
            (69, 77, 88),
            (ex + 5, ey - 4, el - 10, 12)           
        )

        # Divisões horizontais do edificio
        for andar in range(1, 9):
            y = ey + int(eh * andar / 9)

            pygame.draw.line(
                self.tela,
                (115, 135, 145),
                (ex + 4, y),
                (ex + el - 4, y),
                2
            )

        # Associação Comercial de Pernambuco
        ax = int(largura * 0.43)
        ay = int(altura * 0.12)
        al = int(largura * 0.29)
        ah = int(altura * 0.18)

        # Fachada principal
        pygame.draw.rect(
            self.tela,
            (161, 139, 96),
            (ax, ay, al, ah)
        )

        # Divisões dos pavimentos
        for i in range(1, 3):
            y = ay + int(ah * i / 3)

            pygame.draw.line(
                self.tela,
                (208, 183, 138),
                (ax, y),
                (ax + al, y),
                3
            )

        # Janelas
        for andar in range(3):
            for coluna in range(7):
                x = ax + int(al * (coluna + 0.5) / 7)
                y = ay + int(ah * andar / 3) + 5

                pygame.draw.rect(
                    self.tela,
                    (85, 65, 110),
                    (x - 7, y, 14, int(ah / 3) - 10),
                    border_radius=4
                )

            # Cornija superior
            pygame.draw.rect(
                self.tela,
                (208, 183, 138),
                (ax - 3, ay - 4, al + 6, 6)
            )

        # Cupulas
        for proporcao in (0.15, 0.85):
            x = ax + int(al * proporcao)

            pygame.draw.ellipse(
                self.tela,
                (65, 67, 75),
                (x - 17, ay - 25, 34, 30)
            )

            pygame.draw.line(
                self.tela,
                (145, 130, 100),
                (x, ay - 25),
                (x, ay - 35),
                2
            )

        # Caixa Ecônomica cultural
        bx = int(largura * 0.23)
        by = int(altura * 0.10)
        bl = int(largura * 0.19)
        bh = int(altura * 0.18)

        # Fachada
        pygame.draw.rect(
            self.tela,
            (145, 132, 105),
            (bx, by, bl, bh)
        )

        # Cornija superior 
        pygame.draw.rect(
            self.tela,
            (192, 174, 135),
            (bx - 3, by, bl + 6, 5)
        )

        # Janelas
        for andar in range(2):
            for coluna in range(5):
                x = bx + int(bl * (coluna + 0.5) / 5)
                y = by + 10 + andar * int(bh / 2)

                pygame.draw.rect(
                    self.tela,
                    (65, 48, 100),
                    (x - 6, y, 12, 18),
                    border_radius=3
                )

        # Ornamentos verticais da fachada
        for i in range(6):
            px = bx + int(bl * i / 5)

            pygame.draw.line(
                self.tela,
                (192, 174, 135),
                (px, by + 5),
                (px, by + bh),
                3
            )

        # Torres e cupulas
        for proporcao in (0.15, 0.85):
            tx = bx + int(bl * proporcao)
            ty = by - 8

            pygame.draw.rect(
                self.tela,
                (145, 132, 105),
                (tx - 10, ty, 20, 12)
            )
            pygame.draw.ellipse(
                self.tela,
                (65, 70, 82),
                (tx - 12, ty - 15, 24, 24)
            )

            pygame.draw.line(
                self.tela,
                (177, 165, 140),
                (tx, ty - 22),
                (tx, ty - 14),
                2
            )

        # Divisão dos pavimentos
        pygame.draw.line(
            self.tela,
            (192, 174, 135),
            (bx, by + bh // 2),
            (bx + bl, by + bh // 2),
            3
        )

        # Edificios à direita
        cores_fachadas = [
            (125, 83, 88),
            (79, 111, 119),
            (146, 132, 108)
        ]

        for i in range(3):
            fx = int(largura * 0.75) + i * int(largura * 0.075)
            fy = int(altura * 0.12)
            fl = int(largura * 0.07)
            fh = int(altura * 0.17)

            pygame.draw.rect(
                self.tela,
                cores_fachadas[i],
                (fx, fy, fl, fh)
            )

            #  Cornija superior
            pygame.draw.rect(
                self.tela,
                (170, 155, 130),
                (fx, fy, fl, 4)
            )

            # Janelas dos três
            for andar in range(3):
                for coluna in range(2):
                    jx = fx + int(fl * (coluna + 1) / 3)
                    jy = fy + 9 + andar * (fh // 3)

                    pygame.draw.rect(
                        self.tela,
                        (42, 39, 58),
                        (jx - 5, jy, 10, 13),
                        border_radius=2
                    )

        # iluminacao das fachadas
        luz_fachada = pygame.Surface(
            (largura, altura),
            pygame.SRCALPHA
        )

        for i in range(7):
            lx = int(largura * (0.48 + 0.04 * i))
            ly = int(altura * 0.23)

            for raio_luz in range(20, 2, -1):
                intensidade = (20 - raio_luz) * 6

                pygame.draw.circle(
                    luz_fachada,
                    (155, 65, 230, intensidade),
                    (lx, ly),
                    raio_luz
                )

        self.tela.blit(luz_fachada, (0, 0))

        # postes de iluminação
        poste_y = rua_y + rua_h - 4

        for proporcao in (0.08, 0.36, 0.64, 0.92):
            poste_x = int(largura * proporcao)

            # Base do poste
            pygame.draw.rect(
                self.tela,
                (48, 48, 53),
                (poste_x - 6, poste_y - 5, 12, 5),
                4
            )

            # Haste 
            pygame.draw.line(
                self.tela,
                (48, 48, 53),
                (poste_x, poste_y),
                (poste_x, poste_y - 65),
                4
            )
            # Halo de iluminação
            halo = pygame.Surface(
                (100, 100),
                pygame.SRCALPHA
            )

            for raio_luz in range(45, 5, -1):
                intensidade = int((45 - raio_luz) * 2
                )

                pygame.draw.circle(
                  halo,
                  (255, 215, 130, intensidade),
                  (50, 50),
                  raio_luz
               )

            self.tela.blit(
                halo,
                (poste_x - 50, poste_y - 115)
            )

            # Lampada
            pygame.draw.circle(
                self.tela,
                (245, 220, 155),
                (poste_x, poste_y - 65),
                6
            )

        # Palmeiras
        for proporcao in (0.10, 0.90):
            px = int(largura * proporcao)
            py = int(altura * 0.72)

            # sombra
            pygame.draw.ellipse(
                self.tela,
                (100, 85, 75),
                (px - 25, py - 5, 50, 12)
            )

            # Tronco
            
        # Rosa dos ventos
        cx = largura // 2
        cy = int(altura * 0.66)
        raio = int(altura * 0.27)

        pygame.draw.circle(
            self.tela, (144, 139, 121),
            (cx, cy), raio
        )

        pygame.draw.circle(
            self.tela, (185, 164, 135),
            (cx, cy), raio, 3
        )

        pygame.draw.circle(
            self.tela, (89, 127, 144),
            (cx, cy), int(raio * 0.83), 2
        )

        # Pontas diagonais
        d = int(raio * 0.56)
        p = int(raio * 0.20)

        pygame.draw.polygon(
            self.tela, (158, 104, 87),
            [
                (cx-d, cy-d),
                (cx, cy-p),
                (cx+d, cy-d),
                (cx+p, cy),
                (cx+d, cy+d),
                (cx, cy+p),
                (cx-d, cy+d),
                (cx-p, cy)
            ]
        )

        # Pontas pricipais
        r = int(raio * 0.90)

        pygame.draw.polygon(
            self.tela, (186, 160, 99),
            [
                (cx, cy-r),
                (cx+p, cy-p),
                (cx+r, cy),
                (cx+p, cy+p),
                (cx, cy+r),
                (cx-p, cy+p),
                (cx-r, cy),
                (cx-p, cy-p)
            ]
        )

        pygame.draw.circle(
            self.tela, (179, 151, 80),
            (cx, cy), 8
        )

        titulo = self.fonte.render(
            "Marco Zero - Recife",
            True,
            (230, 210, 160)
        )

        posicao = titulo.get_rect(
            midtop=(largura // 2, 15)
        )

        self.tela.blit(titulo, posicao)


