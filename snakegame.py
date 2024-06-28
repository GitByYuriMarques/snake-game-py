import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definindo cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
dark_green = (0, 100, 0)
light_green = (144, 238, 144)

# Definindo dimensões da tela
display_width = 800
display_height = 600

# Inicializando a tela
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Jogo da Cobrinha')

# Definindo o clock
clock = pygame.time.Clock()

# Tamanho do bloco da cobrinha
snake_block = 10

# Velocidade da cobrinha
snake_speed = 15

# Carregar imagens
apple_img = pygame.image.load('apple.png')
background_img = pygame.image.load('background.jpg')

# Redimensionar imagens se necessário
apple_img = pygame.transform.scale(apple_img, (snake_block, snake_block))
background_img = pygame.transform.scale(background_img, (display_width, display_height))

# Definindo fontes com tamanhos diferentes
font_style = pygame.font.SysFont(None, 40)
score_font = pygame.font.SysFont(None, 25)

# Função para mostrar a pontuação na tela
def your_score(score):
    value = score_font.render("Pontuação: " + str(score), True, black)
    dis.blit(value, [10, 10])

# Função para desenhar a cobrinha na tela
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, dark_green, [x[0], x[1], snake_block, snake_block])
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block], 1)  # Borda branca

# Função para desenhar a comida na tela
def draw_food(foodx, foody):
    dis.blit(apple_img, (foodx, foody))

# Função para mostrar uma mensagem na tela
def message(msg, color, size):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(display_width / 2, display_height / 3))
    dis.blit(mesg, text_rect)

# Função principal do jogo
def gameLoop():
    game_over = False  # Variável para verificar se o jogo acabou
    game_close = False  # Variável para verificar se o jogo está em estado de fim

    # Posição inicial da cobrinha
    x1 = display_width / 2
    y1 = display_height / 2

    # Mudança de posição da cobrinha
    x1_change = 0
    y1_change = 0

    # Lista para armazenar os segmentos da cobrinha
    snake_List = []
    Length_of_snake = 1  # Comprimento inicial da cobrinha ajustado para 1

    # Posição inicial da comida
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    # Loop principal do jogo
    while not game_over:

        # Loop para quando o jogador perde o jogo
        while game_close == True:
            dis.fill(light_green)  # Cor de fundo quando perde
            message("Game Over! Pressione F para Fechar ou C para Continuar", red, 40)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # Verificar se o jogador deseja sair ou reiniciar o jogo
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        return  # Certifique-se de retornar para evitar múltiplos loops de jogo

        # Verificar eventos do teclado para movimentação da cobrinha
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Verificar se a cobrinha colidiu com as bordas da tela
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        # Desenhar o fundo
        dis.blit(background_img, (0, 0))

        # Desenhar a comida na tela
        draw_food(foodx, foody)

        # Atualizar a lista da cobrinha
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Verificar se a cobrinha colidiu com si mesma
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Desenhar a cobrinha e a pontuação na tela
        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        # Atualizar a tela
        pygame.display.update()

        # Verificar se a cobrinha comeu a comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        # Controlar a velocidade da cobrinha
        clock.tick(snake_speed)

    # Sair do Pygame
    pygame.quit()
    quit()

# Iniciar o jogo
gameLoop()
