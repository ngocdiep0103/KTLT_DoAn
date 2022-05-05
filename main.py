import sys, pygame
from pipe import Pipe, PipeManager
from floor import Floor
from sound import Sound
from score import Score
from mon import Mon

# hàm trò chơi
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
idx = 0
# đặt size cho cửa sổ
WIN = pygame.display.set_mode((360, 640))

# set up background
bg = pygame.image.load('image/background.png').convert()
bg = pygame.transform.scale2x(bg)

# đặt tên cửa sổ
pygame.display.set_caption("FLAPPY MON")

# xác định số frame mỗi giây
FPS = 60  # tốc dộ bình thường của game
clock = pygame.time.Clock()
# thêm ống
PIPE_SURFACE = pygame.image.load('image/column.png').convert()
PIPE_HEIGHT = [i for i in range(300, 500)]
# thêm font chữ
game_font = pygame.font.Font('Audiowide-Regular (1).ttf', 40)
# biến
game_active = True
# điểm
score = Score(WIN=WIN, game_font=game_font)
# tạo màn hình kết thúc
game_over_surface = pygame.image.load('image/opening .png').convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(180, 320))
# tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)  # sau 1.2s tạo ra ống mới

if game_active:
        WIN.blit(bg, (0, 0))  # thêm background
        doramon.move()
        WIN.blit(doramon.rotated_mon, doramon.mon_rect)  # thêm mon vào
        # ống
        pipe_manager.pipe_movement()
        pipe_manager.draw_pipe()
        game_active = check_collision(pipe_manager.get_pipe_list())
        # điểm
        score.display_score('main game')

    else:
        # màn hình game over
        WIN.blit(game_over_surface, game_over_rect)
        # điểm
        score.update_score()
        score.display_score('game over')

    #  thêm floor chuyển động
    floor.move_floor()
    floor.draw_floor()
    floor.check_and_reset_floor()

    pygame.display.update()
    clock.tick(FPS)  # để kiểm soát tốc độ của chương trình
