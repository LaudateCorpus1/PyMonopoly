# -*- coding: utf-8 -*-
import Globals, pygame
from MenuItems import Cursor, MenuItem
from sys import exit as SYSEXIT

class MainScreen():
    def __init__(self, type):
        if type == 'main_main':
            self.menuitems = {'new_game'    : MenuItem(Globals.TRANSLATION[0], 'main_new_game', 'main_main', 0),
                              'settings'    : MenuItem(Globals.TRANSLATION[1], 'main_settings', 'main_main', 1),
                              'stats'       : MenuItem(Globals.TRANSLATION[2], 'main_stats', 'main_main', 2),
                              'exit'        : MenuItem(Globals.TRANSLATION[3], 'main_sysexit', 'main_main', 3)}
            self.pics = {'background'       : Globals.PICS['background']}
        self.cursor = Cursor(self.menuitems, type)
    def mainloop(self):
        while True:
            key = self.check_mouse_pos(pygame.mouse.get_pos())
            self.render(key)
            self.events(key)
    def check_mouse_pos(self, mp):
        key = self.find_hovering_menuitem(mp)
        if key != self.cursor.active_key and key in self.cursor.keys:
            self.cursor.change_pos(key)
        return key
    def find_hovering_menuitem(self, mp):
        for key in self.menuitems.keys():
            if self.menuitems[key].active_zone.collidepoint(mp):
                return key
        return None
    def render(self, highlighted_menuitem):
        for pic in self.pics.values():
            pic.render()
        if self.cursor:
            self.cursor.render()
        for item in self.menuitems.values():
            item.render(highlighted_menuitem)
        Globals.window.blit(Globals.screen, (0, 0))
        pygame.display.flip()
    def events(self, key):
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1 and key:
                self.action_call()
            elif e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_UP, pygame.K_DOWN):
                    if self.cursor:
                        self.cursor.keypress(e.key)
                elif e.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    self.action_call()
                elif e.key == pygame.K_ESCAPE:
                    self.menuitems['exit'].action()
            elif e.type == pygame.QUIT:
                SYSEXIT()
    def action_call(self):
        type = self.menuitems[self.cursor.active_key].action()
        if type:
            print(type)
