
import pygame
from pygame.locals import *
from constants import *
from data import GameData
from window import Window
from button import Button
from high_scores_helpers import HighScores

class HighScoresWindow(Window):
    def __init__(self, size, caption=None, win=None):
        Window.__init__(self, size, caption, win)
        self.background = GameData.image(HIGH_SCORES_BGD_IMG)

        button_image = GameData.image(BUTTON_IMG)
        self.main_menu_button = Button(HS_RETURN_BTN_POS, button_image, self.buttons)
        self.local_button = Button(HS_LOCAL_BTN_POS, button_image)
        self.global_button = Button(HS_GLOBAL_BTN_POS, button_image, self.buttons)

        self.tab_container = pygame.sprite.LayeredDirty()
        self.tab = None

        self.local_entry_container = pygame.sprite.LayeredDirty()

    """ Expects an optional new score as first paramater of args """
    def setup(self, args=()):
        new_local_rank = 0
        if len(args) > 0:
            level = args[0]
            points = args[1]
            #name = self.name_getter.run()
            #new_local_rank, new_global_rank = HighScores.newScore(name, level, points)
            
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
        
        self.tab_container.empty()
        self.tab = Tab(self.tab_container)
        # TODO: deal with newest score and global entries
        positions = HS_ENTRY_POSITIONS
        if new_local_rank > positions:
            positions -= 1
        scores = HighScores.localTop(positions)

        self.local_entry_container.empty()
        num = 1
        for score in scores:
            color = DEFAULT_FONT_COLOR
            if new_local_rank == num:
                color = SELECTION_FONT_COLOR
            Entry(num, score, self.local_entry_container, color)
            num += 1
        # For when the new score is below the top 11 we add it manually
        if new_local_rank > HS_ENTRY_POSITIONS:
            Entry(new_rank, new_score, self.local_entry_container, SELECTION_FONT_COLOR)

        self.setScopeLocal()

    def handleEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                selection = self.selectedButton()
                if selection == self.main_menu_button:
                    self.running = False
                elif selection == self.local_button:
                    self.setScopeLocal()
                elif selection == self.global_button:
                    self.setScopeGlobal()

    def clear(self):
        self.tab_container.clear(self.screen, self.background)
        self.local_entry_container.clear(self.screen, self.background)

    def draw(self):
        dirty = self.tab_container.draw(self.screen)
        dirty += self.local_entry_container.draw(self.screen)
        return dirty

    def setScopeLocal(self):
        self.tab.setScopeLocal()
        self.buttons.add(self.global_button)
        self.buttons.remove(self.local_button)
        for entry in self.local_entry_container:
            entry.visible = 1
            entry.dirty = 1

    def setScopeGlobal(self):
        self.tab.setScopeGlobal()
        self.buttons.add(self.local_button)
        self.buttons.remove(self.global_button)
        for entry in self.local_entry_container:
            entry.visible = 0
            entry.dirty = 1

class Tab(pygame.sprite.DirtySprite):
    LOCAL = 'local'
    GLOBAL = 'global'
    def __init__(self, container):
        pygame.sprite.DirtySprite.__init__(self, container)
        self.image = pygame.Surface(HS_TAB_SIZE)
        self.image.fill(BGD_COLOR)
        self.rect = pygame.Rect(HS_TAB_LOCAL_POS, HS_TAB_SIZE)
        self.visible = 1
        self.state = None
        self.setScopeLocal()

    def setScopeLocal(self):
        if self.state != self.LOCAL:
            self.state = self.LOCAL
            self.rect.topleft = HS_TAB_LOCAL_POS
            self.dirty = 1

    def setScopeGlobal(self):
        if self.state != self.GLOBAL:
            self.state = self.GLOBAL
            self.rect.topleft = HS_TAB_GLOBAL_POS
            self.dirty = 1

class Entry(pygame.sprite.DirtySprite):
    FONT = None
    def __init__(self, num, score, container, color=DEFAULT_FONT_COLOR):
        pygame.sprite.DirtySprite.__init__(self, container)
        if not self.FONT: # have to do this here so pygame.font is initialized
            self.FONT = pygame.font.SysFont(FONT, HS_ENTRY_FONT_SIZE)
        pos = getEntryPos(num)
        self.rect = pygame.Rect(pos, HS_ENTRY_SIZE)
        self.visible = 1
        self.num = num
        self.score = score
        self.color = color
        self.updateImage()

    def get_text(self, score):
        return "%-*d %-*s Level: %*d %*d" % (
            HS_ENTRY_NUM_LENGTH, self.num,
            HS_ENTRY_MAX_NAME_LENGTH, score.name,
            HS_ENTRY_LEVEL_LENGTH, score.level,
            HS_ENTRY_POINTS_LENGTH, score.points)

    def updateImage(self):
        text = self.get_text(self.score)
        self.image = self.FONT.render(text, True, self.color)
        self.dirty = 1

    def setName(self, new_name):
        HighScores.updateName(new_name, self.score)
        self.score.name = new_name
        self.updateImage()

def getEntryPos(num):
    x = HS_ENTRY_TOP[0] + HS_ENTRY_OFFSET[0]
    if num > HS_ENTRY_POSITIONS: num = HS_ENTRY_POSITIONS
    y = (num - 1) * (HS_ENTRY_SIZE[1] + HS_ENTRY_GAP) + HS_ENTRY_TOP[1] + HS_ENTRY_OFFSET[1]
    return (x, y)

if __name__ == '__main__':
    pygame.init()
    
    main = HighScoresWindow((SCREEN_WIDTH, SCREEN_HEIGHT), 'OmniTank High Scores - Standalone')
    main.run()

    pygame.quit()
