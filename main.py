import pygame
import math
from pygame.locals import *
import sys
from pygame import mixer


pygame.init()
mixer.init()
matriz=[
"CCCCCCCCCCC...................................................C..........................",
"Chhhhhhhhh....................................................C...........................",
"Chhhhhhhhh....................................................C...........................",
"ChhShhhhhh....................................................C...........................",
"Chh.hhhhhh....................................................C...........................",
"Chhhhhhhhh....................................................C..........................",
"PPPPPPPPPP....................................................C..........................",
"..............................................................C..........................",
"DDDDDDDDDD....E...............................................C..........................",
"..............................................................C..........................",
"DDDDDDDDDD....................................................C..........................",
"...................M..........................................C..........................",
"DDDDDDDDDD..............V.....................................C..........................",
"..............................................................C..........................",
"CCCCCCCCCC...............M..............V.....................C..........................",
"CCCCCCCCCC........................M...........................C.........................",
"CCCCCCCCCC.................................M..................C.........................",
"CCCCCCCCCC.......................................V............C..........................",
"CCCCCCCCCC....................................................C..........................",
"CCCCCCCCCC.........................................M..........C.........................",
"CCCCCCCCCC....................................................C..........................",
"CCCCCCCCCC..........................................V.........C..........................",
"CCCCCCCCCC.................................................M..C..........................",
"CCCCCCCCCC...................................V................C..........................",
"CCCCCCCCCC....................................................C..........................",
"CCCCCCCCCC............................PPPPPPPPPPPPPPPPPPPPPPPPP...........................",
"CCCCCCCCCC.......................M.......................................................",
"CCCCCCCCCC..............M.............DDDDDDDDDDDDDDDDDDDDDDDDD..........................",
"CCCCCCCCCC.....G.........................................................................",
"CCCCCCCCCC.....M......................DDDDDDDDDDDDDDDDDDDDDDDDD..........................",
"CCCCCCCCCC...............................................................................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC.......M....................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC.............G..............CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC.............M..............CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
 "CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC...........................",
"CCCCCCCCCC.........................CCCCCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC....................Z.......CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC.........................G.ACCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC........................CCCCCCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC..................M.........CCCCCCCCCCCCCCCCCCCCCCCCC...........................",
"CCCCCCCCCC........M...................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC.............G..............CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC.............C..............CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC.............M..............CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC.......M....................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC.....M......................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"CCCCCCCCCC............................CCCCCCCCCCCCCCCCCCCCCCCCC..........................",
"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPCCCCCCCCCCCCCCCCCCCCCCCCC...........................",
"......................................CCCCCCCCCCCCCCCCCCCCCCCCC...........................",
"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDCCCCCCCCCCCCCCCCCCCCCCCCC...........................",
"......................................CCCCCCCCCCCCCCCCCCCCCCCCC...........................",
"DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDCCCCCCCCCCCCCCCCCCCCCCCCC..........................",
]
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Dangerous Jump')
BlocoLar = largura/16
BlocoAl = altura/12
pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load("sons/som_epico.mp3")
pygame.mixer.music.play(-1)
som_pulo = pygame.mixer.Sound("sons/pulo.wav")
fonte_texto = pygame.font.SysFont("impact", 30, False)
fonte_texto2 = pygame.font.SysFont("adventure", 70, True)



caracteres = pygame.image.load("personagem_aventureiro.png")
cenario = pygame.image.load("tileset.png")
branco = (255, 255, 255)
background = pygame.image.load("ceu2.jpg")
background = pygame.transform.scale(background, (largura, altura))
background2 = pygame.image.load("fundo_inicio.png")
background2 = pygame.transform.scale(background2, (largura, altura))
background3 = pygame.image.load("game_over.jpg")
background3 = pygame.transform.scale(background3, (largura, altura))

relogio = pygame.time.Clock()
alavanca = pygame.image.load("palanca.png")
estado = "TELA INICIAL"
vida = 100

