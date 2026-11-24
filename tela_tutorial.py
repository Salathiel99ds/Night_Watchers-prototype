import pygame
from jogador import Jogador


class TelaTutorial:
    def __init__(self):
        self.fonte_titulo = pygame.font.SysFont("Arial", 40)
        self.fonte_texto = pygame.font.SysFont("Arial", 22)
        self.fonte_pequena = pygame.font.SysFont("Arial", 18)

        self.obstaculos = [
            pygame.Rect(0, 0, 960, 90),
            pygame.Rect(0, 450, 960, 90)
        ]

        self.reiniciar()

    def reiniciar(self):
        self.etapa = 0
        self.jogador = Jogador(200, 254)
        self.vida_levi = 100
        self.defendendo = False
        self.recarga_sign = 0
        self.mostrar_golpe_ate = 0
        self.angulo_golpe = 0
        self.levi_atingido_ate = 0

        # stickman
        self.inimigo = pygame.Vector2(700, 240)
        self.vida_inimigo = 100
        self.estado_inimigo = "andando"
        self.tempo_inimigo = 1.5
        self.inimigo_atingido_ate = 0

        self.acertos = 0
        self.bloqueios = 0
        self.aviso = ""
        self.mostrar_aviso_ate = 0

        # quick time event do barricades
        self.qte_ativo = False
        self.qte_cliques = 0
        self.qte_tempo = 0
        self.qte_meta = 8
        self.qte_limite = 3

        # sequência de golpes do barricades
        self.combo_restante = 0
        self.combo_tempo = 0

    def processar_evento(self, evento):
        if evento.type != pygame.KEYDOWN:
            return ""

        if evento.key == pygame.K_ESCAPE:
            return "voltar"

        if self.combo_restante > 0:
            return ""

        if self.qte_ativo:
            if evento.key == pygame.K_SPACE:
                self.qte_cliques += 1
            return ""

        if self.etapa == 0 and evento.key == pygame.K_RETURN:
            self.etapa = 1

        elif self.etapa == 4 and evento.key == pygame.K_RETURN:
            return "concluido"

        elif evento.key == pygame.K_j and self.etapa in (1, 2, 3):
            self.usar_sign()

        elif evento.key == pygame.K_l and self.etapa == 3:
            self.usar_barricades()

        return ""

    def atualizar(self, teclas, dt):
        if self.etapa in (0, 4):
            return

        if self.qte_ativo:
            self.qte_tempo -= dt

            if self.qte_cliques >= self.qte_meta:
                self.qte_ativo = False
                self.combo_restante = 6
                self.combo_tempo = 0

            elif self.qte_tempo <= 0:
                self.qte_ativo = False
                self.mostrar_aviso("Falhou! Aperte L para tentar de novo.")
            return

        if self.combo_restante > 0:
            self.atualizar_combo(dt)
            return

        self.recarga_sign = max(self.recarga_sign - dt, 0)
        self.defendendo = teclas[pygame.K_k]

        if self.defendendo:
            self.jogador.velocidade = 120
        else:
            self.jogador.velocidade = 240

        self.jogador.atualizar(teclas, dt, self.obstaculos)
        self.jogador.limitar_na_tela(960, 540)

        if self.etapa >= 2:
            self.atualizar_inimigo(dt)

    def atualizar_combo(self, dt):
        self.combo_tempo -= dt
        if self.combo_tempo > 0:
            return

        self.vida_inimigo -= -(-self.vida_inimigo // self.combo_restante)
        self.combo_restante -= 1
        self.combo_tempo = 0.12

        if self.combo_restante % 2 == 0:
            self.angulo_golpe = 30
        else:
            self.angulo_golpe = -30

        self.mostrar_golpe_ate = pygame.time.get_ticks() + 100
        self.inimigo_atingido_ate = pygame.time.get_ticks() + 100

        if self.combo_restante == 0:
            self.etapa = 4

    def atualizar_inimigo(self, dt):
        alvo = self.centro_jogador()
        centro = self.centro_inimigo()
        distancia = alvo.distance_to(centro)

        if self.estado_inimigo == "andando":
            if distancia > 50:
                direcao = (alvo - centro).normalize()
                self.inimigo += direcao * 110 * dt
                self.inimigo.y = max(90, min(self.inimigo.y, 450 - 60))

            self.tempo_inimigo -= dt

            if self.tempo_inimigo <= 0 and distancia <= 90:
                self.estado_inimigo = "preparando"
                self.tempo_inimigo = 0.6

        elif self.estado_inimigo == "preparando":
            self.tempo_inimigo -= dt

            if self.tempo_inimigo <= 0:
                self.golpe_inimigo(distancia)
                self.estado_inimigo = "andando"
                self.tempo_inimigo = 1.5

    def golpe_inimigo(self, distancia):
        if distancia > 80:
            return

        if self.defendendo:
            self.mostrar_aviso("Bloqueado!")

            if self.etapa == 2:
                self.bloqueios += 1
                if self.bloqueios >= 2:
                    self.etapa = 3
        else:
            self.vida_levi = max(self.vida_levi - 15, 10)
            self.levi_atingido_ate = pygame.time.get_ticks() + 150

    def usar_sign(self):
        if self.recarga_sign > 0 or self.defendendo:
            return

        self.recarga_sign = 0.4
        self.angulo_golpe = 0
        self.mostrar_golpe_ate = pygame.time.get_ticks() + 120

        if self.centro_jogador().distance_to(self.centro_inimigo()) <= 70:
            self.vida_inimigo = max(self.vida_inimigo - 8, 40)
            self.inimigo_atingido_ate = pygame.time.get_ticks() + 150

            if self.etapa == 1:
                self.acertos += 1
                if self.acertos >= 3:
                    self.etapa = 2

    def usar_barricades(self):
        if self.vida_levi > 30:
            self.mostrar_aviso("Barricades indisponível: Levi precisa estar com 30% de vida ou menos.")
            return

        self.qte_ativo = True
        self.qte_cliques = 0
        self.qte_tempo = self.qte_limite

    def mostrar_aviso(self, texto):
        self.aviso = texto
        self.mostrar_aviso_ate = pygame.time.get_ticks() + 2000

    def centro_jogador(self):
        return self.jogador.posicao + pygame.Vector2(16, 16)

    def centro_inimigo(self):
        return self.inimigo + pygame.Vector2(15, 30)

    def direcao_inimigo(self):
        direcao = self.centro_inimigo() - self.centro_jogador()
        if direcao.length_squared() == 0:
            return pygame.Vector2(1, 0)
        return direcao.normalize()

    def desenhar(self, tela):
        agora = pygame.time.get_ticks()

        # arena
        tela.fill((185, 180, 169))
        for parede in self.obstaculos:
            pygame.draw.rect(tela, (95, 95, 95), parede)

        if self.vida_inimigo > 0:
            self.desenhar_stickman(tela, agora)

        self.jogador.desenhar(tela)
        jogador_rect = pygame.Rect(
            round(self.jogador.posicao.x),
            round(self.jogador.posicao.y),
            32, 32
        )

        if self.defendendo:
            pygame.draw.rect(tela, (120, 200, 255), jogador_rect.inflate(14, 14), 3, border_radius=6)

        if agora < self.levi_atingido_ate:
            pygame.draw.rect(tela, (220, 65, 65), jogador_rect, 3)

        if agora < self.mostrar_golpe_ate:
            direcao = self.direcao_inimigo().rotate(self.angulo_golpe)
            inicio = self.centro_jogador() + direcao * 18
            fim = self.centro_jogador() + direcao * 70
            pygame.draw.line(tela, (255, 255, 255), inicio, fim, 5)

        self.desenhar_barra(tela, "Levi", self.vida_levi, 20)
        self.desenhar_barra(tela, "Stickman", self.vida_inimigo, 720)

        if agora < self.mostrar_aviso_ate:
            aviso = self.fonte_pequena.render(self.aviso, True, (255, 215, 0))
            tela.blit(aviso, aviso.get_rect(center=(480, 110)))

        self.desenhar_instrucoes(tela)

        if self.etapa == 0:
            self.desenhar_caixa(tela, "TUTORIAL", [
                "Mova Levi com WASD ou as setas.",
                "J - Sign (ataque normal)",
                "K - FTLL (defesa, segure)",
                "L - Barricades (sequência de golpes)",
                "Pressione ENTER para começar"
            ])

        elif self.etapa == 4:
            self.desenhar_caixa(tela, "TUTORIAL CONCLUÍDO", [
                "O stickman foi derrotado!",
                "Pressione ENTER para voltar ao menu"
            ])

        if self.qte_ativo:
            self.desenhar_qte(tela)

    def desenhar_stickman(self, tela, agora):
        x = round(self.inimigo.x)
        y = round(self.inimigo.y)

        if agora < self.inimigo_atingido_ate:
            cor = (255, 255, 255)
        elif self.estado_inimigo == "preparando" and self.etapa >= 2:
            cor = (220, 65, 65)
        else:
            cor = (20, 20, 20)

        pygame.draw.circle(tela, cor, (x + 15, y + 10), 10, 3)
        pygame.draw.line(tela, cor, (x + 15, y + 20), (x + 15, y + 42), 3)
        pygame.draw.line(tela, cor, (x + 15, y + 42), (x + 3, y + 60), 3)
        pygame.draw.line(tela, cor, (x + 15, y + 42), (x + 27, y + 60), 3)

        if self.estado_inimigo == "preparando" and self.etapa >= 2:
            pygame.draw.line(tela, cor, (x + 15, y + 26), (x + 2, y + 10), 3)
            pygame.draw.line(tela, cor, (x + 15, y + 26), (x + 28, y + 10), 3)
        else:
            pygame.draw.line(tela, cor, (x + 15, y + 26), (x + 2, y + 36), 3)
            pygame.draw.line(tela, cor, (x + 15, y + 26), (x + 28, y + 36), 3)

    def desenhar_barra(self, tela, nome, vida, x):
        texto = self.fonte_pequena.render(nome, True, (235, 235, 235))
        tela.blit(texto, (x, 18))

        if vida <= 30:
            cor = (255, 215, 0)
        else:
            cor = (70, 180, 90)

        pygame.draw.rect(tela, (40, 40, 40), (x, 45, 220, 18))
        pygame.draw.rect(tela, cor, (x, 45, 220 * vida // 100, 18))
        pygame.draw.rect(tela, (235, 235, 235), (x, 45, 220, 18), 2)

    def desenhar_instrucoes(self, tela):
        if self.etapa == 1:
            titulo = "ATAQUE NORMAL (SIGN)"
            texto = f"Chegue perto do stickman e aperte J para atacar. Acertos: {self.acertos}/3"
        elif self.etapa == 2:
            titulo = "DEFESA (FTLL)"
            texto = f"Segure K quando o stickman ficar vermelho. Bloqueios: {self.bloqueios}/2"
        elif self.etapa == 3:
            titulo = "ATAQUE ESPECIAL (BARRICADES)"
            texto = "Com Levi em 30% de vida ou menos, aperte L para uma sequência de golpes."
        else:
            return

        linha1 = self.fonte_texto.render(titulo, True, (255, 215, 0))
        linha2 = self.fonte_pequena.render(texto, True, (235, 235, 235))

        tela.blit(linha1, linha1.get_rect(center=(480, 478)))
        tela.blit(linha2, linha2.get_rect(center=(480, 512)))

    def desenhar_caixa(self, tela, titulo, linhas):
        pygame.draw.rect(tela, (30, 30, 40), (180, 120, 600, 300), border_radius=10)

        texto_titulo = self.fonte_titulo.render(titulo, True, (255, 215, 0))
        tela.blit(texto_titulo, texto_titulo.get_rect(center=(480, 165)))

        for i in range(len(linhas)):
            texto = self.fonte_texto.render(linhas[i], True, (240, 240, 240))
            tela.blit(texto, texto.get_rect(center=(480, 225 + i * 38)))

    def desenhar_qte(self, tela):
        pygame.draw.rect(tela, (30, 30, 40), (230, 170, 500, 200), border_radius=10)

        titulo = self.fonte_titulo.render("APERTE ESPAÇO!", True, (255, 215, 0))
        tela.blit(titulo, titulo.get_rect(center=(480, 210)))

        progresso = min(self.qte_cliques / self.qte_meta, 1)
        pygame.draw.rect(tela, (40, 40, 40), (280, 260, 400, 26))
        pygame.draw.rect(tela, (70, 160, 240), (280, 260, 400 * progresso, 26))
        pygame.draw.rect(tela, (235, 235, 235), (280, 260, 400, 26), 2)

        texto = self.fonte_texto.render(
            f"{self.qte_cliques}/{self.qte_meta}   Tempo: {max(self.qte_tempo, 0):.1f}s", True, (240, 240, 240)
        )
        tela.blit(texto, texto.get_rect(center=(480, 325)))
