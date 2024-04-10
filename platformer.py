import pygame

# const
running = True
SCREEN_RESOLUTION = (700, 500)

# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION);
pygame.display.set_caption("Sam's Adventure!")

# player
player_image = pygame.image.load("sprites/DEFAULT_SPRITE/DEFAULT_SPRITE00.png")
player_x = 300
player_y = 200
player_h = player_image.get_height()
player_w = player_image.get_width()
player_velocity_y = 0
player_accelleration = 0.075

# platform
platforms = [
    pygame.Rect(100,300,400,50), #mid
    pygame.Rect(100,250,50,50), #left
    pygame.Rect(450,250,50,50) #right
]

# game loop
while running == True:

    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #horiz input

    temp_player_x = player_x
    temp_player_y = player_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        temp_player_x -= 1
    if keys[pygame.K_RIGHT]:
        temp_player_x += 1
    if keys[pygame.K_UP]:
        player_y_velocity = -3

    #horiz mvt checks

    player_hitbox_x = pygame.Rect(temp_player_x, temp_player_y, player_h, player_w)
    x_collision = False

    #check against platforms
    for p in platforms:
        if p.colliderect(player_hitbox_x):
            x_collision = True
            break
    #if so set x_collision = true
    if x_collision == False:
        player_x = temp_player_x

    #vert input
        
    player_velocity_y += player_accelleration
    temp_player_y += player_velocity_y

    y_collision = False
    player_hitbox_y = pygame.Rect(temp_player_x, temp_player_y, player_h, player_w)

    #check against platforms
    for p in platforms:
        if p.colliderect(player_hitbox_y):
            y_collision = True
            player_velocity_y = 0
            break
    #if so set x_collision = true
    if y_collision == False:
        player_y = temp_player_y

    # update

    # draw
    
    # background
    screen.fill( (50, 50, 50) )

    # player
    screen.blit(player_image, (player_x, player_y))

    # platform
    for p in platforms:
        pygame.draw.rect(screen, (225,0,0), p)

    # present screen
    pygame.display.flip()

# quit
pygame.quit()



