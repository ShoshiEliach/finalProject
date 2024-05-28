

import datetime
import pygame


class trraficLight:
    def __init__(self,id,color,x,y):
        self.id=id
        self.color=color
        self.start_time=datetime.datetime.now().time()
        self.x=x
        self.y=y
        self.colors=[(255, 0, 0), (0, 255, 0)]


class trraficWithPyg(pygame.Surface, trraficLight):
        def __init__(self,id, width, height, color, x, y):
            pygame.Surface.__init__(self, (width, height))
            trraficLight.__init__(self, id, color, x, y)


        def trrafic_is_red(self):
            if self.color==self.colors[0]:
                return True
        def on_trrafic(self):
            self.color=self.colors[1]
            self.fill(self.color)
            self.start_on=datetime.datetime.now()
        def off_trrafic(self):
            self.color=self.colors[0]
            self.fill(self)
            return True
