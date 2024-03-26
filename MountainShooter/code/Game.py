#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pygame

from code.Const import WIN_WIDTH, WIN_HEIGTH
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH))

    def run(self) -> object:
        while True:
            menu = Menu(self.window)
            menu.run()
