import pygame
import time
from random import randint

pygame.init()
pygame.mixer.init()
pygame.font.init()
fonte_t = pygame.font.Font('fonte2.ttf', 44)
fonte_r = pygame.font.Font('fonterecorde.ttf', 25)

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

tdt = (600, 600)

p = 60
relogio = pygame.time.Clock()

escurecer = pygame.image.load('escurecer.png')
recordes = pygame.image.load('recordes.png')
como_jogar = pygame.image.load('tutorial.png')
menus = pygame.image.load('menu.png')
mapas = pygame.image.load('mapas.png')
sprite_o = pygame.image.load('sprite.png')
boneco_i = pygame.image.load('parado.png')
boneco_e = pygame.image.load('esquerda.png')
boneco_d = pygame.image.load('direita.png')
cheio = pygame.image.load('max.png')
parque = pygame.image.load('parque.png')
praia = pygame.image.load('praia.png')
vulcao = pygame.image.load('vulcao.png')
atropelado = pygame.image.load('atropelado.png')
pisoteado = pygame.image.load('pisoteado.png')
afogado = pygame.image.load('afogado.png')
queimado = pygame.image.load('queimado.png')
win = pygame.image.load('venceu.png')
win_recorde = pygame.image.load('recorde.png')

background = []
morte = []

pontuacoes = []

tela = pygame.display.set_mode(tdt)
pygame.display.set_caption('Spritake')

