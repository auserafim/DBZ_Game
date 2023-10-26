# Biblioteca PyGame
import pygame
# Biblioteca para geracao de numeros pseudoaleatorios
import random
# Modulo da biblioteca PyGame que permite o acesso as teclas utilizadas
from pygame.locals import *
#Música 
import pygame.mixer
import pygame.sprite
import sys

# Classe que representar o jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        image_player = pygame.image.load("/home/aurelio/Documents/projects/python_projects/dbz_game/freeza-removebg-preview.png")
        scaled_image_player = pygame.transform.scale(image_player, (image_player.get_width() / 4, image_player.get_height() / 6))
        super(Player, self).__init__()
        self.surf = scaled_image_player
        self.rect = self.surf.get_rect()

    # Determina acao de movimento conforme teclas pressionadas
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        # Mantem o jogador nos limites da tela do jogo
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600

# Classe que representa os inimigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        image_inimigo = pygame.image.load("/home/aurelio/Documents/projects/python_projects/dbz_game/poder rosa.png")
        scaled_image_inimigo = pygame.transform.scale(image_inimigo, (image_inimigo.get_width() / 3, image_inimigo.get_height() / 5))

        super(Enemy, self).__init__()
        self.surf = scaled_image_inimigo
        self.rect = self.surf.get_rect( #Coloca na extrema direita (entre 820 e 900) e sorteia sua posicao em relacao a coordenada y (entre 0 e 600)
            center=(random.randint(820, 900), random.randint(0, 600))
            
        )
        self.speed = random.uniform(1, 5) #Sorteia sua velocidade, entre 1 e 15

    # Funcao que atualiza a posiçao do inimigo em funcao da sua velocidade e termina com ele quando ele atinge o limite esquerdo da tela (x < 0)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Vidas do Personagem

def menu_inicial():
    # Carregue a imagem de fundo do menu
    menu_background = pygame.image.load("game_start.jpeg")  # Substitua "menu_background.jpg" pelo caminho da sua imagem de fundo
    menu_background = pygame.transform.scale(menu_background, (800, 600))

    # Desenhe a imagem de fundo do menu
    screen.blit(menu_background, (0, 0))

    pygame.display.flip()  # Atualize a tela

 
def game_over():
     # Carregue a imagem de fundo do menu
    overback = pygame.image.load("game_over.jpeg")  # Substitua "menu_background.jpg" pelo caminho da sua imagem de fundo
    overback= pygame.transform.scale(overback, (800, 600))
    total_pontos_text = font.render(f"Pontuação Total: {pontuacao}", True, (255, 165, 0), (0, 0, 0))
    textRect = total_pontos_text.get_rect()
    textRect.center = (400, 300)  # Posição do texto de pontuação na tela de Game Over
    

    # Desenhe a imagem de fundo do menu
    screen.blit(overback, (0, 0))
    screen.blit(total_pontos_text, textRect)
    pygame.display.flip()  # Atualize a tela
    
    # Aumentar a dificuldade do jogo ao passar do tempo 
def aumentar_dificuldade():
    if pontuacao > 50:
        for enemy in enemies:
            font = pygame.font.Font(None, 38)  # Escolha a fonte e o tamanho desejados
            textos = font.render(f"Keep GOING:", True, (196, 0, 255))  
            textRect = textos.get_rect()
            textRect.center = (400, 300)
            screen.blit(textos)
            enemy.speed = 5
    if pontuacao > 60:
        for enemy in enemies:
            enemy.speed = 10  
    if pontuacao > 70:
        for enemy in enemies:
            enemy.speed = 15
    if pontuacao > 80:
        for enemy in enemies:
            enemy.speed = 20  
    if pontuacao > 100:
        for enemy in enemies:
            enemy.speed = 25 




# Inicializa o jogo por completo

    
pygame.init()


# Inicializa mixer de música 
pygame.mixer.init()
pygame.mixer.music.set_volume (0.3)
pygame.mixer.music.load('musica-2.mp3')
pygame.mixer.music.play(-1)  # O argumento -1 faz com que a música seja reproduzida em um loop infinito

# Cria a tela com resolução 800x600px
screen = pygame.display.set_mode((800, 600))

# Cria um evento para adicao de inimigos
ADDENEMY = pygame.USEREVENT + 1000
pygame.time.set_timer(ADDENEMY, 1000) #Define um intervalo para a criacao de cada inimigo (milisegundos)




# Cria o jogador (nosso retangulo)
player = Player()

# Define o plano de fundo
x=800
y=600
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("SPACEWAR")
background = pygame.image.load ("background.jpeg")
background = pygame.transform.scale(background, (x, y))


#variavel para controlar a pontuação do jogo
pontuacao = 0
pontos = pontuacao
font = pygame.font.Font(None, 38)  # Escolha a fonte e o tamanho desejados
total_pontos_text = font.render(f"Pontuação: {pontuacao}", True, (196, 0, 255))  # Renderiza o texto da pontuação

