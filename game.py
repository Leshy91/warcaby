
class Game:

    def __init__(self):
        self.status = 1
        self.turn = 'O'
        self.players = ['X', 'O']
        self.hit_move = []
        self.multiple_hit_move = False
        self.game_board = [
            ['-', 'X', '-', 'X', '-', 'X', '-', 'X'],
            ['X', '-', 'X', '-', 'X', '-', 'X', '-'],
            ['-', 'X', '-', 'X', '-', 'X', '-', 'X'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['O', '-', 'O', '-', 'O', '-', 'O', '-'],
            ['-', 'O', '-', 'O', '-', 'O', '-', 'O'],
            ['O', '-', 'O', '-', 'O', '-', 'O', '-'],
            ]

    def draw_board(self, black_pawn, white_pawn, black_dame, white_dame, window,
                   field_size, margin):
        for num_r, row in enumerate(self.game_board):
            for num_i, item in enumerate(row):
                if item == 'X':
                    window.blit(black_pawn, (((num_i * field_size) + margin),
                                ((num_r * field_size) + margin)))
                elif item == 'XD':
                    window.blit(black_dame, (((num_i * field_size) + margin),
                                ((num_r * field_size) + margin)))
                elif item == 'O':
                    window.blit(white_pawn, ((num_i * field_size) + margin,
                                (num_r * field_size) + margin))
                elif item == 'OD':
                    window.blit(white_dame, ((num_i * field_size) + margin,
                                (num_r * field_size) + margin))

    def check_pawn_move_possibility(self, from_to_list):
        return self.game_board[from_to_list[2]][from_to_list[3]] == '-' and \
               self.game_board[from_to_list[0]][from_to_list[1]] == self.turn and \
               self.validate_pawn_move(from_to_list)

    def check_dame_move_possibility(self, from_to_list):
        return self.game_board[from_to_list[2]][from_to_list[3]] == '-' and \
               self.game_board[from_to_list[0]][from_to_list[1]] == f"{self.turn}D" and \
               self.validate_dame_move(from_to_list)

    def validate_pawn_move(self, from_to_list):
        x = 1 if from_to_list[2] == from_to_list[0] + 2 else -1 if from_to_list[2] == from_to_list[0] - 2 else 0
        y = 1 if from_to_list[3] == from_to_list[1] + 2 else -1 if from_to_list[3] == from_to_list[1] - 2 else 0
        if x and y:
            if self.turn == 'X':
                if self.game_board[from_to_list[0] + x][from_to_list[1] + y] == 'O' or \
                        self.game_board[from_to_list[0] + x][from_to_list[1] + y] == 'OD':
                    self.hit_move = [from_to_list[0] + x, from_to_list[1] + y]
                    return True
            elif self.turn == 'O':
                if self.game_board[from_to_list[0] + x][from_to_list[1] + y] == 'X' or \
                             self.game_board[from_to_list[0] + x][from_to_list[1] + y] == 'XD':
                    self.hit_move = [from_to_list[0] + x, from_to_list[1] + y]
                    return True
        elif self.turn == 'X' and from_to_list[2] == from_to_list[0] + 1:
            return from_to_list[3] == from_to_list[1] + 1 or from_to_list[3] == from_to_list[1] - 1
        elif self.turn == 'O' and from_to_list[2] == from_to_list[0] - 1:
            return from_to_list[3] == from_to_list[1] + 1 or from_to_list[3] == from_to_list[1] - 1

    def validate_dame_move(self, from_to_list):
        if abs(from_to_list[3] - from_to_list[1]) == abs(from_to_list[2] - from_to_list[0]):
            x = -1 if (from_to_list[2] - from_to_list[0]) > 0 else 1
            y = -1 if (from_to_list[3] - from_to_list[1]) > 0 else 1
            help_list = []
            for i in range(1, abs(from_to_list[2] - from_to_list[0])):
                if self.game_board[from_to_list[2] + (i * x)][from_to_list[3] + (i * y)] == '-':
                    help_list.append('-')
                # elif i == abs(from_to_list[2] - from_to_list[0]) - 1 and \
                #     self.game_board[from_to_list[2] + (i * x)][from_to_list[3] + (i * y)] == '-'
                else:
                    break
            if len(help_list) == abs(from_to_list[2] - from_to_list[0]) - 1:
                return True
        return False

    def translate_px_to_index(self, px):
        if len(str(px)) == 1 or len(str(px)) == 2:
            return 0
        elif len(str(px)) == 3:
            return int(str(px)[0])

    def make_move(self, from_to_list, window, background, black_pawn, white_pawn, black_dame, white_dame,
                  field_size, margin):
        if len(self.hit_move):
            self.game_board[from_to_list[2]][from_to_list[3]] = self.turn
            self.game_board[from_to_list[0]][from_to_list[1]] = '-'
            self.game_board[self.hit_move[0]][self.hit_move[1]]\
                = '-'
            self.hit_move = []
        else:
            if self.game_board[from_to_list[0]][from_to_list[1]] == f"{self.turn}D":
                self.game_board[from_to_list[2]][from_to_list[3]] = f"{self.turn}D"
                self.game_board[from_to_list[0]][from_to_list[1]] = '-'
            else:
                self.game_board[from_to_list[2]][from_to_list[3]] = self.turn
                self.game_board[from_to_list[0]][from_to_list[1]] = '-'

        self.turn_change()
        self.check_for_dame()
        window.blit(background, (0, 0))
        self.draw_board(black_pawn, white_pawn, black_dame, white_dame, window, field_size, margin)

    def turn_change(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
        # if self.turn == 'X':
        #     self.turn = 'O'
        # else:
        #     self.turn = 'X'

    def check_for_dame(self):
        for i in range(8):
            if self.game_board[0][i] == 'O':
                self.game_board[0][i] = 'OD'
            if self.game_board[7][i] == 'X':
                self.game_board[7][i] = 'XD'

    def check_for_pawn_multiple_hit(self, from_to):
        pass

    # def scan_for_capture_obligation(self):
    #     for i in range(len(self.game_board)):
    #         for j in range(len(self.game_board)):
    #             if self.game_board[i][j] == 'X':
    #                 if self.game_board[]:
    #                     pass
