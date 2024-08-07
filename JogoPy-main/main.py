from config import *
from nivel import Nivel
import pygame
from sys import exit
from os.path import join
from pytmx.util_pygame import load_pygame
from random import choice
import math


class Game:
    def __init__(self):
        pygame.init()

        self.largura_upscale = largura * escala
        self.altura_upscale = altura * escala

        # Criação da janela de jogo
        self.surface = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption(titulo)  # Título do jogo
        self.clock = pygame.time.Clock()

        # Carregar mapas

        self.num_nivel = 0
      #  self.random_mapa = choice((0, 1))
        self.tmx_maps = {
            0: load_pygame(join("TiledLava.tmx")),
            1: load_pygame(join(("C:\\Users\\User\\Desktop\\TiledForest.tmx"))),
            2: load_pygame(join(("C:\\Users\\User\\Desktop\\TiledSnow.tmx")))

        }
        self.current_stage = Nivel(self.tmx_maps[self.num_nivel], self.switch_stage, self.num_nivel)


    def switch_stage(self, num_nivel):
      #  print(num_nivel)
        self.current_stage = Nivel(self.tmx_maps[num_nivel], self.switch_stage, self.num_nivel)


    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Executar lógica do nível
            self.current_stage.run(dt, self.num_nivel)
           # print(self.num_nivel)

            # Ampliar a superfície do jogo
            scaled_surface = pygame.transform.scale(self.surface, (self.largura_upscale, self.altura_upscale))

            # Desenhar a superfície ampliada na tela
            self.surface.blit(scaled_surface, ((-largura*1.5, -altura*1.5))) # escala 2: (-(largura/2), -(altura/2)) | escala 3: (-largura, -altura) | escala 4: (-largura*1.5, -altura*1.5)

            # Atualizar a tela
            pygame.display.update()


if __name__ == '__main__':
    jogo = Game()
    jogo.run()
