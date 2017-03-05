from unittest import TestCase
from datetime import datetime, timedelta
import pygame
import json
from spine_examples.base import Alien, \
                                Dragon, \
                                Goblins, \
                                Hero, \
                                PowerUp, \
                                Raptor, \
                                Speedy, \
                                SpineBoy, \
                                SpineBoyOld, \
                                SpinoSaurus, \
                                skeleton_data


class MetaAssetSuite(type):

    def __new__(cls, name, bases, attrs):
        def spine_animation_test(name):
            def test(self):
                self.run_animation(name)
            return test

        def test_fail(exception):
            def test(self):
                raise exception
            return test

        if 'spine_example' in attrs:
            # raise Exception('aaa %s' % str(attrs))
            try:
                skeleton_file = '%s.json' % attrs['spine_example']
                with open(skeleton_file) as f:
                    data = json.loads(f.read())
                animations = [k for k in data['animations']]

                for a in animations:
                    attrs['test_%s' % a] = spine_animation_test(a)
            except Exception as e:
                attrs['test_fail'] = test_fail(e)

        return super(MetaAssetSuite, cls).__new__(cls, name, bases, attrs)


class AssetSuite(TestCase):

    @classmethod
    def setUpClass(cls):
        pygame.init()
        window_size=(1024, 768)

        cls.screen = pygame.display.set_mode(window_size)
        cls.caption = 'Test Assets'

        cls.spine_asset = cls.spine_asset_class()
        pygame.display.set_caption(cls.caption, 'Spine Runtime')
        cls.elapsed_time = timedelta(seconds=3)

    @classmethod
    def tearDownClass(cls):
        pygame.quit()

    def run_animation(self, animation):
        self.screen.fill((0, 0, 0))
        self.spine_asset.animation = self.spine_asset.get_skeleton_data().findAnimation(animation)
        self.spine_asset.skeleton.x = 480
        self.spine_asset.skeleton.y = 320

        clock = pygame.time.Clock()
        started = datetime.now()
        while True:
            deltaTime = clock.tick(60)
            self.spine_asset.update(deltaTime)
            self.screen.fill((0, 0, 0))
            self.spine_asset.draw(self.screen)
            pygame.display.set_caption('%s  %.2f' % (self.caption, clock.get_fps()), 'Spine Runtime')
            pygame.display.flip()
            if datetime.now() - started > self.elapsed_time:
                break


class AlienTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/alien/export/alien'
    spine_asset_class = Alien

class DragonTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/dragon/export/dragon'
    spine_asset_class = Dragon

class GoblinsTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/goblins/export/goblins'
    spine_asset_class = Goblins

class HeroTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/hero/export/hero'
    spine_asset_class = Hero

class PowerUpTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/powerup/export/powerup'
    spine_asset_class = PowerUp

class RaptorTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/raptor/export/raptor'
    spine_asset_class = Raptor

class SpeedyTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/speedy/export/speedy'
    spine_asset_class = Speedy

class SpineBoyTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/spineboy/export/spineboy'
    spine_asset_class = SpineBoy

class SpineBoyOldTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/spineboy-old/export/spineboy-old'
    spine_asset_class = SpineBoyOld

class SpinoSaurusTest(AssetSuite):
    __metaclass__ = MetaAssetSuite

    spine_example = './assets/spinosaurus/export/spinosaurus'
    spine_asset_class = SpinoSaurus
