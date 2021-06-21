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
    window = pygame.display.set_mode([WIDTH, HEIGHT], pygame.FULLSCREEN)
    pygame.display.set_caption("Egg Hunt Game")
    clock = pygame.time.Clock()
    
    fSize = 25
    bfSize = 40

    font = pygame.font.SysFont('fira code', fSize)
    biggerFont = pygame.font.SysFont('fira code', bfSize)
    enemyLimit = 100

    player = PlayerWS(spawn = {'x': WIDTH // 2 - 8, 'y': HEIGHT // 2 - 8}, timeLimit=60)

    startTime = time.time()

    spawning = True
    spawningColour = (0, 255, 0)

    eggs = pygame.sprite.Group()

    timeRemaining = 0
    timer = f"Timer: {timeRemaining}"

    eggRadius = 15

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.unicode:
                    if pygame.key.key_code(event.unicode) == player.controls['toggleSprint']:
                        player.sprinting = not player.sprinting
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] >= WIDTH-30 and mouse[0] <= WIDTH-5 and mouse[1] >= 5 and mouse[1] <= 30:
                    spawning = not spawning
                    spawningColour = (255, 0, 0) if not spawning else (0, 255, 0)

        keys = pygame.key.get_pressed()

        if spawning:
            if len(eggs) <= enemyLimit:
                eggChoice = random.randint(1, 100)
                spawn = {
                    'x': random.randint(20, WIDTH-20),
                    'y': random.randint(20, HEIGHT-120)
                }

                if eggChoice <= 50: eggs.add(Egg(spawn, eggRadius))
                elif eggChoice > 50 and eggChoice <= 80: eggs.add(StaminaEgg(spawn, eggRadius))
                elif eggChoice > 80 and eggChoice <= 95: eggs.add(TimeEgg(spawn, eggRadius))
                elif eggChoice > 95 and eggChoice <= 99: eggs.add(TripleEgg(spawn, eggRadius))
                elif eggChoice > 99 and eggChoice <= 100: eggs.add(BombEgg(spawn, eggRadius*2))


        window.fill((255, 255, 255))

        pygame.draw.rect(window, (120, 120, 120), (
            0, HEIGHT-100, WIDTH, 100
        )) # bottom bar

        # Bars to display: 
        # stamina
        # time limit

        # 50px bar 100px bar 50px

        # pygame.draw.rect(window, (255, 0, 0), (
        #     0, HEIGHT-50, WIDTH, 50
        # )) # mid bar

        pygame.draw.rect(window, (0, 200, 0), (
            45, HEIGHT-80, ((WIDTH - 200) // 2) + 10, 60
        )) # stamina outline

        pygame.draw.rect(window, (0, 0, 255), (
            ((WIDTH - 200) // 2) + 145, HEIGHT-80, ((WIDTH - 200) // 2) + 10, 60
        )) # time limit

        pygame.draw.rect(window, (0, 255, 0), (
            50, HEIGHT-75, ((WIDTH - 200) // 2) * player.stamina / player.staminaLimit, 50
        )) # stamina bar        

        pygame.draw.rect(window, (0, 100, 150), (
            ((WIDTH - 200) // 2) + 150, HEIGHT-75, ((WIDTH - 200) // 2) * player.timeRemaining / player.timeLimit, 50
        )) # time limit

        pygame.draw.rect(window, (spawningColour), (
            WIDTH - 30, 5, 25, 25
        )) # toggle spawn

        

        colGroup = pygame.sprite.spritecollide(player, eggs, False)

        curTime = time.time()

        timeRemaining = int((startTime - curTime) + player.timeLimit)

        if startTime + player.timeLimit <= curTime:
            return endScreen(player.score)
        
        if player.score < 0:
            return endScreen(player.score)

        for e in colGroup:
            e.onEat(player)
            

        for e in eggs:
            e.draw(window)
            e.checkRadius(player)

        player.draw(window)
        player.update(keys)
        player.updateTime(timeRemaining)

        scoreDisp = font.render(f"Score: {player.score}", True, (0, 0, 0))
        timerDisp = biggerFont.render(str(timeRemaining), True, (0, 0, 0))
        staminaLimitDisp = biggerFont.render(f"{int(player.stamina)}/{player.staminaLimit}", True, (0, 0, 0))

        # pygame.draw.line(window, (0, 0, 0),
        #     (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 1
        # )
        # pygame.draw.line(window, (0, 0, 0),
        #     (WIDTH // 2, 0), (WIDTH //2, HEIGHT), 1
        # )

        # pygame.draw.line(window, (0, 0, 0),
        #     (0, 0), (WIDTH, HEIGHT) , 1
        # )

        # pygame.draw.line(window, (0, 0, 0),
        #     (WIDTH, 0), (0, HEIGHT), 1
        # )

        # To show center of screen

        window.blit(scoreDisp, [0, 0])
        window.blit(timerDisp, [((WIDTH // 4)*3), HEIGHT - 70])
        window.blit(staminaLimitDisp, [(WIDTH // 4) - 80, HEIGHT - 70])

        clock.tick(FPS)
        pygame.display.flip()

def endScreen(score):
    window = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Congratulations")

    font = pygame.font.SysFont('arial', 50)

    finalText = font.render(f'Final Score: {score}', True, (0, 0, 0))

    button = Button([WIDTH // 2 - 48, HEIGHT // 2 + 32], "Restart", func=main)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button.onClick(list(pygame.mouse.get_pos()))


        window.fill((255, 255, 255))

        button.draw(window)
        
        window.blit(finalText, [(WIDTH // 2) - 150, (HEIGHT // 2) - 25])

        pygame.display.flip()


if __name__ == "__main__":
    main()

