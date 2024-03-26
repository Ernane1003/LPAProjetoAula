#!/usr/bin/python
#-*- coding: utf-8 -*-


import pygame
from pygame import Surface
from pygame.font import Font
from pygame.locals import Rect

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window: Surface = window
        self.surf = pygame.image.load('./asset/18359.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/hino-do-atletico-mineiro.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "G A L O", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "FORTE VINGADOR", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
