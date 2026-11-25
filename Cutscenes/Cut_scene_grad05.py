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

    def processar_evento(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if self.indice < len(self.quadros) - 1:
                    self.indice += 1
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

        # caixa de dialogo
        pygame.draw.rect(
            tela,
            (35, 35, 50),
            (70, 195, 820, 240),
            border_radius=12
        )

        pygame.draw.rect(
            tela,
            (180, 180, 200),
            (70, 195, 820, 240),
            2,
            border_radius=12
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
           
            tela.blit(texto_nome, (100, 200))

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

            tela.blit(texto, (100, 250 + i * 40))

        fonte_avanco = pygame.font.Font(None, 24)

        texto_avanco = fonte_avanco.render(
            "APERTE A TECLA ESPAÇO PARA PROSSEGUIR",
            True,
            (170, 170, 185)
        )

        tela.blit(
            texto_avanco,
            texto_avanco.get_rect(
                right=tela.get_width() - 90,
                top=465
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
