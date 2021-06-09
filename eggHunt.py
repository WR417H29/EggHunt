import pygame
import random
import time

from utils.consts import WIDTH, HEIGHT, FPS
from components.base.button import Button
from components.players.playerws import PlayerWS
from components.enemies.egg import Egg
from components.enemies.staminaEgg import StaminaEgg
from components.enemies.timeEgg import TimeEgg
from components.enemies.tripleEgg import TripleEgg
from components.enemies.bombEgg import BombEgg


def main():
    window = pygame.display.set_mode([WIDTH, HEIGHT+100])
    pygame.display.set_caption("Egg Hunt Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('arial', 25)
    biggerFont = pygame.font.SysFont('arial', 45)
    enemyLimit = 100

    player = PlayerWS(spawn = {'x': WIDTH // 2 + 8, 'y': HEIGHT // 2 + 8}, timeLimit=60000)

    startTime = time.time()

    eggs = pygame.sprite.Group()

    timeRemaining = 0
    timer = f"Timer: {timeRemaining}"

    eggRadius = 500

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode:
                    if pygame.key.key_code(event.unicode) == player.controls['toggleSprint']:
                        player.sprinting = not player.sprinting

        keys = pygame.key.get_pressed()

        if len(eggs) <= enemyLimit:
            eggChoice = random.randint(1, 100)
            spawn = {
                'x': random.randint(100, WIDTH-100),
                'y': random.randint(100, HEIGHT-100)
            }

            # if eggChoice <= 50: eggs.add(Egg(spawn, eggRadius))
            # elif eggChoice > 50 and eggChoice <= 65: eggs.add(StaminaEgg(spawn, eggRadius))
            # elif eggChoice > 65 and eggChoice <= 80: eggs.add(TimeEgg(spawn, eggRadius))
            # elif eggChoice > 80 and eggChoice <= 95: eggs.add(TripleEgg(spawn, eggRadius))
            # elif eggChoice > 95 and eggChoice <= 100: eggs.add(BombEgg(spawn, eggRadius+5))

            eggs.add(StaminaEgg(spawn, eggRadius))

        window.fill((255, 255, 255))

        pygame.draw.rect(window, (0, 255, 0), (
            0, HEIGHT, WIDTH*(player.stamina/player.staminaLimit), 100
        )) # bottom bar

        colGroup = pygame.sprite.spritecollide(player, eggs, False)

        curTime = time.time()

        timeRemaining = int((startTime - curTime) + player.timeLimit)

        if startTime + player.timeLimit <= curTime:
            return endScreen(player.score)
        
        if player.score <= 0:
            return endScreen(player.score)

        for e in colGroup:
            e.onEat(player)
            

        for e in eggs:
            e.draw(window)
            e.checkRadius(player)

        player.draw(window)
        player.update(keys)

        scoreDisp = font.render(f"Score: {player.score}", True, (0, 0, 0))
        timerDisp = font.render(f"Timer: {timeRemaining}", True, (0, 0, 0))
        staminaLimitDisp = biggerFont.render(f"{player.stamina}/{player.staminaLimit}", True, (0, 0, 0))

        window.blit(scoreDisp, [0, 0])
        window.blit(timerDisp, [0, 25])
        window.blit(staminaLimitDisp, [WIDTH // 2 - 25, HEIGHT + 50])

        clock.tick(FPS)
        pygame.display.flip()

def endScreen(score):
    window = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Congratulations")

    font = pygame.font.SysFont('arial', 50)

    finalText = font.render(f'Final Score: {score}', True, (0, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        window.fill((255, 255, 255))
        
        window.blit(finalText, [(WIDTH // 2) - 150, (HEIGHT // 2) - 25])

        pygame.display.flip()


if __name__ == "__main__":
    main()

