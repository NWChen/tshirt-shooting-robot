import math
import pygame
import random

pygame.init()
size = (1000, 1000)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
i = 0

while True:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	i+=1
	rect = pygame.Rect(500, 500, 50, 50)
	pygame.draw.rect(screen, (255, 255, 255), rect)
	pygame.transform.rotate(rect, math.radians(i))
	pygame.display.flip()
	clock.tick(60)

pygame.quit()