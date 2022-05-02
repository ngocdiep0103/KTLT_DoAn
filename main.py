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
