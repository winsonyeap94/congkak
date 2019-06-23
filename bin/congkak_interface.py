import pygame
import numpy as np
from aspect_scale import aspect_scale

# Initialising pygame
pygame.init()

# Loading resources
wood_texture = pygame.image.load("../res/wood-texture.png")
marble_img = pygame.image.load("../res/marble.png")
board_hole_colour = (223, 194, 125)

# Display-related defaults
tile_width = 90
tile_height = 150
center_board_position = [225, 100]
overlay_font = pygame.font.Font(pygame.font.match_font('arialblack'), 32)
marble_count_font = pygame.font.Font(pygame.font.match_font('stencil'), 24)

# Player-related defaults
player1_score = 0
player2_score = 0
player1_house_marbles = [7, 7, 7, 7, 7, 7, 7]
player2_house_marbles = [7, 7, 7, 7, 7, 7, 7]

# Defining main game window for Congkak
game_window = pygame.display.set_mode((1000, 600))
game_window.fill((255, 255, 255))

congkak_title = overlay_font.render("Congkak Simulator", True, (0, 175, 169))
congkak_title_rect = congkak_title.get_rect()
congkak_title_rect.center = (500, 50)
game_window.blit(congkak_title, congkak_title_rect)

pygame.display.set_caption("Congkak")


def draw_congkak_board(player1_score, player2_score, player1_house_marbles, player2_house_marbles):
    global game_window

    # Drawing the middle part of the congkak board
    x = np.tile(np.arange(center_board_position[0], center_board_position[0] + tile_width * 7, tile_width), 2).tolist()
    y = np.append(np.repeat(center_board_position[1], 7), np.repeat(center_board_position[1] + tile_height, 7)).tolist()
    scaled_wood_texture = pygame.transform.scale(wood_texture, (tile_width, tile_height))
    scaled_marble = aspect_scale(marble_img, tile_width - 30, tile_height - 20)

    for idx, (x_pos, y_pos) in enumerate(zip(x, y)):
        # Layering wood texture
        rect = scaled_wood_texture.get_rect()
        rect = rect.move((x_pos, y_pos))
        game_window.blit(scaled_wood_texture, rect)
        pygame.draw.rect(game_window, board_hole_colour, (x_pos + 10, y_pos + 10, tile_width - 20, tile_height - 20))
        # Adding holes
        rect = scaled_marble.get_rect()
        rect = rect.move((x_pos + 15, y_pos + 10))
        game_window.blit(scaled_marble, rect)
        # Adding display text for marble count
        if idx > 6:
            house_marbles = player2_house_marbles
            idx = idx - 7
        else:
            house_marbles = player1_house_marbles
        marble_text = marble_count_font.render(str(house_marbles[idx]), False, (0, 0, 0))
        marble_text_rect = marble_text.get_rect()
        marble_text_rect.center = (x_pos + tile_width/2, y_pos + 100)
        game_window.blit(marble_text, marble_text_rect)

    # Drawing the sides (houses) of the congkak board
    house_x = [x[0] - tile_width * 2, x[len(x)-1]]
    house_y = [center_board_position[1], center_board_position[1]]

    scaled_wood_texture = pygame.transform.scale(wood_texture, (tile_width * 2, tile_height * 2))
    for idx, (x_pos, y_pos) in enumerate(zip(house_x, house_y)):
        # Layering wood texture
        rect = scaled_wood_texture.get_rect()
        rect = rect.move((x_pos, y_pos))
        game_window.blit(scaled_wood_texture, rect)
        pygame.draw.rect(game_window, board_hole_colour, (x_pos + 10, y_pos + 10, tile_width * 2 - 20,
                                                          tile_height * 2 - 20))
        # Adding holes
        rect = scaled_marble.get_rect()
        rect = rect.move((x_pos + 65, y_pos + 30))
        game_window.blit(scaled_marble, rect)
        # Adding display text for marble count
        if idx == 0:
            score_marbles = player1_score
        else:
            score_marbles = player2_score
        marble_text = marble_count_font.render(str(score_marbles), False, (0, 0, 0))
        marble_text_rect = marble_text.get_rect()
        marble_text_rect.center = (x_pos + tile_width, y_pos + 200)
        game_window.blit(marble_text, marble_text_rect)

    pygame.display.update()


draw_congkak_board(player1_score, player2_score, player1_house_marbles, player2_house_marbles)
game_run_flag = True

while game_run_flag:

    # Default quitting sequence: Close box if click on 'X' button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run_flag = False

    # Redraw congkak_board after every action
    draw_congkak_board(player1_score, player2_score, player1_house_marbles, player2_house_marbles)

# Exit
pygame.quit()