#adicionar vida
total_lifes = 5
remaining_lifes = total_lifes
font = pygame.font.Font(None, 38)  # Escolha a fonte e o tamanho desejados
total_lifes_text = font.render(f"LIFES: {total_lifes}", True, (196, 0, 255))  # Renderiza o texto da pontuação

#Cria o grupo de inimigos
enemies = pygame.sprite.Group() 
all_sprites = pygame.sprite.Group() #Cria o grupo de todos os Sprites
all_sprites.add(player) #Adicionar o player no grupo de todos os Sprites


# Definindo a flag para controle do menu
menu_ativo = True

# Loop do menu inicial
while menu_ativo:
    menu_inicial()

    # Aguarde até que o jogador pressione uma tecla para começar o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            menu_ativo = False

# Definindo a flag para controle do game over

game_over_ativo = False
running = True #Flag para controle do jogo

last_score_update_time = pygame.time.get_ticks()
score_update_interval = 1000  # Atualizar a pontuação a cada 1000 milissegundos (1 segundo)

while running: 
     #Laco para verificacao do evento que ocorreu
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: #Verifica se a tecla ESC foi pressionada
                running = False
        elif event.type == QUIT: #Verifica se a janela foi fechada
            running = False
        elif(event.type == ADDENEMY): #Verifica se e o evento de criar um inimigo
            new_enemy = Enemy() #Cria um novo inimigo
            enemies.add(new_enemy) #Adiciona o inimigo no grupo de inimigos
            all_sprites.add(new_enemy) #Adiciona o inimigo no grupo de todos os Sprites

    rel_x = x % background.get_rect().width
    screen.blit(background, (0, 0)) #Atualiza a exibicao do plano de fundo do jogo (neste caso nao surte efeito)
    screen.blit(background, (rel_x - background.get_rect().width,0))#cria background
    if rel_x < 800:
         screen.blit(background, (rel_x, 0))
         x-=0.2
    screen.blit(total_pontos_text, (550, 10))  # Define a posição do texto na tela
    screen.blit(total_lifes_text, (10, 10))  # Define a posição do texto na tela
    pressed_keys = pygame.key.get_pressed() #Captura as as teclas pressionadas
    player.update(pressed_keys) #Atualiza a posicao do player conforme teclas usadas
    enemies.update() #Atualiza posicao dos inimigos

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect) #Atualiza a exibicao de todos os Sprites
        if pygame.sprite.spritecollideany(player, enemies): #Verifica se ocorreu a colisao do player com um dos inimigos
            remaining_lifes -= 1
            total_lifes_text = font.render(f"LIFES: {remaining_lifes}", True, (196, 0, 255))
            collided_enemies = pygame.sprite.spritecollide(player, enemies, True)
        else:
            # Verifique o tempo atual e atualize a pontuação apenas a cada intervalo de tempo
            current_time = pygame.time.get_ticks()
            if current_time - last_score_update_time >= score_update_interval:
                pontuacao += 10
                total_pontos_text = font.render(f"Pontuação: {pontuacao}", True, (196, 0, 255))
                last_score_update_time = current_time
            if remaining_lifes == 0 and not game_over_ativo:
                running = False
                game_over_ativo = True  # O jogador perdeu todas as vidas, definimos o estado de game over  
        if game_over_ativo:
            game_over()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:  # Tecla "R" para reiniciar o jogo
                    # Reinicie o jogo, redefina as vidas e outras configurações
                    remaining_lifes = total_lifes
                    game_over_ativo = False  # Defina a flag de Game Over como False para reiniciar o jogo
                    game_over_running = False  # Finalize o loop de Game Over
                    running = True
                    remaining_lifes = total_lifes
                    total_lifes_text = font.render(f"LIFES: {remaining_lifes}", True, (196, 0, 255))
                    game_over_ativo = False  # Desative o estado de Game Over para continuar o jogo
                if event.key == K_q:  # Tecla "Q" para sair do jogo
                    pygame.quit()  # Encerre o jogo corretamente

    pygame.display.flip()  # Atualize a tela
    aumentar_dificuldade() 
# Adicione uma nova flag para o loop de Game Over
game_over_ativo = True
game_over_running = True  
#Loop para controlar a tela de game over
while game_over_running:
    game_over()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over_running = False  # Finalize o loop de Game Over se o jogador fechar a janela
        if event.type == pygame.KEYDOWN:
            if event.key == K_r:  # Tecla "R" para reiniciar o jogo
                # Reinicie o jogo, redefina as vidas e outras configurações
                remaining_lifes = total_lifes
                game_over_ativo = False  # Defina a flag de Game Over como False para reiniciar o jogo
                game_over_running = False  # Finalize o loop de Game Over
                running = True
            if event.key == K_q:  # Tecla "Q" para sair do jogo
                game_over_running = False  # Finalize o loop de Game Over
    # Adicione o texto da pontuação à tela de Game Over
   








