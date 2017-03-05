#!/usr/bin/env python

import os
import pygame
import pyguts as spine
import pygameui as ui

UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

def skeleton_data(atlas_file, skeleton_file):
    atlas = spine.Atlas(file=atlas_file)
    skeletonJson = spine.SkeletonJson(spine.AtlasAttachmentLoader(atlas))
    return skeletonJson.readSkeletonDataFile(skeleton_file)

class Actor(object):
    __skeleton_data = None
    initialized = False

    @classmethod
    def get_skeleton_data(cls):
        if not cls.__skeleton_data:
            atlas_file = '%s.atlas' % cls.animation_data
            skeleton_file = '%s.json' % cls.animation_data
            cls.__skeleton_data = skeleton_data(atlas_file, skeleton_file)
        return cls.__skeleton_data


    def __init__(self):
        self.skeleton = spine.Skeleton(skeletonData=self.get_skeleton_data())
        self.skeleton.debug = False
        self.skeleton.setToBindPose()
        self.animationTime = 0
        self.facing = RIGHT
        self.skeleton.x = 0
        self.skeleton.y = 0
        self.skeleton.flipX = False
        self.skeleton.flipY = False

    def lazy_init(self):
        pass

    def update(self, deltaTime):
        self.skeleton.flipX = self.facing != RIGHT

        self.animationTime += deltaTime / 1000.0
        self.animation.apply(skeleton=self.skeleton,
                              time=self.animationTime,
                              loop=True)
        self.skeleton.updateWorldTransform()


    def draw(self, screen):
        self.skeleton.draw(screen, 0)

class Alien(Actor):
    animation_data = './assets/alien/export/alien'

class Dragon(Actor):
    animation_data = './assets/dragon/export/dragon'

class Goblins(Actor):
    animation_data = './assets/goblins/export/goblins'

class Hero(Actor):
    animation_data = './assets/hero/export/hero'

class PowerUp(Actor):
    animation_data = './assets/powerup/export/powerup'

class Raptor(Actor):
    animation_data = './assets/raptor/export/raptor'

class Speedy(Actor):
    animation_data = './assets/speedy/export/speedy'

class SpineBoy(Actor):
    animation_data = './assets/spineboy/export/spineboy'

class SpineBoyOld(Actor):
    animation_data = './assets/spineboy-old/export/spineboy-old'

class SpinoSaurus(Actor):
    animation_data = './assets/spinosaurus/export/spinosaurus'
