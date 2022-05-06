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

def check_collision(pipes):  # check va chạm
    for pipee in pipes:
        if doramon.mon_rect.colliderect(pipee):
            sound.hit_sound.play()
            return False
    if doramon.mon_rect.top <= -100 or doramon.mon_rect.bottom >= 550:  # kiểm soát mon không bay ra ngoài cửa sổ
        sound.hit_sound.play()
        return False
    return True

while True:  # tạo loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                # jump
                doramon.set_mon_movement(-5)
                sound.flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_manager.clear_pipe_list()
                doramon.mon_rect.center = (100, 320)
                doramon.set_mon_movement(0)
                score.reset_score()
                pipe_manager.idx = 0
        if event.type == spawnpipe:
            pipe_pos = pipe.create_pipe()
            pipe_manager.add_pipe(pipe_pos) 
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
