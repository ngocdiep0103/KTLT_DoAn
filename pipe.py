import pygame, random


class Pipe:
    def __init__(self, PIPE_SURFACE, PIPE_HEIGHT):
        self.PIPE_SURFACE = PIPE_SURFACE
        self.PIPE_HEIGHT = PIPE_HEIGHT

    def create_pipe(self):
        random_pipe_pos = random.choice(self.PIPE_HEIGHT)
        bottom_pipe = self.PIPE_SURFACE.get_rect(midtop=(400, random_pipe_pos))
        top_pipe = self.PIPE_SURFACE.get_rect(midtop=(400, random_pipe_pos - 580))
        return bottom_pipe, top_pipe


class PipeManager:
    def __init__(self, WIN, score, sound, idx, game_active, PIPE_SURFACE, PIPE_HEIGHT):
        self.pipe_list = []
        self.WIN = WIN
        self.score = score
        self.sound = sound
        self.idx = idx
        self.game_active = game_active
        self.PIPE_SURFACE = PIPE_SURFACE
        self.PIPE_HEIGHT = PIPE_HEIGHT

    def draw_pipe(self):
        for pipe in self.pipe_list:
            self.WIN.blit(self.PIPE_SURFACE, pipe)

    def add_pipe(self, pipe):
        self.pipe_list.extend(pipe)

    def clear_pipe_list(self):
        self.pipe_list.clear()

    def get_pipe_list(self):
        return self.pipe_list

    def pipe_movement(self):
        for pipe in self.pipe_list:
            pipe.centerx -= 3
        if len(self.pipe_list) != 0:
            if (self.pipe_list[self.idx].centerx + 48) == 100 and self.game_active:
                self.score.increase_score()
                self.sound.score_sound.play()
                self.idx += 2
        # update pipe_list