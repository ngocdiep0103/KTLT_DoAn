

class Score:
    def __init__(self, WIN, game_font):
        self.WIN = WIN
        self.game_font = game_font
        self.score = 0
        self.high_score = 0

    def display_score(self, game_state):#Tạo hình ảnh của điểm và các hình ảnh liên quan như chữ gameover
        if game_state == 'main game':
            score_surface = self.game_font.render(str(int(self.score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(180, 100))
            self.WIN.blit(score_surface, score_rect)
        if game_state == 'game over':
            score_surface = self.game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(180, 100))
            self.WIN.blit(score_surface, score_rect)

            high_score_surface = self.game_font.render(f'High Score: {int(self.high_score)}', True, (255, 255, 255))
            high_score_rect = score_surface.get_rect(center=(120, 525))
            self.WIN.blit(high_score_surface, high_score_rect)

    def reset_score(self):  #Reset lại điểm
        self.score = 0

    def increase_score(self):   #Thay đổi điểm
        self.score += 1

    def update_score(self): #Thay đổi high_score
        if self.score > self.high_score:
            self.high_score = self.score
        return self.high_score
