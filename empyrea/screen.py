import libtcodpy as libtcod
import os

class Screen:
    def __init__(self, width, height, fullscreen, font, font_type, limit_fps = 30):
        self.width = width
        self.height = height
        self.view_width = width - 22
        self.view_height = height - 16
        self.limit_fps = limit_fps
        self.fullscreen = fullscreen

        os.putenv("SDL_VIDEO_CENTERED", "1")

        # Create and partially configure the various consoles
        self.GraphicsLayer = libtcod.console_new(width,height)
        self.wiwindow = libtcod.console_new(self.view_width, height - self.view_height - 3)
        self.wswindow = libtcod.console_new(width - self.view_width - 3,height - 2)
        self.toplayer = libtcod.console_new(self.view_width,self.view_height)

        self.LoadScreen = libtcod.console_new(self.view_width,self.view_height)
        libtcod.console_set_key_color(self.LoadScreen,libtcod.magenta)

        self.GUILayer = libtcod.console_new(32,9)

        self.GUIBlurb = libtcod.console_new(24,6)
        libtcod.console_set_key_color(self.GUIBlurb,libtcod.magenta)
        libtcod.console_set_default_background(self.GUIBlurb,libtcod.magenta)
        libtcod.console_clear(self.GUIBlurb)

        self.TimeLayer = libtcod.console_new(16,5)
        self.PauseLayer = libtcod.console_new(5,5)

        # Initialize fonts
        fontimage = libtcod.image_load('fonts/' + font)
        self.fontx = 32
        self.fonty = 2055

        if font_type == 'GREYSCALE':
            libtcod.console_set_custom_font('fonts/' + font,
                        libtcod.FONT_LAYOUT_TCOD | libtcod.FONT_TYPE_GREYSCALE,
                        self.fontx, self.fonty)
        else:
            libtcod.console_set_custom_font('fonts/' + font,
                        libtcod.FONT_LAYOUT_TCOD, self.fontx, self.fonty)

        self.finfomod = libtcod.image_get_size(fontimage)
        self.finfomod = self.finfomod[0] / 32
        self.fontinfo = libtcod.image_load('fonts/fontinfo%s.png' % self.finfomod)

        # Window configuration
        libtcod.mouse_show_cursor(True)
        libtcod.console_init_root(width, height,'Empyrea', fullscreen)
        libtcod.sys_set_fps(self.limit_fps)


        ## NOTE TO SELF - Blit2x reserves characters 226-232 ##
        libtcod.console_map_ascii_code_to_font(157,4,5) # Deciduous
        libtcod.console_map_ascii_code_to_font(156,1,5) # Shrubland
        libtcod.console_map_ascii_code_to_font(154,2,5) # Cacti
        libtcod.console_map_ascii_code_to_font(153,3,5) # Heathland
        libtcod.console_map_ascii_code_to_font(151,0,5) # Broadleaf
        libtcod.console_map_ascii_code_to_font(150,5,5) # Mixed Forest
        libtcod.console_map_ascii_code_to_font(149,13,5) # Coniferous
        libtcod.console_map_ascii_code_to_font(148,6,5) # Evergreen
        libtcod.console_map_ascii_code_to_font(147,7,5) # Caves
        libtcod.console_map_ascii_code_to_font(146,8,5) # Tropical Forest

        libtcod.console_map_ascii_code_to_font(145,9,5) # Human
        libtcod.console_map_ascii_code_to_font(144,10,5) # Castle
        libtcod.console_map_ascii_code_to_font(143,11,5) # Village
        libtcod.console_map_ascii_code_to_font(142,12,5) # City

        libtcod.console_map_ascii_code_to_font(159,16,2) # 4-way wall.

        # Skip chr. 160 - return key?
        libtcod.console_map_ascii_code_to_font(161,19,6) # Conifer 1
        libtcod.console_map_ascii_code_to_font(162,19,7) # Conifer 2
        libtcod.console_map_ascii_code_to_font(163,20,6) # Conifer 3
        libtcod.console_map_ascii_code_to_font(164,20,7) # Conifer 4
        libtcod.console_map_ascii_code_to_font(165,21,6) # Conifer 5
        libtcod.console_map_ascii_code_to_font(166,21,7) # Conifer 6
        libtcod.console_map_ascii_code_to_font(167,22,6) # Conifer 7
        libtcod.console_map_ascii_code_to_font(168,22,7) # Conifer 8
        libtcod.console_map_ascii_code_to_font(169,23,7) # Conifer Tree-Top

        libtcod.console_map_ascii_code_to_font(170,23,6) # Tree Trunk

        libtcod.console_map_ascii_code_to_font(171,14,5) # Cactus
        libtcod.console_map_ascii_code_to_font(172,15,5) # Cactus Branch 1
        libtcod.console_map_ascii_code_to_font(173,16,5) # Cactus Branch 2
        libtcod.console_map_ascii_code_to_font(174,17,5) # Cactus Branch 3
        libtcod.console_map_ascii_code_to_font(175,18,5) # Cactus Branch 4

        libtcod.console_map_ascii_code_to_font(219,0,6) # Vertical river.
        libtcod.console_map_ascii_code_to_font(220,1,6) # Horizontal river.
        libtcod.console_map_ascii_code_to_font(221,2,6) # 4-way river.
        libtcod.console_map_ascii_code_to_font(222,3,6) # 3-way west river.
        libtcod.console_map_ascii_code_to_font(223,4,6) # 3-way north river.
        libtcod.console_map_ascii_code_to_font(224,5,6) # 3-way east river.
        libtcod.console_map_ascii_code_to_font(225,6,6) # 3-way south river.

        libtcod.console_map_ascii_code_to_font(233,7,6) # Corner north/east river.
        libtcod.console_map_ascii_code_to_font(234,8,6) # Corner south/east river.
        libtcod.console_map_ascii_code_to_font(235,9,6) # Corner south/west river.
        libtcod.console_map_ascii_code_to_font(236,10,6) # Corner north/west river.
        libtcod.console_map_ascii_code_to_font(237,11,6) # Glacier 1
        libtcod.console_map_ascii_code_to_font(238,12,6) # Glacier 2
        libtcod.console_map_ascii_code_to_font(239,11,7) # Glacier 3
        libtcod.console_map_ascii_code_to_font(240,12,7) # Glacier 4
        libtcod.console_map_ascii_code_to_font(245,17,6) # Grass 1
        libtcod.console_map_ascii_code_to_font(246,18,6) # Grass 2
        libtcod.console_map_ascii_code_to_font(247,17,7) # Grass 3
        libtcod.console_map_ascii_code_to_font(248,18,7) # Grass 4
        libtcod.console_map_ascii_code_to_font(249,17,6) # Leaves 1
        libtcod.console_map_ascii_code_to_font(250,18,6) # Leaves 2
        libtcod.console_map_ascii_code_to_font(251,17,7) # Leaves 3
        libtcod.console_map_ascii_code_to_font(252,18,7) # Leaves 4

        libtcod.console_map_ascii_code_to_font(253,4,2) # Up Scroll Arrow
        libtcod.console_map_ascii_code_to_font(254,5,2) # Down Scroll Arrow


    def is_fullscreen(self):
        return self.fullscreen

    def set_fullscreen(self, fullscreen):
        self.fullscreen = fullscreen
        libtcod.console_set_fullscreen(fullscreen)

