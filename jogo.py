import time
import pygame

pygame.init()

janela = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Ping Pong')

BRANCO = (255, 255, 255)
PRETO  = (0, 0, 0)

raquete1_x, raquete1_y = 50, 225
raquete2_x, raquete2_y = 450, 225
bola_x, bola_y = 250, 250

velocidade_inicial_x, velocidade_inicial_y = 0.08, 0.16
velocidade_bola_x, velocidade_bola_y = velocidade_inicial_x, velocidade_inicial_y

velocidade_raquete = 0.5

raquete_largura, raquete_altura = 20, 100
bola_largura, bola_altura = 20, 20

placar1 = 0
placar2 = 0

font = pygame.font.SysFont(None, 55)

def desenhar():
    janela.fill(BRANCO)
    pygame.draw.rect(janela, PRETO, (raquete1_x, raquete1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(janela, PRETO, (raquete2_x, raquete2_y, raquete_largura, raquete_altura))
    pygame.draw.ellipse(janela, PRETO, (bola_x, bola_y, bola_largura, bola_altura))
    placar_texto = font.render(f'{placar1}  |  {placar2}', True, PRETO)
    janela.blit(placar_texto, (200, 20))

tempo_inicial = pygame.time.get_ticks()

# Variável de controle para pausa após ponto
esperando_ponto = False

LOOP = True
while LOOP:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            LOOP = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < 500 - raquete_altura:
        raquete1_y += velocidade_raquete
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500 - raquete_altura:
        raquete2_y += velocidade_raquete

    if not esperando_ponto:
        bola_x += velocidade_bola_x
        bola_y += velocidade_bola_y

    if bola_y <= 0 or bola_y >= 500 - bola_altura:
        velocidade_bola_y = -velocidade_bola_y

    # Detecção de colisão com raquete1 (lado esquerdo)
    if (raquete1_x < bola_x + bola_largura <= raquete1_x + raquete_largura) and (raquete1_y < bola_y + bola_altura and bola_y < raquete1_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
        bola_x = raquete1_x + raquete_largura  # Corrige a posição da bola para não "deslizar"

    # Detecção de colisão com raquete2 (lado direito)
    if (raquete2_x <= bola_x + bola_largura < raquete2_x + raquete_largura) and (raquete2_y < bola_y + bola_altura and bola_y < raquete2_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
        bola_x = raquete2_x - bola_largura  # Corrige a posição da bola para não "deslizar"

    if bola_x <= 0:
        placar2 += 1
        bola_x, bola_y = 250, 250
        velocidade_bola_x, velocidade_bola_y = velocidade_inicial_x, velocidade_inicial_y
        esperando_ponto = True  # Inicia a espera após ponto
        tempo_pausa = pygame.time.get_ticks()  # Marca o tempo de início da pausa

    if bola_x >= 500 - bola_largura:
        placar1 += 1
        bola_x, bola_y = 250, 250
        velocidade_bola_x, velocidade_bola_y = velocidade_inicial_x, velocidade_inicial_y
        esperando_ponto = True  # Inicia a espera após ponto
        tempo_pausa = pygame.time.get_ticks()  # Marca o tempo de início da pausa

    # Verifica se passou 1 segundo após marcar ponto
    if esperando_ponto and pygame.time.get_ticks() - tempo_pausa >= 1000:
        esperando_ponto = False  # Termina a pausa

    tempo_decorrido = pygame.time.get_ticks() - tempo_inicial
    if tempo_decorrido > 2500:
        velocidade_bola_x *= 1.05
        velocidade_bola_y *= 1.05
        tempo_inicial = pygame.time.get_ticks()

    desenhar()

    pygame.display.update()

pygame.quit()
