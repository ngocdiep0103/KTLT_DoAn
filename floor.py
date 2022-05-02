import pygame

class Floor:
    def __init__(self, WIN):
        # thêm ảnh floor
        self.floor = pygame.image.load('image/floor.png').convert()
        self.floor = pygame.transform.scale2x(self.floor)
        self.floor_x_pos = 0
        self.WIN = WIN

    def draw_floor(self):
        self.WIN.blit(self.floor, (self.floor_x_pos, 600))
        self.WIN.blit(self.floor, (self.floor_x_pos + 360, 600))

    def move_floor(self):
        self.floor_x_pos -= 1

    def check_and_reset_floor(self):
        if self.floor_x_pos <= -360:
            self.floor_x_pos = 0