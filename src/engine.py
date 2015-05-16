#python2.7-32

import pygame, sys, time;

from pygame import *;

pygame.init();
mainClock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 500

windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Game Name Here")

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

WHITE = (255, 255, 255)

player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load("translateimage.png")
MOVESPEED = 5


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT or event.key == ord("a"):
				moveRight = False
				moveLeft = True
			if event.key == K_RIGHT or event.key == ord("d"):
				moveLeft = False
				moveRight = True
			if event.key == K_UP or event.key == ord("w"):
				moveDown = False
				moveUp = True
			if event.key == K_DOWN or event.key == ord("s"):
				moveUp = False
				moveDown = True
			#if event.key == ord("q"):
				#inventory or menu
			#if event.key == ord("e"):
				#interact

		if event.type == KEYUP:
			if event.key == K_LEFT or event.key == ord("a"):
				moveLeft = False
			if event.key == K_RIGHT or event.key == ord("d"):
				moveRight = False
			if event.key == K_UP or event.key == ord("w"):
				moveUp = False
			if event.key == K_DOWN or event.key == ord("s"):
				moveDown = False		

	windowSurface.fill(WHITE)

	if moveDown and player.bottom < WINDOWHEIGHT:
		player.top += MOVESPEED #player.move
	if moveUp and player.top > 0:
		player.top -= MOVESPEED
	if moveLeft and player.left > 0:
		player.left -= MOVESPEED
	if moveRight and player.right < WINDOWWIDTH:
		player.right += MOVESPEED

	windowSurface.blit(playerImage, player)

	pygame.display.update()
	mainClock.tick(40)





