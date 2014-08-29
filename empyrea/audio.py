####################################
# I.A Music/Sound Functions        #
####################################

import pygame

class Audio:
    def __init__(self, mvolume, svolume):
        self.__class__.MVolume = ((mvolume * 1.0) / 100)
        self.__class__.SVolume = ((svolume * 1.0) / 100)

        pygame.mixer.init()
        pygame.mixer.set_num_channels(32)


    def setMVolume(self, volume):
        self.MVolume = int(volume)
        pygame.mixer.music.set_volume(self.MVolume)


    def setSVolume(self, volume):
        self.SVolume = int(volume)
        pygame.mixer.music.set_volume(self.SVolume)


    def playMusic(self, fname, loops=0, start=0.0):
        pygame.mixer.music.load(fname)
        pygame.mixer.music.play(loops,start)
        pygame.mixer.music.set_volume(self.MVolume)


    def fadeoutMusic(self, delay):
        pygame.mixer.music.fadeout(delay)


    def playSound(self, fname, fadeout=0, volume=1.0):
        sound = pygame.mixer.Sound(fname)
        sound.play()
        if fadeout:
            sound.fadeout(fadeout)
            sound.set_volume(min(self.SVolume, volume))

        return sound
