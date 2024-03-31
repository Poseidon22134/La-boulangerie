import pygame


class App:
    SCREEN_RES = (384, 288)

    def __init__(self):
        self.screen = pygame.display.set_mode(self.SCREEN_RES, pygame.SCALED)

        pygame.display.set_caption("La boulangerie | The bakery")
        pygame.display.set_icon(pygame.image.load("assets/ui/icon_32.png").convert_alpha())

        self.clock = pygame.time.Clock()
        self.fps = 0

        self.running = True

        self.textures = {
            "cupboard": pygame.image.load("assets/backgrounds/arches.png").convert_alpha(),
            "mixing": pygame.image.load("assets/backgrounds/mixing.png").convert_alpha(),
            "oven": pygame.image.load("assets/backgrounds/oven.png").convert_alpha(),
            "bread_cooked": pygame.image.load("assets/ui/icon_64.png").convert_alpha(),
            "dough": pygame.image.load("assets/backgrounds/dough.png").convert_alpha(),
            "semicooked": pygame.image.load("assets/backgrounds/semicooked.png").convert_alpha(),
            "ash": pygame.image.load("assets/backgrounds/ash.png").convert_alpha(),
            "pot": pygame.image.load("assets/backgrounds/pot.png").convert_alpha(),
            "flour": pygame.image.load("assets/backgrounds/flour.png").convert_alpha(),
            "water": pygame.image.load("assets/backgrounds/water.png").convert_alpha(),
        }

        self.accel = 0
        self.game_screen = 2
        self.screens = ["oven", "mixing", "cupboard"]

        self.storage = [["", "water", "flour"], ["water", "", "flour"], ["pot", "flour", ""]]
        self.storage_positions = [(24, 80), (104, 80), (208, 80)]

    def update(self):
        self.clock.tick()
        self.fps = self.clock.get_fps()
        if not self.fps:
            return

        # self.bread_level += 1 / self.fps

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.accel > -0.001:
            self.accel -= 0.00001
        elif keys[pygame.K_RIGHT] and self.accel < 0.001:
            self.accel += 0.00001
        else:
            self.accel /= 1.01
        self.game_screen = max(0, min(2, self.game_screen + self.accel))

    def render(self):
        self.screen.fill("#a08662")

        # backgrounds
        for i, screen in enumerate(self.screens):
            self.screen.blit(self.textures[screen], (i * self.SCREEN_RES[0] - self.game_screen * self.SCREEN_RES[0], 0))

        for y, shelf in enumerate(self.storage):
            for x, item in enumerate(shelf):
                if item == "":
                    continue
                self.screen.blit(self.textures[item], (x * self.storage_positions[y][1] + 80 - self.game_screen * self.SCREEN_RES[0] + self.SCREEN_RES[0] * 2, self.storage_positions[y][0]))

        # self.screen.blit(self.textures[level], (180, 186))

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            if not self.fps:
                continue
            self.render()


if __name__ == "__main__":
    app = App()
    app.run()
