import arcade as dungeon
import random

# САЛАМ КАБАНАМ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "BillyWars"
GANTEL_SPEED = 5
OSU_BALL_SPEED = 1
OSU_DISTANCE = 50

class Billy(dungeon.Sprite):
    def __init__(self):
        super().__init__("img.png", 0.2)

    def update(self):
        self.center_x += self.change_x


class Gantel(dungeon.Sprite):
    def __init__(self):
        super().__init__("gan.png", 0.1)
        self.center_x = windows.b.center_x
        self.center_y = windows.b.center_y
        self.change_y = GANTEL_SPEED
        self.gantel_sound1 = dungeon.load_sound("h.wav")
        self.gantel_sound2 = dungeon.load_sound("woo.wav")
        self.gantel_sound3 = dungeon.load_sound("spank1.wav")
        self.kill_sound = dungeon.load_sound("spank.wav")
        self.change_angle = 20
        self.randomsound = []
        self.randomsound.append(self.gantel_sound1)
        self.randomsound.append(self.gantel_sound2)
        self.randomsound.append(self.gantel_sound3)
        self.gantel_sound = random.choice(self.randomsound)
        self.gantel_sound.play()

    def update(self):
        self.angle += self.change_angle
        self.center_y += self.change_y
        if self.center_y >= SCREEN_HEIGHT:
            self.kill()

class PowerGantel(dungeon.Sprite):
    def __init__(self):
        super().__init__("power.g.png", 0.1)
        self.center_x = windows.b.center_x
        self.center_y = windows.b.center_y
        self.change_y = GANTEL_SPEED
        self.power_sound = dungeon.load_sound("spit-yeeeeeaaaahhh.wav")
        self.kill_sound = dungeon.load_sound("spank.wav")

        self.power_sound.play()
        self.change_angle = 20

    def update(self):
        self.angle += self.change_angle
        self.center_y += self.change_y
        if self.center_y >= SCREEN_HEIGHT:
            self.kill()


class OsuBall(dungeon.Sprite):
    def __init__(self):
        super().__init__("osu.png", 0.09)
        self.change_y = OSU_BALL_SPEED

    def update(self):
        self.center_y -= self.change_y
        if self.center_y <= 0:
            self.kill()

class Gays(dungeon.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = dungeon.load_texture("kac.jpg")
        self.b = Billy()
        self.ganteli = dungeon.SpriteList()
        self.osuballs = dungeon.SpriteList()
        self.gays = True
        self.win = dungeon.load_texture("img_1.png")
        self.shetchik = 0
        self.power_ganteli = dungeon.SpriteList()
        self.win_sound = dungeon.load_sound("pobeda.wav")

    def setup(self):
        self.win_sound.play()
        self.b.center_x = SCREEN_WIDTH/2
        self.b.center_y = 90
        for i in range(50):
            osuball = OsuBall()
            osuball.center_x = random.randint(0, SCREEN_WIDTH)
            osuball.center_y = SCREEN_HEIGHT + i * OSU_DISTANCE
            self.osuballs.append(osuball)


    def on_draw(self):
        self.clear((255, 255, 255))
        dungeon.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.b.draw()
        self.ganteli.draw()
        self.osuballs.draw()
        self.power_ganteli.draw()
        if len(self.osuballs) == 0:
            self.gays = False
            dungeon.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.win)


    def update(self, delta_time):
        if self.gays:
            self.b.update()
            self.ganteli.update()
            self.osuballs.update()
            self.power_ganteli.update()
            for gantelya in self.ganteli:
                hitlist = dungeon.check_for_collision_with_list(gantelya, self.osuballs)
                if hitlist:
                    gantelya.kill_sound.play()
                    gantelya.kill()
                    for osuball in hitlist:
                        osuball.kill()
        for gantelya in self.power_ganteli:
            hitlist = dungeon.check_for_collision_with_list(gantelya, self.osuballs)
            if hitlist:
                gantelya.kill_sound.play()

                for osuball in hitlist:
                    osuball.kill()

    def on_key_press(self, key, modifiers):
        if self.gays:
            if key == dungeon.key.A:
                self.b.change_x = -5
            if key == dungeon.key.D:
                self.b.change_x = 5
            if key ==  dungeon.key.SPACE:
                self.shetchik += 1
                if self.shetchik % 10 == 0:
                    power_gantelya = PowerGantel()
                    self.power_ganteli.append(power_gantelya)
                else:
                    gantel = Gantel()
                    self.ganteli.append(gantel)



    def on_key_release(self, key, modifiers):
        if self.gays:
            if key == dungeon.key.A or key == dungeon.key.D:
                self.b.change_x = 0











windows = Gays(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
windows.setup()


dungeon.run()