#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from abc import ABC, abstractmethod


class Entity(ABC):

    def __init__(self, name:str, positon: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets' + name + '.png')
        self.rect = self.surf.get_rect(left=positon[0], top=positon[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
