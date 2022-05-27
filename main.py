import pygame
import game

BOARD_SIZE = 800
FIELD_SIZE = BOARD_SIZE / 8
PAWN_SIZE = 85
PAWN_MARGIN = (FIELD_SIZE - PAWN_SIZE) / 2

pygame.init()
game = game.Game()
window = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
window.fill((150, 150, 150))
pygame.display.set_caption("Warcaby")
font = pygame.font.SysFont('timesnewroman', 15)
background = pygame.image.load('images/gameboard.png')
window.blit(background, (0, 0))

black_pawn = pygame.image.load('images/black_pawn.png')
white_pawn = pygame.image.load('images/white_pawn.png')
black_dame = pygame.image.load('images/black_dame.png')
white_dame = pygame.image.load('images/white_dame.png')

game.draw_board(black_pawn, white_pawn, black_dame, white_dame, window, FIELD_SIZE, PAWN_MARGIN)
pygame.display.update()


from_to = []
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            from_to.append(game.translate_px_to_index(mouse_y))
            from_to.append(game.translate_px_to_index(mouse_x))
            if len(from_to) == 4:
                if game.check_pawn_move_possibility(from_to) or game.check_dame_move_possibility(from_to):
                    game.make_move(from_to, window, background, black_pawn, white_pawn, black_dame, white_dame,
                                   FIELD_SIZE, PAWN_MARGIN)
                    pygame.display.update()
                from_to.clear()

    pygame.display.update()
    clock.tick(60)