#bloco com grama
class Bloco(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        bloco_orig = cenario.subsurface((4,1), (40, 42))
        self.image = pygame.transform.scale(bloco_orig, (BlocoLar*2, BlocoAl*2))
        x = coluna * BlocoLar
        y = linha * BlocoAl
        self.rect = pygame.Rect((x,y), (BlocoLar*2, BlocoAl*2))
#bloco de pedra
class Blocos2(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        bloco2_orig = cenario.subsurface((150, 160), (40, 42))
        self.image = pygame.transform.scale(bloco2_orig, (BlocoLar*1.3, BlocoAl))
        x = coluna * BlocoLar
        y = linha * BlocoAl
        self.rect = pygame.Rect((x, y), (BlocoLar*1.3, BlocoAl))
#bloco sem grama
class Bloco3(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        bloco3_orig = cenario.subsurface((4,10), (40, 35))
        self.image = pygame.transform.scale(bloco3_orig, (BlocoLar*2, BlocoAl*2))
        x = coluna * BlocoLar
        y = linha * BlocoAl
        self.rect = pygame.Rect((x,y), (BlocoLar*2, BlocoAl*2))
#bloquinho
class Bloco4(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        bloco4_orig = cenario.subsurface((48,48), (16, 30))
        self.image = pygame.transform.scale(bloco4_orig, (BlocoLar//1.5, BlocoAl//1.5))
        x = coluna * BlocoLar
        y = linha * BlocoAl
        self.rect = pygame.Rect((x,y), (BlocoLar//1.5, BlocoAl//1.5))

class Bloco_sem_colisao(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        bloco5_orig = cenario.subsurface((150,160), (40, 42))
        self.image = pygame.transform.scale(bloco5_orig, (BlocoLar*2, BlocoAl*2))
        x = coluna * BlocoLar
        y = linha * BlocoAl
        self.rect = pygame.Rect((x,y), (BlocoLar*2, BlocoAl*2))

#plataformas fixas
class Plataformas(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        plataforma_orig = cenario.subsurface((0, 48), (48, 16))
        self.image = pygame.transform.scale(plataforma_orig, (BlocoLar*2.5, BlocoAl/1.5))
        self.cord_x = coluna * BlocoLar
        self.cord_y = linha * BlocoAl
        self.rect = pygame.Rect((self.cord_x, self.cord_y), (BlocoLar*2.5, BlocoAl/1.5))
        self.timer = 0
#plataformas móveis
class Plataformas2(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        plataforma2_orig = cenario.subsurface((0, 48), (48, 16))
        self.image = pygame.transform.scale(plataforma2_orig, (BlocoLar*2.5, BlocoAl/1.5))
        self.cord_x = coluna * BlocoLar
        self.cord_y = linha * BlocoAl
        self.rect = pygame.Rect((self.cord_x, self.cord_y), (BlocoLar*2.5, BlocoAl/1.5))
        self.timer = 0

    def update(self, *args):
        self.timer += 0.01
        self.rect.x = self.cord_x + math.sin(self.timer) *300
# ferros perfurantes
class Perfurante(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        perf_orig = cenario.subsurface((40, 160), (38, 15))
        self.image = pygame.transform.scale(perf_orig, (BlocoLar*1.5, BlocoAl//1.5))
        x = coluna * BlocoLar
        y = linha * 50.55
        self.rect = pygame.Rect((x, y), (BlocoLar, BlocoAl//1.5))
#personagem
class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames_andar = []
        self.frames_andar.append(pygame.image.load("boneco_andando/0.png"))
        self.frames_andar.append(pygame.image.load("boneco_andando/1.png"))
        self.frames_andar.append(pygame.image.load("boneco_andando/2.png"))
        self.frames_andar.append(pygame.image.load("boneco_andando/3.png"))
        self.frames_andar.append(pygame.image.load("boneco_andando/4.png"))
        self.frames_andar.append(pygame.image.load("boneco_andando/5.png"))
        self.frames_andar.append(pygame.image.load("boneco_andando/6.png"))
        self.frames_andar.append(pygame.image.load("boneco_andando/7.png"))
        self.frames_parado = []
        self.frames_parado.append(pygame.image.load("boneco_parado/0.png"))
        self.frames_parado.append(pygame.image.load("boneco_parado/1.png"))
        self.frames_parado.append(pygame.image.load("boneco_parado/2.png"))
        self.frames_parado.append(pygame.image.load("boneco_parado/3.png"))
        self.frames_parado.append(pygame.image.load("boneco_parado/4.png"))
        self.frames_parado.append(pygame.image.load("boneco_parado/5.png"))
        self.frames_parado.append(pygame.image.load("boneco_parado/6.png"))
        self.frames_parado.append(pygame.image.load("boneco_parado/7.png"))
        self.pulando = pygame.image.load("pulando.png")
        self.atual = 0
        self.image = self.frames_andar[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (45, 75))
        self.pulo = True
        self.no_ar = False
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.rect = pygame.Rect((700, 2500), (38, 70))
        self.gravidade = 0.9
        self.intencao_posicao = list(self.rect.center)
    def mover_esquerda(self):
        self.velocidade_x = -8

    def mover_direita(self):
        self.velocidade_x = 8



    def update(self, *args):
        self.velocidade_y += self.gravidade
        self.intencao_posicao[0] += self.velocidade_x
        self.intencao_posicao[1] += self.velocidade_y
        self.atual += 0.2
        if self.atual >= len(self.frames_andar):
            self.atual = 0
        if self.velocidade_x>0:
            self.image = self.frames_andar[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (45, 75))
        elif self.velocidade_x==0:
            self.image = self.frames_parado[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (45,75))
        elif self.velocidade_x<0:
            self.image = self.frames_andar[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (45, 75))
            self.image = pygame.transform.flip(self.image, True, False)
        if self.velocidade_x>0 and self.velocidade_y<0 or self.velocidade_x==0 and self.velocidade_y<0 :
            self.image = self.pulando
            self.image = pygame.transform.scale(self.image, (45, 75))
        if self.velocidade_x<0 and self.velocidade_y<0:
            self.image = self.pulando
            self.image = pygame.transform.scale(self.image, (45, 75))
            self.image = pygame.transform.flip(self.image, True, False)


    def parar_horizontal(self):
        self.velocidade_x = 0

    def autorizar_movimento(self):
        self.rect.center = self.intencao_posicao

    def recusar_movimento(self):
        self.intencao_posicao = list(self.rect.center)

    def teste_colisao(self, grupo):
        temp = self.rect.center
        self.rect.center = self.intencao_posicao
        if not pygame.sprite.spritecollide(personagem, grupo, False):
            self.autorizar_movimento()
            self.gravidade = 0.9
        else:
            self.rect.center = temp
            self.velocidade_y = 0
            self.gravidade = 0
            self.recusar_movimento()

    def pular(self):
        if self.velocidade_y == 0 or self.velocidade_y == 0.9 or self.velocidade_y==1.8:
            som_pulo.play()
            self.velocidade_y = -20
            valor = self.intencao_posicao[1]
            self.intencao_posicao[1] += self.velocidade_y
            print(self.velocidade_y)
            self.gravidade = 0.9

        else:
            pass

#faz a camera
class Camera:
    def __init__(self, posicao, tamanho):
        self.janela = pygame.Rect(posicao, tamanho)
        self.posicao = posicao
        self.offset_x = 0
        self.offset_y =0
        self.limpar_imagem = pygame.Surface(self.janela.size)
        self.limpar_imagem.blit(background, (0, 0))
        self.draw_area = pygame.Surface(self.janela.size)

    def in_viewport(self, r):
        return self.janela.colliderect(r)
    def move(self, pos):
        self.janela.center = pos
        self.offset_x = self.janela.x
        self.offset_y = self.janela.y
    def start_drawing(self):
        self.draw_area.blit(self.limpar_imagem, (0, 0))
    def paint(self, screen):
        screen.blit(self.draw_area, self.posicao)
        pygame.draw.rect(screen, (0, 0, 0), (self.posicao, self.janela.size), 3)
    def draw_group(self, group):
        for s in group:
            if self.in_viewport(s.rect):
                self.draw_area.blit(s.image,(s.rect.x - self.offset_x, s.rect.y - self.offset_y))
#alavanca
class Acionador(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        acionador_orig = alavanca
        self.image = pygame.transform.scale(acionador_orig, (30, 30))
        x = coluna * BlocoLar
        y = linha * 50.5
        self.rect = pygame.Rect((x,y), (30, 30))
#monstros
class Voadores(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        #voador_orig = monstro_voador
        self.frames_voar = []
        self.frames_voar.append(pygame.image.load("voador/fly01.png"))
        self.frames_voar.append(pygame.image.load("voador/fly02.png"))
        self.frames_voar.append(pygame.image.load("voador/fly03.png"))
        self.frames_voar.append(pygame.image.load("voador/fly04.png"))
        self.frames_voar.append(pygame.image.load("voador/fly05.png"))
        self.frames_voar.append(pygame.image.load("voador/fly06.png"))
        self.frames_voar.append(pygame.image.load("voador/fly07.png"))
        self.atual = 0
        self.image = self.frames_voar[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.cord_x = coluna * BlocoLar
        self.cord_y = linha * BlocoAl
        self.rect = pygame.Rect((self.cord_x, self.cord_y), (50, 40))
        self.timer = 0

    def update(self, *args):
        self.timer += 0.01
        movimento = math.sin(self.timer)
        self.rect.x = self.cord_x + movimento *300
        self.atual += 0.2
        if self.atual >= len(self.frames_voar):
            self.atual = 0
        if movimento>0:
            self.image = self.frames_voar[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (50, 40))
        else:
            self.image = self.frames_voar[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (50, 40))
            self.image = pygame.transform.flip(self.image, True, False)

class Porta_final(pygame.sprite.Sprite):
    def __init__(self, linha, coluna):
        pygame.sprite.Sprite.__init__(self)
        porta_org = pygame.image.load("porta.png")
        self.image = pygame.transform.scale(porta_org, (BlocoLar*3, BlocoAl*3))
        x = coluna * BlocoLar
        y = linha * 52
        self.rect = pygame.Rect((x, y), (BlocoLar*3, BlocoAl*3))


#Grupos
personagem = Personagem()
personagens = pygame.sprite.Group(personagem)
blocos = pygame.sprite.Group()
perfurantes = pygame.sprite.Group()
acionadores = pygame.sprite.Group()
bloco_ponte = pygame.sprite.Group()
portas = pygame.sprite.Group()
blocos_scolisao = pygame.sprite.Group()

#define o que cada tipo de elemento na matriz representa
for linha, lin in enumerate(matriz):
    for coluna in range(0, 80):
        elemento = matriz[linha][coluna]
        if elemento == "P":
            bloco = Bloco(linha, coluna)
            blocos.add(bloco)
        if elemento == "M":
            plataforma = Plataformas(linha, coluna)
            blocos.add(plataforma)
        if elemento == "E":
            plataforma2 = Plataformas2(linha, coluna)
            blocos.add(plataforma2)
        elif elemento == "C":
            bloco2 = Blocos2(linha, coluna)
            blocos.add(bloco2)
        elif elemento == "D":
            bloco3 = Bloco3(linha, coluna)
            blocos.add(bloco3)
        elif elemento == "G":
            perfurante = Perfurante(linha, coluna)
            perfurantes.add(perfurante)
        elif elemento == "A":
            acionador = Acionador(linha, coluna)
            acionadores.add(acionador)
        elif elemento == "Z":
            bloco4 = Bloco4(linha, coluna)
            bloco_ponte.add(bloco4)
        elif elemento == "V":
            voador = Voadores(linha, coluna)
            perfurantes.add(voador)
        elif elemento=="S":
            porta = Porta_final(linha, coluna)
            portas.add(porta)
        elif elemento == "h":
            bloco_scol = Bloco_sem_colisao(linha, coluna)
            blocos_scolisao.add(bloco_scol)


cam = Camera((0,0), (largura, altura)) #atributos da câmera
colidir = False
#loop principal


while True:
    if estado == "JOGANDO":
        relogio.tick(60)
        #desenha os grupos na tela
        cam.start_drawing()
        cam.draw_group(blocos_scolisao)
        cam.draw_group(blocos)
        cam.draw_group(portas)
        cam.draw_group(perfurantes)
        cam.draw_group(acionadores)
        cam.draw_group(personagens)


        colisao2 = pygame.sprite.spritecollide(personagem, acionadores, False)

        if colisao2:
            colidir = True
        else:
            pass
        if colidir == True:
            cam.draw_group(bloco_ponte)
            personagem.teste_colisao(bloco_ponte)

        cam.paint(tela) #pinta a camera
        #tela.fill(branco)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    personagem.mover_direita()
                if event.key == pygame.K_LEFT:
                    personagem.mover_esquerda()
                if event.key == pygame.K_SPACE:
                    personagem.pular()
                if event.key == pygame.K_p:
                    estado = "TELA"

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                    personagem.parar_horizontal()
        colisao = pygame.sprite.spritecollide(personagem, perfurantes, False)

        if colisao:
            vida = 0

            print(vida)
        else:
            pass

        colisao_porta = pygame.sprite.spritecollide(personagem, portas, False)
        if colisao_porta:
            estado = "VITORIA"
        else:
            pass


        blocos.update()
        perfurantes.update()
        personagens.update()

        personagem.teste_colisao(blocos)
        if vida == 0:
            estado = "GAME OVER"

    elif estado=="GAME OVER":
        pygame.mixer.music.stop()
        tela.blit(background3, (0,0))
        mensagem3 = "precione r para tentar novamente"
        texto_formatado3 = fonte_texto.render(mensagem3, False, (255, 255, 50))
        tela.blit(texto_formatado3, (180, 370))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    estado = "JOGANDO"

    elif estado == "TELA INICIAL":
        tela.blit(background2, (0,0))
        mensagem = "Precione qualquer tecla para iniciar"
        texto_formatado = fonte_texto.render(mensagem, False, (255, 255, 255))
        mensagem2 = "Dangerous Jump"
        texto_formatado2 = fonte_texto2.render(mensagem2, False, (255, 255, 0))
        tela.blit(texto_formatado, (170, 350))
        tela.blit(texto_formatado2, (170, 150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                estado = "JOGANDO"
    elif estado == "VITORIA":
        tela.blit(background2, (0, 0))
        mensagem = "Precione r para jogar novamente"
        texto_formatado = fonte_texto.render(mensagem, False, (255, 255, 255))
        mensagem2 = "Parabéns, Você Venceu!"
        texto_formatado2 = fonte_texto2.render(mensagem2, False, (255, 150, 0))
        tela.blit(texto_formatado, (165, 350))
        tela.blit(texto_formatado2, (80, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                estado = "JOGANDO"



    cam.move(personagem.rect.center) #camera move de acordo com o personagem
    pygame.display.update()
