import pygame

class CutsceneGrad05:
    def __init__(self):
        # texto
        self.quadros = [
                "Levi se aproxima da Grad05.",

    "Estudantes e monitores estão assustados. "
    "O professor permanece desacordado.",

    "LVN, AC e MJ estão entre os presentes.",

    "Uma figura de trajes imperiais segura um enorme martelo. "
    "É o Flagelo Fulgurante.",

    "O Flagelo está recuperando suas forças, "
    "mas sua regeneração ainda está incompleta.",

    "Flagelo Fulgurante: Que lastimável, "
    "ninguém corajoso o bastante para tentar me deter em vão?",

    "Os monitores imploram ao Flagelo que poupe o professor, "
    "mas ele ignora os pedidos.",

    "Flagelo Fulgurante: Pois bem... "
    "chegou a hora do cortejo fúnebre.",

    "Um disparo interrompe a cena. ",
    "O Flagelo volta sua atenção para Levi, ",
    "que está com a pistola apontada em sua direção."

    "O Flagelo toca a testa e percebe que foi ferido. "
    "Enfurecido, encara Levi.",

    "Flagelo Fulgurante: COMO OUSA ME FERIR SUA ANTA QUADRADA! "
    "VOCÊ ACHA QUE CONSEGUE ME MATAR COM ISSO!?",

    "Levi: Eu sei muito bem que armas de fogo não conseguem te matar, "
    "seu cretino. Saiba que fiz isso pra chamar a sua atenção.",

    "Levi revela que já enfrentou seres similares ao Flagelo "
    "em diferentes países.",

    "Levi: Mesmo depois de termos lutado em tantos "
    "estados brasileiros, eu ainda não sei o que "
    "realmente é você...",

    "Levi: Flagelo Fulgurante.",

    "Lutar dentro da Grad05 colocaria a vida dos estudantes, "
    "monitores e professor em perigo. Levi precisava afastar o Pivô daquela área.",

    "Levi: O que acha de lutarmos em um local afastado? "
    "Se você me derrotar, você pode continuar o seu "
    "showzinho quando voltar.",

    "O Flagelo acredita que pode derrotar Levi, mesmo "
    "que ele esteja debilitado, e depois retornar ao CIn para "
    "completar sua regeneração. ",

    "O Flagelo ergue seu martelo e desfere um golpe "
    "de força sobrenatural contra Levi.",

    "Levi é arremessado fisicamente da Grad05 "
    "em direção ao Marco Zero, no Recife.",

    "Flagelo Fulgurante: Assim que esse fedelho "
    "finalmente for exterminado, farei de vocês "
    "o meu lanchinho. ",

    "O Flagelo solta uma pequena risada e parte "
    "para o campo de batalha usando seu martelo. ",

    "O Flagelo deixou a Grad05, mas os estudantes "
    "e monitores continuam profundamente abalados.",

    "PV: Eu queria estar sonhando... "
    "mas isso está vívido até demais.",

    "AH: Eu não quero morrer.",

    "SM: TODOS AQUI PRESENTES!",

    "SM: PRECISAMOS LEVAR O PROFESSOR E AS DEMAIS "
    "PESSOAS AFETADAS PRA FORA DAQUI, "
    "ELES PRECISAM DE NOSSA AJUDA.",

    "Os demais conseguem se recompor e retirar os estudantes "
    "e monitores, incluindo LVN e AC, em segurança. "
    "O professor também recebe assistência."
    
    ]

        self.indice = 0
        self.finalizada = False
        self.mostrando_sala = True

    def processar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:

                # Encerra a apresentação inicial da sala
                if self.mostrando_sala:
                    self.mostrando_sala = False

                # Avança os quadros narrativos
                elif self.indice < len(self.quadros) - 1:
                    self.indice += 1

                # Encerra a cutscene
                else:
                    self.finalizada = True 

    def desenhar(self, tela):
        # Limpa a tela
        tela.fill((15, 15, 25))

        # Parede frontal da Grad05
        pygame.draw.rect(
            tela,
            (210, 212, 208),
            (0, 0, 960, 195)
        )

        # Porta do lado esquerdo
        pygame.draw.rect(
            tela,
            (205, 190, 160),
            (25, 15, 115, 175),
        )

        # Moldura da porta
        pygame.draw.rect(
            tela,
            (115, 110, 100),
            (25, 15, 115, 175),
            3
        )

        # Visor da porta
        pygame.draw.rect(
            tela,
            (135, 155, 165),
            (60, 45, 25, 90)
        )

        # Macaneta 
        pygame.draw.circle(
            tela,
            (110, 105, 95),
            (120, 115),
            5
        )

        # Piso do Grad05
        pygame.draw.rect(
            tela,
            (65, 65, 70),
            (0, 195, 960, 345)
        )

        # linhas de perspectiva do piso
        for x in range(0, 1200, 160):
            pygame.draw.line(
                tela,
                (80, 80, 85),
                (480, 195),
                (x, 540),
                1
            )

        # Divisões horizontais do piso
        for y in (280, 350, 430, 520):
            pygame.draw.line(
                tela,
                (85, 85, 90),
                (0, y),
                (960, y),
                1
            )

        # Primeiro quadro branco
        pygame.draw.rect(
            tela,
            (225, 235, 240),
            (160, 40, 215, 125),
        )

        pygame.draw.rect(
            tela,
            (155, 165, 175),
            (160, 40, 215, 125),
            3
        )

        # Televisão entre os dois quadros
        pygame.draw.rect(
            tela,
            (20, 23, 28),
            (390, 25, 235, 145),
        )

        # Moldura da TV
        pygame.draw.rect(
            tela,
            (85, 90, 95),
            (390, 25, 235, 145),
            3
        )

        # Segundo quadro branco
        pygame.draw.rect(
            tela,
            (225, 235, 240),
            (640, 40, 250, 125)
        )

        pygame.draw.rect(
            tela,
            (155, 165, 175),
            (640, 40, 250, 125),
            3
        )

        # Mesa do professor - Grad05

        # Tampo da mesa
        pygame.draw.rect(
            tela,
            (205, 180, 145),
            (740, 235, 155, 12),
            border_radius=3
        )

        # Sustentação esquerda
        pygame.draw.rect(
            tela,
            (155, 125, 95),
            (750, 247, 10, 32)
        )

        # Gabinete lateral da mesa
        pygame.draw.rect(
            tela,
            (190, 165, 130),
            (850, 247, 40, 32),
            border_radius=2
        )

        # Contorno do gabinete
        pygame.draw.rect(
            tela,
            (120, 95, 70),
            (850, 247, 40, 32),
            2,
            border_radius=2
        )

        # Monitor do professor (moldura, tela, base do monitor, teclado e mouse)
        pygame.draw.rect(
            tela,
            (25, 25, 30),
            (785, 202, 75, 32),
            border_radius=3
        )

        pygame.draw.rect(
            tela,
            (45, 60, 70),
            (790, 207, 65, 22)
        )

        pygame.draw.rect(
            tela,
            (55, 55, 60),
            (818, 231, 10, 7)
        )

        pygame.draw.rect(
            tela,
            (35, 35, 40),
            (760, 240, 48, 6),
            border_radius=2
        )

        for x in range(764, 804, 6):
            pygame.draw.line(
                tela,
                (100, 100, 105),
                (x, 242),
                (x + 3, 242)
            )
        pygame.draw.ellipse(
            tela,
            (40, 40, 45),
            (818, 240, 9, 7)
        )

        # Cadeira giratória (encosto, contorno, assento, haste, base)
        pygame.draw.rect(
            tela,
            (40, 42, 48),
            (695, 215, 34, 48),
            border_radius=12
        )

        pygame.draw.rect(
            tela,
            (105, 105, 115),
            (695, 215, 34, 48),
            border_radius=12
        )

        pygame.draw.ellipse(
            tela,
            (50, 50, 55),
            (687, 260, 50, 13)
        )

        pygame.draw.rect(
            tela,
            (90, 90, 95),
            (709, 271, 6, 20)
        )

        pygame.draw.line(
            tela,
            (75, 75, 80),
            (694, 291),
            (731, 291),
            4
        )

        # primeira fileira de computadores

        for x in(120, 300, 480):

            # Tampo da mesa
            pygame.draw.rect(
                tela,
                (205, 205, 205),
                (x, 248, 140, 10)
            )

            # Pés da mesa
            pygame.draw.rect(
                tela,
                (125, 125, 130),
                (x + 8, 258, 7, 22)
            )

            pygame.draw.rect(
                tela,
                (25, 25, 30),
                (x + 42, 215, 56, 30),
                border_radius=2
            )

            # Moldura do monitor
            pygame.draw.rect(
                tela,
                (25, 25, 30),
                (x + 42, 215, 56, 30),
                border_radius=2
            )

            # tela do monitor
            pygame.draw.rect(
                tela,
                (45, 55, 65),
                (x + 46, 219, 48, 22)
            )

            pygame.draw.rect(
                tela,
                (65, 65, 70),
                (x + 66, 245, 10, 3)
            )

        # Cadeiras dos estudantes
        for x in (120, 300, 480):

            pygame.draw.rect(
                tela,
                (38, 40, 45),
                (x + 50, 257, 40, 42),
                2,
                border_radius=2
            )

            pygame.draw.rect(
                tela,
                (95, 100, 105),
                (x + 50, 257, 40, 42),
                2,
                border_radius=8
            )

            pygame.draw.ellipse(
                tela,
                (48, 50, 55),
                (x + 45, 291, 50, 12)
            )


        # Aparelhos de ar-condicionado
        for x in (200, 690):
            # corpo do aparelho
            pygame.draw.rect(
                tela,
                (235, 238, 240),
                (x, 5, 145, 29),
                border_radius=5
           )

            # Contorno
            pygame.draw.rect(
                tela,
                (145, 150, 155),
                (x, 5, 145, 29),
                2,
                border_radius=5
           )

            # Saída de ar
            pygame.draw.line(
                tela,
                (110, 115, 120),
                (x + 12, 26),
                (x + 133, 26),
                2
            )

        # Segunda fileira de computadores - mais próxima sustentações, molduras, telas, bases dos monitores, teclados e encostos)

        for x in (100, 355, 610):
            # Mesa
            pygame.draw.rect(
                tela,
                (205, 205, 205),
                (x, 345, 175, 14),
                border_radius=2
            )

            # Sustentações
            pygame.draw.rect(
                tela,
                (125, 125, 130),
                (x + 12, 359, 9, 35)
            )

            pygame.draw.rect(
                tela,
                (125, 125, 130),
                (x + 154, 359, 9, 35)
            )

            # Molduras dos monitores
            pygame.draw.rect(
                tela,
                (25, 25, 30),
                (x + 48, 299, 78, 43),
                border_radius=3
            )

            # Tela
            pygame.draw.rect(
                tela,
                (45, 55, 65),
                (x + 53, 304, 68, 33)
            )

            # Base do monitor
            pygame.draw.rect(
                tela,
                (65, 65, 70),
                (x + 83, 342, 12, 4)
            )

            # Teclados 
            pygame.draw.rect(
                tela,
                (40, 40, 45),
                (x + 58, 348, 55, 6)
            )

            # Encosto da cadeira
            pygame.draw.rect(
                tela,
                (38, 40, 45),
                (x + 64, 378, 48, 47),
                border_radius=9
            )

        # terceira fileira de computadores - primeiro plano 
        for x in (50, 355, 660):

            # Tampo da mesa
            pygame.draw.rect(
                tela,
                (210, 210, 210),
                (x, 418, 240, 14),
                border_radius=2
            )

            # Sustentações 
            pygame.draw.rect(
                tela,
                (135, 135, 140),
                (x + 15, 432, 10, 45)
            )

            pygame.draw.rect(
                tela,
                (135, 135, 140),
                (x + 215, 432, 10, 45)
            )

            # Moldura do Monitor
            pygame.draw.rect(
                tela,
                (25, 25, 30),
                (x + 81, 360, 78, 45)
            )

            # Tela do monitor
            pygame.draw.rect(
                tela,
                (45, 55, 65),
                (x + 81, 360, 78, 45)
            )

            # Suporte do monitor
            pygame.draw.rect(
                tela,
                (65, 65, 70),
                (x + 116, 410, 10, 8)
            )

            # Teclado
            pygame.draw.rect(
                tela,
                (40, 40, 45),
                (x + 90, 422, 65, 6),
                border_radius=2
            )

            # Encosto da cadeira
            pygame.draw.rect(
                tela,
                (38, 40, 45),
                (x + 88, 448, 65, 48),
                border_radius=9
            )

            # Contorno da cadeira
            pygame.draw.rect(
                tela,
                (95, 100, 105), 
                (x + 88, 448, 65, 48),
                2,
                border_radius=9
            )

        # Apresentação inicial do grad05
        if self.mostrando_sala:
            fonte_intro = pygame.font.Font(None, 28)
            
            aviso = fonte_intro.render(
              "APERTE ESPAÇO PARA INICIAR A NARRATIVA",
               True,
               (230, 200, 130)
            )
        
            tela.blit(aviso, aviso.get_rect(center=(480, 510))
            )
        
            return

        # Fundo da caixa de diálogo
        pygame.draw.rect(
            tela,
            (35, 35, 50),
            (70, 280, 820, 210),
            border_radius=12
        )

        # Borda da caixa de diálogo
        pygame.draw.rect(
            tela,
            (180, 180, 200),
            (70, 280, 820, 210),
            3,
            border_radius=12
        )

        fonte = pygame.font.Font(None, 32)

        texto_atual = self.quadros[self.indice]
    
        nome = "NARRADOR"

        personagens = [
            "Levi",
            "Flagelo Fulgurante",
            "PV",
            "AH",
            "SM"
        ]

        for personagem in personagens:
            if texto_atual.startswith(personagem + ":"):
                nome = personagem.upper()
                texto_atual = texto_atual[len(personagem) + 1:].strip()

        cores_nomes = {
            "NARRADOR":(200, 200, 210),
            "LEVI":(150, 200, 255),
            "FLAGELO FULGURANTE":(255, 155, 115),
            "PV":(190, 160, 255),
            "AH":(255, 170, 200),
            "SM":(150, 230, 170)
        }

        cor_nome = cores_nomes.get(nome, (230, 200, 130))

        fonte_nome = pygame.font.Font(None, 30)

        if nome != "NARRADOR":
            texto_nome = fonte_nome.render(
             nome,
             True,
             cor_nome
           )
           
            tela.blit(texto_nome, (100, 295))

        if nome == "NARRADOR":
            cor_texto = (200, 200, 210)
        else:
            cor_texto = (255, 225, 175)

        palavras = texto_atual.split()

        linhas = []
        linha = ""

        largura_maxima = tela.get_width()- 200

        for palavra in palavras:
            teste = linha + " " + palavra

            if fonte.size(teste)[0] <= largura_maxima:
                linha = teste
            else:
                linhas.append(linha)
                linha = palavra

        if linha:
            linhas.append(linha)

        for i in range(len(linhas)):
            texto = fonte.render(
                linhas[i],
                True,
                cor_texto
           )

            tela.blit(texto, (100, 330 + i * 32))

        fonte_avanco = pygame.font.Font(None, 24)

        # Avanço da cutscene
        texto_avanco = fonte_avanco.render(
            "APERTE A TECLA ESPAÇO PARA PROSSEGUIR",
            True,
            (170, 170, 185)
        )

        tela.blit(
            texto_avanco,
            texto_avanco.get_rect(
                right=tela.get_width() - 90,
                top=505
            )
        )

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
