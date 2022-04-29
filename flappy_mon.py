def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(180, 100))
        WIN.blit(score_surface, score_rect)
    if game_state == 'game over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(180, 100))
        WIN.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = score_surface.get_rect(center=(120, 525))
        WIN.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

# điểm
score = 0
high_score = 0
while True:  # tạo loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                mon_movement = -5
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                mon_rect.center = (100, 320)
                mon_movement = 0
                score = 0
                idx=0
        if event.type == spawnpipe:
            pipe = create_pipe()
            pipe_list.extend(pipe)




    if game_active:
        WIN.blit(background, (0, 0))  # thêm background
        mon_movement += gravity
        rotated_mon = rotate_mon(mon)
        mon_rect.centery += mon_movement
        WIN.blit(rotated_mon, mon_rect)  # thêm mon vào
        # ống
        pipe_list = pipe_movement(pipe_list)
        draw_pipe(pipe_list)
        game_active = check_collision(pipe_list)
        # điểm

        score_display('main game')

    else:
        # màn hình game over
        WIN.blit(game_over_surface, game_over_rect)
        # điểm
        high_score = update_score(score, high_score)
        score_display('game over')

    #  thêm floor chuyển động
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -360:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(FPS)  # để kiểm soát tốc độ của chương trình

