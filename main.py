import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")

resolution = (400, 320)
screen = pygame.display.set_mode(resolution)

timer = 200
NotEeaten = True
move = 0
phase = ""

body = [[x * -80, 0] for x in range(0, 5)]
foodLocation = []
moves = []

if resolution[0] > resolution[1]:
    leader = resolution[0]

else:
    leader = resolution[1]

while True:
    screen.fill((0, 0, 0))

    # Draw grid
    for i in range(0, leader, 40):
        pygame.draw.line(screen, (255, 255, 255), (0, 0 + i), (resolution[0], 0 + i))
        pygame.draw.line(screen, (255, 255, 255), (0 + i, 0), (0 + i, resolution[1]))

    for event in pygame.event.get():
        # Leave game with exit button
        if event.type == pygame.QUIT:
            pygame.quit()

        # Check which direction to move snake
        if event.type == pygame.KEYDOWN:
            if phase != "R" and event.key == pygame.K_LEFT:
                phase = "L"
                move = -40

            if phase != "L" and event.key == pygame.K_RIGHT:
                phase = "R"
                move = 40

            if phase != "D" and event.key == pygame.K_UP:
                phase = "U"
                move = -40

            if phase != "U" and event.key == pygame.K_DOWN:
                phase = "D"
                move = 40

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP \
                    or event.key == pygame.K_DOWN:
                if len(moves) > 0:
                    if phase != moves[0]:
                        moves.append(phase)

                else:
                    moves.append(phase)

    # If direction chosed the first time
    if move != 0:
        pygame.time.wait(int(timer))

        # Food
        if NotEeaten:
            foodLocation = random.choice([[x, y] for x in range(0, resolution[0], 40)
                                          for y in range(0, resolution[1], 40) if
                                          [x, y] not in body])
            NotEeaten = False

        elif not NotEeaten:
            pygame.draw.rect(screen, (0, 200, 0), (foodLocation[0], foodLocation[1], 40, 40))

        # Boundries
        if body[0][0] <= -40:
            body[0][0] = resolution[0] - 40

        elif body[0][0] >= resolution[0]:
            body[0][0] = 0

        elif body[0][1] <= -40:
            body[0][1] = resolution[1] - 40

        elif body[0][1] >= resolution[1]:
            body[0][1] = 0

        # Last part of body moves behind the head
        body.remove(body[len(body) - 1])
        body.insert(1, [body[0][0], body[0][1]])

        # Keep moving the head
        if len(moves) > 1:
            moves.remove(moves[0])

        if moves[0] == "L" or moves[0] == "R":
            body[0][0] += move

        elif moves[0] == "U" or moves[0] == "D":
            body[0][1] += move

        # Check if food eaten
        if body[0] == foodLocation:
            body.append(body[len(body) - 1])

            foodLocation = []
            NotEeaten = True

    # Draw body and check for Game Over
    for index in range(0, len(body)):
        if body[0] == body[index] and index != 0:
            pygame.quit()

        elif index == 0:
            pygame.draw.rect(screen, (128, 19, 11), (body[0][0], body[0][1], 40, 40))

        else:
            pygame.draw.rect(screen, (176, 23, 12),
                             (body[index][0], body[index][1], 40, 40))

    pygame.display.update()
