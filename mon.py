import pygame
GRAVITY = 0.25  # trọng lượng


class Mon:
    def __init__(self):
        self.mon_big = pygame.image.load('image/doradora.png').convert_alpha()
        self.mon_width = 75
        self.mon_height = 95
        self.mon = pygame.transform.scale(self.mon_big, (self.mon_width, self.mon_height))
        self.rotated_mon = self.mon
        self.mon_rect = self.mon.get_rect(center=(100, 320))  # vẽ khung theo mon
        self.mon_movement = 0

    def set_mon_movement(self, value):
        self.mon_movement = value

    def move(self):
        self.mon_movement += GRAVITY
        self.rotate_mon()
        self.mon_rect.centery += self.mon_movement

    def rotate_mon(self):
        self.rotated_mon = pygame.transform.rotozoom(self.mon, -int(self.mon_movement) * 2, 1)  # tạo hiệu ứng xoay