def menu():
  pygame.mixer.music.load('musica_menu.mp3')
  pygame.mixer.music.set_volume(5)
  pygame.mixer.music.play(-1)
  quer_jogar = True
  while quer_jogar:
    tela.blit(menus, (0, 0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quer_jogar = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if 58 < x < 58+251 and 198 < y < 198+66:
          clique()
          mapa()
          background.clear()
          morte.clear()
        if 515 < x < 515+56 and 21 < y < 21+57:
          clique()
          quer_jogar = False
        if 58 < x < 58+251 and 282 < y < 66+282:
          clique()
          recorde()
        if 58 < x < 58+251 and 368 < y < 66+368:
          clique()
          tutorial()
    pygame.display.update()

def gameover():
  pygame.mixer.music.load('musica_menu.mp3')
  pygame.mixer.music.set_volume(5)
  essa_tela = True
  if morte[0] == 'ganhou':
    jornal = win
  elif morte[0] == 'recorde':
    jornal = win_recorde
  elif background[0] == parque:
    jornal = atropelado
  elif background[0] == praia:
    if morte[0] == 'topo':
      jornal = afogado
    if morte[0] == 'lateral':
      jornal = pisoteado
    if morte[0] == 'fundo':
      jornal = atropelado
  elif background[0] == vulcao:
    jornal = queimado
  tela.blit(escurecer, (0, 0))
  tela.blit(jornal, (70, 0))
  pygame.display.update()
  while essa_tela:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        essa_tela = False
        pygame.mixer.music.play(-1)
      if event.type == pygame.MOUSEBUTTONDOWN:
        essa_tela = False
        pygame.mixer.music.play(-1)
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          continue
        else:
          essa_tela = False
          pygame.mixer.music.play(-1)
    
    
def recorde():
  voltar_menu = False
  if pontuacoes == []:
    maior_pont = '--'
    pont_x = 275
  else:
    maior_pont = str(max(pontuacoes))
    pont_x = 275
  while not voltar_menu:
    tela.blit(recordes, (0,0))
    maior_pont_render = fonte_r.render(maior_pont, 1, branco)
    tela.blit(maior_pont_render, (pont_x, 316))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        voltar_menu = True
      if event.type == pygame.MOUSEBUTTONDOWN:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if 20 < x < 20+28 and 34 < y < 34+20:
          clique()
          voltar_menu = True
    pygame.display.update()

def tutorial():
  lendo = True
  while lendo:
    tela.blit(como_jogar, (0,0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        lendo = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if 20 < x < 20+28 and 34 < y < 34+20:
          clique()
          lendo = False
    pygame.display.update()
    
def mapa():
  escolhendo = True
  while escolhendo:
    tela.blit(mapas, (0, 0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        escolhendo = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if 48 < x < 138+48 and 177 < y < 116+177:
          clique()
          background.append(parque)
          escolhendo = False
          pygame.mixer.music.load('musica_parque.mp3')
          jogo()
        if 237 < x < 138+237 and 177 < y < 116+177:
          clique()
          background.append(vulcao)
          escolhendo = False
          pygame.mixer.music.load('musica_vulcao.mp3')
          jogo()
        if 425 < x < 138+425 and 177 < y < 116+177:
          clique()
          background.append(praia)
          escolhendo = False
          pygame.mixer.music.load('musica_praia.mp3')
          jogo()
        if 20 < x < 20+28 and 34 < y < 34+20:
          clique()
          escolhendo = False
      
    pygame.display.update()


def sprite(pls_x, pls_y):
  tela.blit(sprite_o, (pls_x, pls_y))
  
def alarme():
  pygame.mixer.Sound('alarme.mp3').set_volume(50)
  pygame.mixer.Sound('alarme.mp3').play()

def ponto():
  pygame.mixer.Sound('ponto.mp3').set_volume(0.5)
  pygame.mixer.Sound('ponto.mp3').play()

def error():
  pygame.mixer.Sound('error.mp3').set_volume(7)
  pygame.mixer.Sound('error.mp3').play()

def comemoracao():
  pygame.mixer.Sound('ganhou.mp3').set_volume(7)
  pygame.mixer.Sound('ganhou.mp3').play()

def humilhacao():
  pygame.mixer.Sound('perdeu.mp3').set_volume(7)
  pygame.mixer.Sound('perdeu.mp3').play()

def descarte():
  pygame.mixer.Sound('descarte.mp3').set_volume(5)
  pygame.mixer.Sound('descarte.mp3').play()

def clique():
  pygame.mixer.Sound('clique.mp3').set_volume(0.5)
  pygame.mixer.Sound('clique.mp3').play()
  
def jogo():
  pygame.mixer.music.set_volume(0.5)
  pygame.mixer.music.play()
  
  game_over = False
  hitbox = False
  movendo = False
  rodando = False
  
  contador = 0
  segundos = 60
  
  direcao = 'D'
  direcao_v = False
  direcao_h = False
    
  pls_x = randint(57, ((542 - 54)/10) * 10)
  pls_y = randint(157, ((534 - 54)/10) * 10)
  pls_x = (pls_x - 57)//54 * 54 + 57
  while pls_x == 273:
    pls_x = randint(57, ((542 - 54)/10) * 10)
    pls_x = (pls_x - 57)//54 * 54 + 57
  pls_y = (pls_y - 157)//54 * 54 + 157
  while pls_y == 319:
    pls_y = randint(157, ((534 - 54)/10) * 10)
    pls_y = (pls_y - 157)//54 * 54 + 157
  pos_x = 273
  pos_y = 319
  sac_x = 219
  sac_y = 319
  v_x = 0
  v_y = 0
  slow = 0
  sacola = 0
  latinhas = 0

  horizontal = False
  vertical = False

  muda = False
  
  temp = '1:00'
  cor_temp = branco

  fonte_t = pygame.font.Font('fonte2.ttf', 44)
  temptela = fonte_t.render(temp, 1, cor_temp)
  
  while not game_over:
    relogio.tick(p)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
              if hitbox:
                hitbox = False
              else:
                hitbox = False
            else:
              movendo = True
              rodando = True
              if event.key == pygame.K_LEFT:
                horizontal = True
                vertical = False
                v_y = 0
                v_x = -2.5 + slow
                direcao = 'E'
                direcao_h = 'E'
                if direcao_v == 'C':
                  pos_y = (pos_y - 157)//54 * 54 + 157
                if direcao_v == 'B':
                  if (pos_y - 157)%54 > 15:
                    muda = True
                  pos_y = (pos_y - 157)//54 * 54 + 157
                  if muda:
                    pos_y += 54
                    muda = False
                direcao_v = False
              if event.key == pygame.K_RIGHT:
                horizontal = True
                vertical = False
                v_y = 0
                v_x = 2.5 - slow
                direcao = 'D'
                direcao_h = 'D'
                if direcao_v == 'C':
                  pos_y = (pos_y - 157)//54 * 54 + 157
                if direcao_v == 'B':
                  if (pos_y - 157)%54 > 15:
                    muda = True
                  pos_y = (pos_y - 157)//54 * 54 + 157
                  if muda:
                    pos_y += 54
                    muda = False
                direcao_v = False
              if event.key == pygame.K_UP:
                vertical = True
                horizontal = False
                v_x = 0
                v_y = -2.5 + slow
                direcao_v = 'C'
                if direcao_h == 'E':
                  pos_x = (pos_x - 57)//54 * 54 + 57
                if direcao_h == 'D':
                  if (pos_x - 57)%54 > 15:
                    muda = True
                  pos_x = (pos_x - 57)//54 * 54 + 57
                  if muda:
                    pos_x += 54
                    muda = False
                direcao_h = False
              if event.key == pygame.K_DOWN:
                vertical = True
                horizontal = False
                v_x = 0
                v_y = 2.5 - slow
                direcao_v = 'B'
                if direcao_h == 'E':
                  pos_x = (pos_x - 57)//54 * 54 + 57
                if direcao_h == 'D':
                  if (pos_x - 57)%54 > 15:
                    muda = True
                  pos_x = (pos_x - 57)//54 * 54 + 57
                  if muda:
                    pos_x += 54
                    muda = False
                direcao_h = False
            
    tela.blit(background[0], (0, 0))
    if rodando:
      contador += 1
      if contador == 60:
        segundos -= 1
        contador = 0
        if segundos < 0:
          temp = '0:00'
        elif segundos == 10:
          cor_temp = vermelho
          alarme()
        if segundos > 9:
          temp = '0:' + str(segundos)
        else:
          temp = '0:0' + str(segundos)
        fonte_t = pygame.font.Font('fonte2.ttf', 44)
        temptela = fonte_t.render(temp, 1, cor_temp)
      if segundos == 60:
        tela.blit(temptela, (89, 28))
      else:
        tela.blit(temptela, (80, 28))

    if horizontal:
      pos_x += v_x
      sac_x += v_x
    if vertical:
      pos_y += v_y
      sac_y += v_y
    
    if (pls_x - 50) < pos_x < (pls_x + 50) and (pls_y - 50) < pos_y < (pls_y + 50):
      if sacola < 10:
        ponto()
        pls_x_antes = pls_x
        pls_y_antes = pls_y
        pls_x = randint(57, ((542 - 54)/10) * 10)
        pls_y = randint(157, ((534 - 54)/10) * 10)
        pls_x = (pls_x - 57)//54 * 54 + 57
        pls_y = (pls_y - 157)//54 * 54 + 157
        while pls_x == pls_x_antes:
          pls_x = randint(57, ((542 - 54)/10) * 10)
          pls_x = (pls_x - 57)//54 * 54 + 57
        while pls_y == pls_y_antes:
          pls_y = randint(157, ((534 - 54)/10) * 10)
          pls_y = (pls_y - 157)//54 * 54 + 157
        slow += 0.15
        sacola += 1
      elif pls_x == pos_x and pls_y == pos_y:
        error()

    sprite(pls_x+4, pls_y+4)
    
    fonte_s = pygame.font.Font('fonte.ttf', 45)
    latinhastela = fonte_s.render(str(latinhas), 1, branco)
    tela.blit(latinhastela, (514, 20))

    if sacola < 10:
      sacolatela = fonte_s.render(str(sacola), 1, branco)
      tela.blit(sacolatela, (386, 20))
    else:
      tela.blit(cheio, (360, 25))

    if movendo:
      if direcao == 'E':
        tela.blit(boneco_e, (pos_x, pos_y))
      if direcao == 'D':
        tela.blit(boneco_d, (pos_x, pos_y))
    else:
      tela.blit(boneco_i, (pos_x, pos_y))
      if not rodando:
        tela.blit(temptela, (89, 28))
      
    if 486.5 < pos_x < 491.5 and 478.5 < pos_y < 483.5:
      if movendo:
        descarte()
      latinhas += sacola
      slow = 0
      sacola = 0
      movendo = False
      pos_x = 489
      pos_y = 480
      v_x = 0
      v_y = 0
      
    elif pos_x < 57 or pos_x > 543 - 54:
      humilhacao()
      morte.append('lateral')
      game_over = True
      gameover()
    elif pos_y < 157:
      humilhacao()
      morte.append('topo')
      game_over = True
      gameover()
    elif pos_y > 535 - 54:
      humilhacao()
      morte.append('fundo')
      game_over = True
      gameover()
    if segundos < 0:
      comemoracao()
      if pontuacoes == []:
        morte.append('ganhou')
      elif latinhas > max(pontuacoes):
        morte.append('recorde')
      else:
        morte.append('ganhou')
      pontuacoes.append(latinhas)
      game_over = True
      gameover()
      
    pygame.display.update()
    
menu()
pygame.quit()
